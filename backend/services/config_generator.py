import random, uuid
from user.models import V2rayClient


names = []
with open("names.txt", "r") as f:
    for i in f:
        names.append(i.strip())


def get_random_name():
    return random.choice(names) + str(random.randint(1000, 9999))


def gen_uuid():
    return str(uuid.uuid4())


def generate_config(quantity:int):
    for _ in range(quantity):
        name = get_random_name()
        while V2rayClient.objects.filter(name=name).exists():
            name = get_random_name()
        uid = gen_uuid()
        while V2rayClient.objects.filter(uuid=uid).exists():
            uid = gen_uuid()
        V2rayClient.objects.create(name=name, uuid=uid)
