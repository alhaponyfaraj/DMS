#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='192.168.0.121', credentials=credentials))
channel = connection.channel()
# connect to the middleware