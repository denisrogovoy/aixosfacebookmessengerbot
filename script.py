import random
import requests
from flask import Flask, request, render_template
from pymessenger.bot import Bot
import time, re
import buttons, texts, main_menu, faq_menu
import json
import secrets

app = Flask(__name__, static_url_path='')

ACCESS_TOKEN = secrets.token_access
VERIFY_TOKEN = secrets.token_verify

bot = Bot(ACCESS_TOKEN)
account=False
responseUserInfo=dict()

@app.route('/control')
def control():
    return render_template('controlTeacher.html', **responseUserInfo)

@app.route('/changes')
def changes():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


#Получать сообщения, посылаемые фейсбуком нашему боту мы будем в этом терминале вызова
@app.route('/', methods=['GET', 'POST'])
def receive_message():
    global account
    global responseUserInfo
    if request.method == 'GET':
    # до того как позволить людям отправлять что-либо боту, Facebook проверяет токен,
    # подтверждающий, что все запросы, получаемые ботом, приходят из Facebook
        token_sent = request.args['hub.verify_token']
        return verify_fb_token(token_sent)
    # если запрос не был GET, это был POST-запрос и мы обрабатываем запрос пользователя
    else:
        # получаем сообщение, отправленное пользователем для бота в Facebook
        output = request.get_json()
        #typing_message={"recipient": {"id": "<PSID>"}, "sender_action": "typing_on"}
        print(output)
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                recipient_id = message['sender']['id']

                if message.get('message'):
                    bot.send_raw({"recipient": {"id": recipient_id}, "sender_action": "typing_on"})
                    bot.send_raw({"recipient": {"id": recipient_id}, "sender_action": "mark_seen"})
                    time.sleep(2)
                    if message['message'].get('quick_reply'):
                        if message['message']['quick_reply'].get('payload'):
                            quick_reply = message['message'].get('quick_reply').get('payload')
                            if quick_reply in ["Tasks", "Schedule", "Requirements", "Work with WPARs", "Interesting facts"]:
                                faq_menu.faq_options(bot, recipient_id, quick_reply)
                            if re.match(r'(\+\d\d\d\d\d\d\d\d\d\d\d\d)', quick_reply):
                                bot.send_raw({"recipient": {"id": recipient_id}, "messaging_type": "RESPONSE",
                                              "message": buttons.share_email})
                            elif re.match(r'.*@.*', quick_reply):
                                bot.send_text_message(recipient_id, "Вітаю! 😉 Ви увійшли до особистого кабінету викладача 🎓.")
                                account=True
                                response=requests.get("https://graph.facebook.com/" + recipient_id + "?fields=first_name,last_name,profile_pic&access_token="+ACCESS_TOKEN)
                                responseUserInfo=json.loads(response.text)
                                responseUserInfo.update({"psid": recipient_id})
                                responseUserInfo.update({"mlistlen": 3})
                                responseUserInfo.update({"wpars":[["wpar1", "A", "S", "wpar1", "/wpars/wpar1"],
                                                                  ["wpar2", "A", "S", "wpar2", "/wpars/wpar2"],
                                                                  ["wpar3", "A", "S", "wpar3", "/wpars/wpar3"],
                                                         ]})

                                print(responseUserInfo)
                                bot.send_raw({"recipient": {"id": recipient_id}, "message": buttons.control_panel})
                    elif message['message'].get('text'):
                        recipient_message = message['message'].get('text')
                        #bot.send_raw({"recipient": {"id": recipient_id}, "sender_action": "typing_off"})
                        main_menu.main_options(bot, recipient_id, recipient_message, account)
                        #send_message(recipient_id, response_sent_text)
                    #если пользователь отправил GIF, фото, видео и любой не текстовый объект
                    elif message['message'].get('attachments'):
                        #response_sent_nontext = get_message()
                        #send_message(recipient_id, response_sent_nontext)
                        pass
                    #typing_message = {"recipient": {"id": recipient_id}, "sender_action": "typing_off"}
                    bot.send_raw({"recipient": {"id": recipient_id}, "sender_action": "typing_off"})
                elif message.get('postback'):
                    bot.send_raw({"recipient": {"id": recipient_id}, "sender_action": "typing_on"})
                    bot.send_raw({"recipient": {"id": recipient_id}, "sender_action": "mark_seen"})
                    time.sleep(2)
                    if message['postback']['payload']=="Start new dialog":
                        bot.send_text_message(recipient_id, texts.welcome)
                        bot.send_raw({"recipient": {"id": recipient_id}, "sender_action": "typing_on"})
                        time.sleep(1)
                        bot.send_text_message(recipient_id, texts.hint)
                        bot.send_raw({"recipient": {"id": recipient_id},
                                      "message": '{"attachment":{"type":"image", "payload":{"attachment_id": "1125925454538660"}}}'})
                    elif message['postback']['payload'] in ["FAQ", "Personal account", "Help", "Feedback", "Який розклад лабораторних робіт?", "Які вимоги до звіту?"]:
                        main_menu.main_options(bot, recipient_id, message['postback']['payload'], account)
                    bot.send_raw({"recipient": {"id": recipient_id}, "sender_action": "typing_off"})
                elif message.get('referral'):
                    refsource=message['referral']['ref']
                    if refsource=="qr-code":
                        bot.send_raw({"recipient": {"id": recipient_id}, "sender_action": "typing_on"})
                        bot.send_raw({"recipient": {"id": recipient_id}, "sender_action": "mark_seen"})
                        time.sleep(1)
                        bot.send_text_message(recipient_id, texts.welcome)
                        print("kdkdkkdkdkdkd")
                        bot.send_raw({"recipient": {"id": recipient_id}, "sender_action": "typing_on"})
                        time.sleep(1)
                        bot.send_text_message(recipient_id, texts.hint)
                        bot.send_raw({"recipient": {"id": recipient_id},
                                      "message": '{"attachment":{"type":"image", "payload":{"attachment_id": "1125925454538660"}}}'})
                        bot.send_raw({"recipient": {"id": recipient_id}, "sender_action": "typing_off"})
                    print(refsource)

        return "Message Processed"

def verify_fb_token(token_sent):
    '''Сверяет токен, отправленный фейсбуком, с имеющимся у вас.
    При соответствии позволяет осуществить запрос, в обратном случае выдает ошибку.'''
    if token_sent == VERIFY_TOKEN:
        return request.args['hub.challenge']
    else:
        return 'Invalid verification token'

def send_message(recipient_id, response):
    '''Отправляет пользователю текстовое сообщение в соответствии с параметром response.'''
    bot.send_text_message(recipient_id, response)
    return 'Success'



if __name__ == '__main__':
    context = ('fullchain.pem', 'privkey.pem')
    app.run(host='0.0.0.0', port=443, debug=True, ssl_context=context)
