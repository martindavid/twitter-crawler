import pika


class Messaging:

    def __init__(self, host: str, port: int, queue_name: str) -> None:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host, port=port)
        )
        self.queue_name = queue_name
        self.channel = connection.channel()
        args = {"x-max-length": 2000}
        self.channel.queue_declare(queue=queue_name, arguments=args)

    def publish(self, message: str) -> None:
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body=message
        )
