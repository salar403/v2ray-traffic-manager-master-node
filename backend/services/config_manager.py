import json
from django.db.models import Q

from backend.environments import V2RAY_CONFIG_PATH
from backend.services.rabbit_manager import publish
from user.models import User, V2rayClient

def load_config(path:str):
    with open(path,"r") as inp:
        data = json.load(inp)
    return data

def save_config(path:str, config:dict):
    with open(path,"w") as out:
        json.dump(config, out)

def sync_config():
    configs = V2rayClient.objects.filter(limited=False)
    v2ray_config = load_config(path=V2RAY_CONFIG_PATH)
    vless_conf = v2ray_config["inbounds"][1]["settings"]["clients"]
    vmess_conf = v2ray_config["inbounds"][2]["settings"]["clients"]
    vless_conf = []
    vmess_conf = []
    for config in configs:
        vmess_conf.append({'id': config.uuid, 'level': 0, 'email': config.name, 'alterId': 0})
        vless_conf.append({'id': config.uuid, 'level': 0, 'email': config.name})
    publish(body=v2ray_config)
