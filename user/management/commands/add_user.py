import base64
from django.core.management.base import BaseCommand

from user.models import User

from backend.services.telegram import send_message
from backend.environments import CLOUDFLARE_IP, ARVAN_DOMAIN
# class Command(BaseCommand):
#     help = "creates new v2ray clients"

#     def add_arguments(self, parser):
#         parser.add_argument("count", type=str, default=500)

#     def handle(self, *args, **options):
#         count = options["count"]
#         for _ in range(count):
#             name = name_generator(25)
#             uuid = str(uuid4())
#             V2rayClient.objects.create(uuid=uuid, name=name)
#         self.stdout.write(self.style.SUCCESS(f"Successfully created {count} clients"))



def gen_user(message):
    tel_id = message.from_user.id
    user = User.objects.filter(telegram_id=tel_id)
    if user.exists():
        if not user.config.limited:
            message = f"trafic masraf shode: {user.used_traffic} MB"
            send_message(tel_id, message)
        else:
            send_message(tel_id, "حجمتون تمون شده. تا آخر هفته برای شارژ مجدد صبر کنید")        
        txt="ارسال پیام به من با /pm مثال: \n /pm سلام\n"
        message = f"{txt}حمایت مالی: /donate\nآموزش و برنامه ها: نیازمند منبع - v2rayng نسخه ی جدید\nمقدار حجم مصرفی رو با زدن  /tr ببینید\nمقدار حجم هفتگی کانفیگ ها ۷ گیگ هست (فعلا)\nسرور ها فیلتر شده؟ /help"
        send_message(tel_id, txt+ f'')
        name=user.config.name
        uid=user.config.uuid
        conf1 = make_config1(uid, name)
        conf2 = make_config2(uid, name)
        conf3 = make_config_arvan(uid, name, ARVAN_DOMAIN)
        send_message(tel_id, f'`{conf1}`\nبرای استفاده از این کانفیگ بهتره توی v2rayng آپدیت شده ادیت رو بزنید و اون آخر utls رو روی کروم بزارید')
        send_message(tel_id, f'{conf2}')
        send_message(tel_id, f'اینم vmess روی آروان \#jadi ❤️ \n`{conf3}`\n️')
        return 0
    names=[]
    for i in d:
        names.append(d[i]["name"])
    for i in v2["inbounds"][1]["settings"]["clients"]:
        if i["email"] not in names:
            data = {"name": i["email"], "trafic": 7, "uuid": i["id"]}
            d.update({str(tel_id): data})
            save_db(d)
            tr.update({str(tel_id): 0})
            #print(tr)
            save_tr(tr)
            txt="ارسال پیام به من با /pm مثال: \n /pm سلام\n"
            conf1 = make_config1(i["id"], i["email"])
            conf2 = make_config2(i["id"], i["email"])
            conf3 = make_config_arvan(i["id"], i["email"], arvan)
            send_message(tel_id, txt+ f'حمایت مالی: /donate\nآموزش و برنامه ها: نیازمند منبع\nمقدار حجم مصرفی رو با زدن  /tr ببینید\nمقدار حجم هفتگی ۷ گیگ هست (فعلا)\nسرور ها فیلتر شده؟ /help')
            send_message(tel_id, f'`{conf1}`\nبرای استفاده از این کانفیگ توی v2rayng آپدیت شده ادیت رو بزنید و اون آخر utls رو روی کروم بزارید'2)
            send_message(tel_id, f'{conf2}')
            send_message(tel_id, f'اینم vmess روی آروان \#jadi ❤️ \n`{conf3}`\n️')
            return 0
    else:
        bot.send_message(tel_id, "تمون شده . لطفا چند ساعتی دیگر تلاش کنید . یادتون نره هاا")
        bot.send_message(5607291327, "تمون شده")

        save_wait(str(message.from_user.id))
    return 0

def make_config1(uid:str, name:str):
    return f"vless://{uid}@{CLOUDFLARE_IP}:443?sni=betterthanunix.ml&host=gheychi.betterthanunix.ml&type=ws&security=tls&path=%2Fmetrix&encryption=none#{name}_%40sansorchi_bezan_gheychi_bot"


def make_config2(uid:str, name:str):
    return "vmess://"+base64.b64encode(b'{"add":"'+CLOUDFLARE_IP.encode()+b'","aid":"0","host":"gheychi.betterthanunix.ml","id":"'+uid.encode()+b'","net":"ws","path":"/ws","port":"80","ps":"'+name.encode()+b"-@sansorchi_bezan_gheychi_bot"+b'","tls":"","scy":"auto","type":"none","v":"2"}').decode()


def make_config_sub1(uid, name,sub):
    sni = ".".join(sub.split(".")[-2:])
    #print(sni)
    return f"vless://{uid}@{sub}:443?sni={sni}&type=ws&security=tls&path=%2Fmetrix&encryption=none#{name}_%40sansorchi_bezan_gheychi_bot"


def make_config_arvan(uid, name, sub=arvan):
    return "vmess://"+base64.b64encode(b'{"add":"snappfood.ir","aid":"0","host":"'+sub.encode()+b'","id":"'+uid.encode()+b'","net":"ws","path":"/ws","port":"80","ps":"@sansorchi_bezan_gheychi_bot-'+name.encode()+b'","tls":"","scy":"auto","type":"none","v":"2"}').decode()


def make_config_sub2(uid, name, sub):
    return "vmess://"+base64.b64encode(b'{"add":"'+sub.encode()+b'","aid":"0","host":"","id":"'+uid.encode()+b'","net":"ws","path":"/ws","port":"80","ps":"_%40sansorchi_bezan_gheychi_bot_'+name.encode()+b'_your_sub","tls":"","scy":"auto","type":"none","v":"2"}').decode()