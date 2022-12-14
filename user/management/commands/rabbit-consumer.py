import json, pika
from django.core.management.base import BaseCommand
from backend.environments import (
    RABBITMQ_HOST,
    RABBITMQ_PASSWORD,
    RABBITMQ_PORT,
    RABBITMQ_USERNAME,
    RABBITMQ_VIRTUAL_HOST,
    RABBITMQ_QUEUE,
)


class Command(BaseCommand):
    help = "checks users vpn usages"

    def handle(self, *args, **options):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=RABBITMQ_HOST,
                port=int(RABBITMQ_PORT),
                virtual_host=RABBITMQ_VIRTUAL_HOST,
                credentials=pika.PlainCredentials(
                    username=RABBITMQ_USERNAME,
                    password=RABBITMQ_PASSWORD,
                ),
                heartbeat=None,
                blocked_connection_timeout=300,
            )
        )
        channel = connection.channel()
        channel.queue_declare(
            queue=RABBITMQ_QUEUE,
            durable=True,
            passive=True,
            arguments={"x-queue-type":"stream"},
        )
        channel.basic_qos(prefetch_count=1000)
        channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=self.callback)
        print("Started Consuming...")
        channel.start_consuming()

    def callback(self, ch, method, properties, body):
        print("Received new message")
        data = json.loads(body)
        print(data)
