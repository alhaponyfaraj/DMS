#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='192.168.0.121', credentials=credentials))
channel = connection.channel()
# connect to the middleware

def send(username, message):

    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    message = ' '.join(sys.argv[1:]) or "info:" + message + "!"
    channel.basic_publish(exchange='logs', routing_key='', body=message)
    print(" Sent " + message + " !" + "from "+ username)
