import os


def bot_owner() -> int:
    return 296981333811396608


def bot_token():
    return os.environ['BOT_TOKEN']


def bot_prefix():
    return os.environ['BOT_PREFIX']


def db_host():
    return os.environ['DB_HOST']


def db_database():
    return os.environ['DB_DATABASE']


def db_user():
    return os.environ['DB_USER']


def db_password():
    return os.environ['DB_PASSWORD']


def lavalink_host():
    return os.environ['LAVALINK_HOST']


def lavalink_port():
    return os.environ['LAVALINK_PORT']


def lavalink_password():
    return os.environ['LAVALINK_PASSWORD']


def osu_api_key():
    return os.environ['OSU_API_KEY']