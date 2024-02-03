LEXICON_RU: dict[str, str] = {
    '/start': 'Привет!\n\nЗдесь можно записать и сохранить свой текущий вес.\n'
              'Или записать замеры своего тела и сохранить их.\n'
              'Помощь по команде /help',
    '/help': 'Список команд бота:\n'
             '/start - запустить бот\n'
             '/help - список команд\n',
    '/profile': 'Let`s fill your profile\n'
                'If you want to stop filling profile - send /cancel\n\n'
                'What is your name?',
    '/cancel': 'Nothing to cancel',
    'other_answers': 'Я понимаю не все сообщения.\n'
                     '/help - cписок доступных команд'
}

LEXICON_COMMANDS_RU: dict[str, str] = {
    '/help': 'How this bot works',
    '/profile': 'Setup you profile',
}

LEXICON_FSM: dict[str, str] = {
    'name': 'What is your name?',
    'age': 'How old are you?',
    'gender': 'What is your gender?',
    'weight': 'What is your current weight?',
    'profile_done': 'Thank you. Yor profile was updated',
    'not_name': 'You sent not name\n\n'
                'Send you name please\n'
                'or send /cancel if you want to stop',
    'not_age': 'You sent not correct age\n\n'
               'Please send number between 18 and 120\n'
               'or send /cancel if you want to stop',
    'not_weight': 'You sent not correct weight\n\n'
                  'Please send number between 20 and 700\n'
                  'or send /cancel if you want to stop',
    'not_gender': 'Please, use button to choose your gender\n\n'
                  'or send /cancel if you want to stop',
    '/cancel': 'You have stopped FSM\n'
               'If you want to fill your profile - send /profile'
}
