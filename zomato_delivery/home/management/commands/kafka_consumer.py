# tracker/management/commands/kafka_consumer.py
from django.core.management.base import BaseCommand
from confluent_kafka import Consumer, KafkaException
import json
from home.models import LocationUpdate
import os
from collections import defaultdict
from home.models import Post
from django.db import transaction

class Command(BaseCommand):
    help = 'Run Kafka consumer to listen for location updates'

    def handle(self, *args, **options)-> str | None:
        like_batch = defaultdict(int)
        print(like_batch)
        conf = {
            'bootstrap.servers': 'localhost:9092',
            'group.id': "location_group",
            'auto.offset.reset': 'earliest'
        }

        consumer = Consumer(conf)
        consumer.subscribe(['location_group'])
        print("KAFKA CONSUMER STARTED")
        total_messages = 0
        try:
            while True:
               
                msg = consumer.poll(timeout=1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaException._PARTITION_EOF:
                        continue
                    else:
                        print(msg.error())
                        break

                data = json.loads(msg.value().decode('utf-8'))
                LocationUpdate.objects.create( 
                    latitude=data['latitude'],
                    longitude=data['longitude'],
                    )
                print(f"Message: {data}")



        except KeyboardInterrupt:
            pass
        finally:
            consumer.close()