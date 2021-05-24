import re
import random
import buttons, texts


def faq_options(bot, recipient_id, recipient_message):
    if re.match(r'(?i)(.*((tasks)|(завдання)).*)', recipient_message):
        bot.send_raw({"recipient": {"id": recipient_id}, "message": buttons.tasks})
    elif re.match(r'(?i)(.*((schedule)|(розклад)).*)', recipient_message):
        bot.send_text_message(recipient_id, texts.schedule)
    elif re.match(r'(?i)(.*((requirements)|(вимог.*звіт)).*)', recipient_message):
        bot.send_text_message(recipient_id, texts.requirements)
    elif re.match(r'(?i)(.*((work with wpar)|(робот.*wpar)).*)', recipient_message):
        bot.send_text_message(recipient_id, texts.connect_ssh)
        bot.send_raw({"recipient": {"id": recipient_id}, "message": buttons.button_putty})
    elif re.match(r'(?i)(.*((interest.*fact)|(цікав.*факт)).*)', recipient_message):
        bot.send_text_message(recipient_id, texts.interesting_facts[random.randint(0, 4)])