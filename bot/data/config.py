import os

env_vars = os.environ.copy()

BOT_TOKEN = str(env_vars.get('BOT_TOKEN'))
URL = str(env_vars.get("URL_VPS"))
HOST = str(env_vars.get("HOST"))
DATABASE = str(env_vars.get("DATABASE"))
USER = str(env_vars.get("USER"))
PASSWORD = str(env_vars.get("PASSWORD"))
PORT = str(env_vars.get("PORT"))
ADMIN_GROUP_ID = int(env_vars.get("ADMIN_GROUP_ID"))
