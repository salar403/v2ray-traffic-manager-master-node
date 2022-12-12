import subprocess, datetime
from django.db.models import F

from backend.services.cache_manager import update_user_traffic

from user.models import User


def get_bytes_v2ray(user):
    usage= 0
    data1=None
    data2=None
    side1="downlink"
    side2="uplink"
    try:
        data1=subprocess.check_output('/root/v2/v2ctl api --server=172.17.0.2:54321 StatsService.GetStats ' + "'" + 'name: "user>>>' + user + '>>>traffic>>>' + side1 + '" reset: true' + "'" + '  2>/dev/null  | grep value | cut -d: -f2 | tr -d " "', shell = True)
        #print(data1)
    except :
        pass
    try:
        data2 = subprocess.check_output('/root/v2/v2ctl api --server=172.17.0.2:54321 StatsService.GetStats ' + "'" + 'name: "user>>>' + user + '>>>traffic>>>' + side2 + '" reset:true ' + "'" + ' 2>/dev/null | grep value | cut -d: -f2 | tr -d " "', shell = True)
    except:
        pass
    try:
        if data1 != None:
            if data1.decode("utf-8") != '':
                usage += int(data1.decode("utf-8"))
        if data2 != None:
            if data2.decode("utf-8") != '':
                usage += int(data2.decode("utf-8"))
    except:
        pass
        #print(data1,data2)
    return usage

def update_usage():
    users = User.objects.all()
    for user in users:
        usage=int(int(get_bytes_v2ray(user.config.name))/(1024*1024))
        if usage > 0:
            update_user_traffic(user_id=user.id, amount=usage)

def check_usage():
    users = User.objects.filter(used_traffic__gt=F("traffic_limit"), config__limited=False)
    existance = users.exists()
    for user in users:
        user.config.limited = True
        user.save()
        print(user.telegram_id,str(datetime.datetime.today()))
    return existance
