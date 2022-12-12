import random
import string
from uuid import uuid4
from django.core.management.base import BaseCommand
from backend.services.config_manager import sync_config

from user.models import V2rayClient


def name_generator(length=20):
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


class Command(BaseCommand):
    help = "creates new v2ray clients"

    def add_arguments(self, parser):
        parser.add_argument("count", type=str, default=500)

    def handle(self, *args, **options):
        count = options["count"]
        for _ in range(count):
            name = name_generator(25)
            uuid = str(uuid4())
            V2rayClient.objects.create(uuid=uuid, name=name)
        sync_config()
        self.stdout.write(self.style.SUCCESS(f"Successfully created {count} clients"))
