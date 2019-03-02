from typing import List
from app.logger import LOG as log
import pika
import json


class Messaging:

    def __init__(self, queue_name: str, host: str = 'localhost', port: int = 5672, username: str = 'guest', password: str = 'guest') -> None:
        credentials = pika.PlainCredentials(username, password)
        con = pika.BlockingConnection(
            pika.ConnectionParameters(host=host, port=port, credentials=credentials)
        )
        self.channel = con.channel()

        # set max queue size
        args = {"x-max-length": 2000}
        self.queue_name = queue_name
        self.channel.queue_declare(queue=queue_name, arguments=args)

    def publish(self, message: str) -> None:
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body=json.dumps(message)
        )

    def get(self, size: int) -> List:
        tweets = []
        count = 0
        for method_frame, properties, body in self.channel.consume(self.queue_name):
            tweets.append(json.loads(body))

            # Acknowledge the message
            self.channel.basic_ack(method_frame.delivery_tag)

            count += 1

            if count == size:
                break

        requeued_messages = self.channel.cancel()
        log.info(f'Requeued {requeued_messages} messages')

        return tweets
