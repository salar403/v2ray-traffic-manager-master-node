from django.core.cache import caches

from user.models import User

traffic_cache = caches["traffic"]

def sync_traffic_cache():
    user_list = User.objects.all()
    for user in user_list:
        update_user_traffic(user_id=user.id, amount=user.used_traffic)

def update_user_traffic(user_id:int, amount:int):
    if not traffic_cache.get(user_id):
        traffic_cache.set(user_id, amount, None)
    else:
        traffic_cache.incr(user_id, amount)
    if amount != 0:
        user = User.objects.get(id=user_id)
        user.used_traffic += amount
        user.save()
