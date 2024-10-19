from time import sleep

import mqttPart
import random
def startMqtt(text:str):
    client = mqttPart.connect_mqtt()
    client.loop_start()
    ##mqttPart.subscribe(client)
    sleep(1)
    mqttPart.publish(client, mqttPart.topic_pub, text)
    client.disconnect()