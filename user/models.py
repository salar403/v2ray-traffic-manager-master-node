from django.db import models


class User(models.Model):
    telegram_id = models.BigIntegerField(null=False, unique=True)
    traffic_limit = models.BigIntegerField(null=False, default=7 * 1024)
    used_traffic = models.BigIntegerField(null=False, default=0)

class V2rayClient(models.Model):
    uuid = models.CharField(null=False, max_length=50)
    name = models.CharField(max_length=1000, null=False)
    user = models.OneToOneField(
        to=User,
        on_delete=models.SET_NULL,
        related_name="config",
        null=True,
    )
    limited = models.BooleanField(default=False)
