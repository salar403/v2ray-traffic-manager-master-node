from django.core.cache import caches

from backend.services.config_generator import generate_config

from user.models import V2rayClient

cache_lock = caches["cache_lock"]


def assign_client(user: object):
    if V2rayClient.objects.count() < 500:
        generate_config(1000)
    client = V2rayClient.objects.filter(user__isnull=True).first()
    is_free = cache_lock.set(client.id, user.id, None)
    while not is_free:
        client = V2rayClient.objects.filter(user__isnull=True).first()
        is_free = cache_lock.set(client.id, user.id, None)
    client.user = user
    client.save()
    return client
