from json import load, dump



# Текущая версия бомбера
VERSION = '1.07'

URL_CHANNEL='https://t.me/+i5AhxcIinEVkZjAy'

# Стандартный цвет программы
MY_COLOR = 'PURPLE_400'

#Та самая функция с добавлением прокси, синтаксис PROXY='http://user:password@127.0.0.1:1080' 
PROXY=None

# Название конфига
CONFIG_NAME = 'config.json'



def check_config():
    '''Просмотр конфига'''

    while True:
        try:
            with open(CONFIG_NAME) as f:
                return load(f)
        except:
            with open(CONFIG_NAME, 'w') as f:
                f.write('{"theme": "dark", "feedback": "True", "type_attack": "MIX", "attack": "False", "key": "", "color": "deeppurpleaccent100"}')



def change_config(key, value):
    '''Редактирование конфига'''

    config = check_config()
    config[key] = f'{value}'
    with open(CONFIG_NAME, 'w') as f:
        dump(config, f)


