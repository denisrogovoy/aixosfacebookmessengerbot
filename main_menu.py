import re
import buttons
import faq_menu, texts

def main_options(bot, recipient_id, recipient_message, account):
    if re.match(r'(?i)(.*((FAQ)|(поширені питання)).*)', recipient_message):
        bot.send_raw({"recipient": {"id": recipient_id}, "messaging_type": "RESPONSE", "message":buttons.faq_menu})
    elif re.match(r'(?i)(.*((Personal account)|(особ.*кабінет)).*)', recipient_message):
        if account:
            bot.send_raw({"recipient": {"id": recipient_id}, "message": buttons.control_panel})
        else:
            bot.send_raw({"recipient": {"id": recipient_id}, "messaging_type": "RESPONSE", "message": buttons.share_phone})
    elif re.match(r'(?i)(.*((help)|(довідка)|(допомога)).*)', recipient_message):
        bot.send_text_message(recipient_id, texts.help)
    elif re.match(r'(?i)(.*((feedback)|((зв\'язок)|(написати)|(зв\'язатися).*викладач)).*)', recipient_message):
        bot.send_text_message(recipient_id, "Задай питання, яке тебе цікавить викладачу нижче:")
    else:
        faq_menu.faq_options(bot, recipient_id, recipient_message)