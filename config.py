# (c) @JigarVarma2005

import os


class Config(object):
    # get it from my.telegram.org
    APP_ID = os.environ.get("APP_ID", 27190467)
    API_HASH = os.environ.get("API_HASH", "ff6bc6ad2faba520f426cf04ca7f5773")
    # Get it from @botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7442771033:AAFtr-5VeWahz-0aS5aAv3OWUDwDPUNYqNc")
    # Leave this defualt
    SESSION_NAME = os.environ.get("SESSION_NAME", "JV_CaptchaBot")
    # get it from https://cloud.mongodb.com 
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://raretrack907:nROK1YKWq7ytVfkz@sharktheaquaking.nqcqmbv.mongodb.net/?retryWrites=true&w=majority&appName=SharkTheAquaKing")
    # Ask in https://t.me/JV_Community
    API_TOKEN = os.environ.get("API_TOKEN", None)
    # Sudo users(goto @JVToolsBot and send /id to get your id)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "6066102279 7102604217").split()))
    SUDO_USERS.append(6066102279)
    SUDO_USERS = list(set(SUDO_USERS))
