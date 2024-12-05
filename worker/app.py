import os
import logging

import ollama
import pika


os.system("ollama pull qwen2.5-coder")
logging.basicConfig(level=logging.INFO)

def send():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='ollama')
    channel.basic_publish(exchange='',
                      routing_key='ollama',
                      body='Hello')
    logging.info("\n [x] Sent 'Hello!'\n")
    connection.close()


def callback(ch, method, properties, body):
    logging.info(f"\n [*] Received:\n {body}\n")
    response = ollama.chat(
        model="qwen2.5-coder",
        messages=[
            {
                "role": "user",
                "content": body
            },
        ]
    )
    logging.info(f"\n [*] Response:\n {response['message']['content']} \n")


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue="ollama")
    channel.basic_consume(
        queue="ollama",
        auto_ack=True,
        on_message_callback=callback
    )
    logging.info("\n [*] Waiting for messages. To exit press Ctrl+C \n")
    channel.start_consuming()


if __name__ == '__main__':
    try:
        send()
        send()
        main()
    except KeyboardInterrupt:
        logging.warning('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
