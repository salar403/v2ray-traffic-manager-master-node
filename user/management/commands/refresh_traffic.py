import os
from django.core.management.base import BaseCommand
from backend.services.config_manager import sync_config
from backend.services.traffic_manager import update_usage, check_usage

class Command(BaseCommand):
    help = "checks users vpn usages"

    def handle(self, *args, **options):
        update_usage()
        new_limitations = check_usage()
        if new_limitations:
            sync_config()
            os.system("docker restart v2ray")
            self.stdout.write(self.style.SUCCESS("new users limited"))
        self.stdout.write(self.style.SUCCESS("check_done, no users limited"))
