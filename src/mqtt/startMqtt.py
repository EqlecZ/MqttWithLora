from time import sleep

from src.mqtt import MqttConfig
from src.mqtt.mqttPart import *
import random


def startMqtt(text: str):
    mqttsettings = MqttConfig.MqttConfig('broker', 'port', 'topic_pub', 'topic_sub', 'client_id')
    mqttsettings.readSettings()
    client = connect_mqtt(mqttsettings.broker, mqttsettings.port, mqttsettings.client_id)
    client.loop_start()
    ##subscribe(client)
    sleep(1)
    publish(client, mqttsettings.topic_pub, text)
    client.disconnect()
