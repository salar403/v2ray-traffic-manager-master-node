from os import getenv

REDIS_DEFAULT = "0"
REDIS_TRAFFIC = "1"
REDIS_T = "2"

REDIS_HOST = getenv("REDIS_HOST","localhost")
REDIS_PORT = getenv("REDIS_HOST",6379)

POSTGRES_HOST = getenv("REDIS_HOST","localhost")
POSTGRES_HOST = getenv("REDIS_HOST",5432)
POSTGRES_DB = getenv("POSTGRES_DB","postgres")
POSTGRES_USERNAME = getenv("POSTGRES_USERNAME","postgres")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD","postgres")

V2RAY_CONFIG_PATH = getenv("V2RAY_CONFIG_PATH","/root/v2/config-main.json")
CLOUDFLARE_IP = getenv("CLOUDFLARE_IP","104.18.125.0")
ARVAN_DOMAIN = getenv("CLOUDFLARE_DOMAIN","wearejadi.vpnmaster.uno")
TELEGRAM_BOT_TOKEN = getenv("TELEGRAM_BOT_TOKEN","5705397533:AAGnWZCHdqNFv_nhgNCYyVMXBLaMNx6S")
