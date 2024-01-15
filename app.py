import sys
from flask import Flask, jsonify, request
# import json
import logging
import configparser
from kafkaProducer import kafkaProducer
# import requests


configParser = configparser.RawConfigParser()   
configFilePath = r'config.ini'
configParser.read(configFilePath)

logLevel=configParser.get('logging', 'logging.level')
logging.basicConfig()
logging.getLogger().setLevel(logLevel)

topic=configParser.get('confluent', 'user.topic')

app = Flask(__name__)

success = {'status':'success'}

@app.route('/health/ping', methods=['GET'])
def healthCheck():
    logging.info("getHealthCheck exit")
    healthResponse = success
    logging.info("getHealthCheck exit")
    return jsonify(healthResponse), 200

@app.route('/post', methods=['POST'])
def managePosts():
    logging.info("post enter")
    logging.info("Requestor IP : " + request.remote_addr)
    # logging.info(str(request.headers))
    key = request.get_json()['key']
    logging.info("KEY :  " + key)
    kafkaProducer(topic,str(key),str(request.get_json()))
    response=success
    logging.info(response)
    logging.info("post exit")
    return jsonify(response), 200
    


if __name__ == "__main__":
    # app.run(ssl_context='adhoc')
    app.run(ssl_context='adhoc')
    