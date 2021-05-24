faq_menu = '''{
    "text": "Обери питання, яке тебе цікавить ❓:",
    "quick_replies":[
      {
        "content_type":"text",
        "title":"Завдання",
        "payload":"Tasks"
      },{
        "content_type":"text",
        "title":"Розклад",
        "payload":"Schedule"
      },{
        "content_type":"text",
        "title":"Вимоги до звіту",
        "payload":"Requirements"
      },{
        "content_type":"text",
        "title":"Робота з WPARs",
        "payload":"Work with WPARs"
      },{
        "content_type":"text",
        "title":"Цікаві факти",
        "payload":"Interesting facts"
      }
    ]
  }'''

button_putty = {
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"button",
        "text":"PuTTY - вільно розповсюджуваний клієнт для різних протоколів віддаленого доступу, включаючи SSH, Telnet, rlogin:",
        "buttons":[
          {
            "type":"web_url",
            "url":"https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html",
            "title":"Завантажити PuTTY",
            "webview_height_ratio": "full"
          }
        ]
      }
    }
  }

control_panel = {
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"button",
        "text":"Відкрити панель керування:",
        "buttons":[
          {
            "type":"web_url",
            "url":"https://aixosbot.pp.ua/control",
            "title":"Панель керування",
            "webview_height_ratio": "tall",
            "messenger_extensions": "true",
            "fallback_url":"https://aixosbot.pp.ua/control"
          }
        ]
      }
    }
  }


share_phone = '''{
    "text": "Для того, щоб увійти у свій особистий кабінет пройдіть аутентифікацію за допомогою навчальної платформи Moodle 🗝. Будь-ласка, надішліть свій номер мобільного телефону 📞:",
    "quick_replies":[
      {
        "content_type":"user_phone_number"
      }]
}
'''

share_email = '''{
    "text": "Будь-ласка, надішліть свій email 📬:",
    "quick_replies":[
      {
        "content_type":"user_email"
      }]
}
'''

tasks = '''{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"generic",
        "elements":[
           {
            "title":"Лабораторна робота №1",
            "image_url":"https://viberbotbucket.s3.eu-gb.cloud-object-storage.appdomain.cloud/landing/shell.png",
            "subtitle":"Основи роботи з Shell",
            "default_action": {
              "type": "web_url",
              "url": "https://drive.google.com/file/d/1kRq5fmN-wINjBuxDN6hmm4EsQ3I_FLi8/view?usp=sharing",
              "webview_height_ratio": "tall",
            },
            "buttons":[
              {
                "type":"web_url",
                "url":"https://drive.google.com/file/d/1kRq5fmN-wINjBuxDN6hmm4EsQ3I_FLi8/view?usp=sharing",
                "title":"Відкрити"
              }             
            ]      
          },
          {
            "title":"Лабораторна робота №2",
            "image_url":"https://viberbotbucket.s3.eu-gb.cloud-object-storage.appdomain.cloud/landing/textEditor.png",
            "subtitle":"Текстові редактори в ОС AIX",
            "default_action": {
              "type": "web_url",
              "url": "https://drive.google.com/file/d/1hGwd5RDr4JoFCjK9e8r0AZrqNLXN7irE/view?usp=sharing",
              "webview_height_ratio": "tall",
            },
            "buttons":[
              {
                "type":"web_url",
                "url":"https://drive.google.com/file/d/1hGwd5RDr4JoFCjK9e8r0AZrqNLXN7irE/view?usp=sharing",
                "title":"Відкрити"
              }             
            ]      
          },
          {
            "title":"Лабораторна робота №3",
            "image_url":"https://viberbotbucket.s3.eu-gb.cloud-object-storage.appdomain.cloud/landing/regex.jpeg",
            "subtitle":"Регулярні вирази, команда grep",
            "default_action": {
              "type": "web_url",
              "url": "https://drive.google.com/file/d/1QFDP9wbosKtVpohAzqeWz2kEDyJbIMKN/view?usp=sharing",
              "webview_height_ratio": "tall",
            },
            "buttons":[
              {
                "type":"web_url",
                "url":"https://drive.google.com/file/d/1QFDP9wbosKtVpohAzqeWz2kEDyJbIMKN/view?usp=sharing",
                "title":"Відкрити"
              }             
            ]      
          },
          {
            "title":"Лабораторна робота №4",
            "image_url":"https://viberbotbucket.s3.eu-gb.cloud-object-storage.appdomain.cloud/landing/sed.png",
            "subtitle":"Потоковий редактор SED. Процесор мови обробки шаблонів AWK",
            "default_action": {
              "type": "web_url",
              "url": "https://drive.google.com/file/d/1q-qu8N54GU_xlXGgTob64Y5pM26J4RNm/view?usp=sharing",
              "webview_height_ratio": "tall",
            },
            "buttons":[
              {
                "type":"web_url",
                "url":"https://drive.google.com/file/d/1q-qu8N54GU_xlXGgTob64Y5pM26J4RNm/view?usp=sharing",
                "title":"Відкрити"
              }             
            ]      
          },
          {
            "title":"Лабораторна робота №5",
            "image_url":"https://viberbotbucket.s3.eu-gb.cloud-object-storage.appdomain.cloud/landing/bash.png",
            "subtitle":"Програмування мовою оболонки bash",
            "default_action": {
              "type": "web_url",
              "url": "https://drive.google.com/file/d/1lmv07r3PLgtEHhoWQKFpadF5z0bS_X-C/view?usp=sharing",
              "webview_height_ratio": "tall",
            },
            "buttons":[
              {
                "type":"web_url",
                "url":"https://drive.google.com/file/d/1lmv07r3PLgtEHhoWQKFpadF5z0bS_X-C/view?usp=sharing",
                "title":"Відкрити"
              }             
            ]      
          },
          {
            "title":"Лабораторна робота №6",
            "image_url":"https://viberbotbucket.s3.eu-gb.cloud-object-storage.appdomain.cloud/landing/python.png",
            "subtitle":"Мова програмування Python у системному адмініструванні ОС AIX",
            "default_action": {
              "type": "web_url",
              "url": "https://drive.google.com/file/d/1JF61tUmlc4y397-4nAfYLaAmKfYs1cTE/view?usp=sharing",
              "webview_height_ratio": "tall",
            },
            "buttons":[
              {
                "type":"web_url",
                "url":"https://drive.google.com/file/d/1JF61tUmlc4y397-4nAfYLaAmKfYs1cTE/view?usp=sharing",
                "title":"Відкрити"
              }             
            ]      
          },
          {
            "title":"Лабораторна робота №7",
            "image_url":"https://viberbotbucket.s3.eu-gb.cloud-object-storage.appdomain.cloud/landing/aix.png",
            "subtitle":"Додаткові можливості ОС AIX",
            "default_action": {
              "type": "web_url",
              "url": "https://drive.google.com/file/d/1ZjaHuOvCq4HJ04wQOGK09LeQukqhwSqF/view?usp=sharing",
              "webview_height_ratio": "tall",
            },
            "buttons":[
              {
                "type":"web_url",
                "url":"https://drive.google.com/file/d/1ZjaHuOvCq4HJ04wQOGK09LeQukqhwSqF/view?usp=sharing",
                "title":"Відкрити"
              }             
            ]      
          }
        ]
      }
    }
}'''