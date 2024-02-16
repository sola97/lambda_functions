import os

from starlette.config import Config

current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_dir, '..', '.env')

config = Config(env_path)

SERVER_URL = config("SERVER_URL", cast=str)
app_configs = {
    "server_url": SERVER_URL,
}
