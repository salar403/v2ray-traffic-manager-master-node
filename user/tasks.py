from celery import shared_task

from backend.services.rabbit_manager import publish
from user.models import User, V2rayClient

from user.serializers import ClientSerializer, UserSerializer


@shared_task(queue="main")
def broadcast_config():
    queryset = V2rayClient.objects.filter(limited=False)
    ret = {
        "drak": ClientSerializer(queryset.filter(cpg=V2rayClient.DRAK), many=True).data
    }
    ret["cloudflare"] = ClientSerializer(
        queryset.filter(vpg=V2rayClient.CLOUDFLATE), many=True
    ).data
    ret["users"] = UserSerializer(
        User.objects.filter(config__limited=False), many=True
    ).data
    publish(body=ret)
