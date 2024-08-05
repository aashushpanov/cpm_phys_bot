import os

env_vars = os.environ.copy()

BOT_TOKEN = str(env_vars.get('BOT_TOKEN'))
URL = str(env_vars.get("URL_VPS"))
