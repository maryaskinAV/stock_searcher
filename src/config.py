from environs import Env

env = Env()
env.read_env()

DEBUG = env.str("DEBUG")
SECRET_KEY = env.str("SECRET_KEY")
VERSION = "0.1.0"

ALGORITHM = "HS512"
ACCESS_TOKEN_EXPIRE_MINUTES = 300

ORIGINS = [
    "http://help-cube.local",
    "http://api.help-cube.ru/",
    "http://help-cube.ru",
]

try:
    from .local_config import *
except ImportError:
    pass
