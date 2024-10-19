from time import sleep

from src.mqtt.mqttPart import *
import random
def startMqtt(text:str):
    client = connect_mqtt()
    client.loop_start()
    ##subscribe(client)
    sleep(1)
    publish(client, topic_pub, text)
    client.disconnect()