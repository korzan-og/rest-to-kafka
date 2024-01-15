#!/usr/bin/env python

import sys
from random import choice
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Producer
import logging
import configparser

configParser = configparser.RawConfigParser()   
configFilePath = r'config.ini'
configParser.read(configFilePath)

username=configParser.get('confluent', 'sasl.username')
password=configParser.get('confluent', 'sasl.password')
mechanism=configParser.get('confluent', 'sasl.mechanisms')
broker=configParser.get('confluent', 'bootstrap.servers')
protocol=configParser.get('confluent', 'security.protocol')
clientId=configParser.get('confluent', 'client.id')
config={'bootstrap.servers': broker,'security.protocol':protocol,'sasl.mechanisms':mechanism,'client.id':clientId,'sasl.username':username,'sasl.password':password} # For cloud

logLevel=configParser.get('logging', 'logging.level')
logging.basicConfig()
logging.getLogger().setLevel(logLevel)

def kafkaProducer(topic,key,message):
    producer = Producer(config)
    def delivery_callback(err, msg):
        if err:
            logging.error('ERROR: Message failed delivery failed for {}: {}'.format(topic, err))
        else:
            logging.info("Produced event to topic {topic}: key = {key} value = {value}".format(
                topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
    producer.produce(topic, message, key, callback=delivery_callback)
    producer.poll(10000)


