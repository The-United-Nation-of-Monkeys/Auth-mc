from kafka import KafkaProducer
from kafka import KafkaAdminClient
from kafka.admin import NewTopic

from src.config import settings
import json


# bootstrap_server = "localhost:19092"


# producer = KafkaProducer(bootstrap_servers=bootstrap_server)
# for _ in range(100):
#     producer.send('auth', b'some_message_bytes')

class Broker:
    bootstrap_server: str = settings.broker.BROKER_URL
    producer = KafkaProducer(bootstrap_servers=bootstrap_server,
                             value_serializer=lambda v: json.dumps(v).encode('utf-8') )

    @staticmethod
    def send_message(topic: str, detail: dict):
        Broker.producer.send(topic, detail)