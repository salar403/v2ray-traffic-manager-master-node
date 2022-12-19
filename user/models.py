from django.db import models


class User(models.Model):
    telegram_id = models.BigIntegerField(null=False, unique=True)
    traffic_limit = models.BigIntegerField(null=False, default=7 * 1024)
    used_traffic = models.BigIntegerField(null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    last_recharge = models.DateTimeField(null=True)


class V2rayClient(models.Model):
    DRAK = 1
    CLOUDFLARE = 2
    CDNS = [
        (DRAK, "DRAK"),
        (DRAK, "CLOUDFLARE"),
    ]
    uuid = models.CharField(null=False, max_length=50)
    name = models.CharField(max_length=1000, null=False)
    user = models.OneToOneField(
        to=User,
        on_delete=models.SET_NULL,
        related_name="config",
        null=True,
    )
    cdn = models.integer(choices=CDNS, null=False)
    limited = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
