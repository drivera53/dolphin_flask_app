#!/usr/bin/env python3
import json, pika

def create_new_username_MQ(username):
    try:
        '''
        Establish a connection to a RabbitMQ server.
        localhost means we are connecting to the local
        machine. However we can provide a IP address to
        a different machine.
        '''
        conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        channel = conn.channel()

        '''
        We create a queue just for new_ig_username
        '''
        channel.queue_declare(queue='new_ig_username')

        channel.basic_publish(exchange="", routing_key='new_ig_username',
                            body=json.dumps({
                                "new_username": username
                            }))
    except:
        print("An exception occurred while adding new message to MQ: new_ig_username")