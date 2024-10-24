import json
import random
class MqttConfig:
    def __init__(self,broker,port,topic_pub,topic_sub,client_id):
        self.broker = broker
        self.port = port
        self.topic_pub = topic_pub
        self.topic_sub = topic_sub
        self.client_id = client_id

    def readSettings(self):
        with open('../../config.json', 'r') as json_file:
            data = json.load(json_file)
            self.broker=(data['broker'])
            self.port=(data['port'])
            self.topic_pub=(data['topic_pub'])
            self.topic_sub=(data['topic_sub'])
            self.client_id=f'python-mqtt-{random.randint(0, 1000)}'
            print("broker:",self.broker)
            print("port:",self.port)
            print("topic_pub:",self.topic_pub)
            print("topic_sub:",self.topic_sub)
            print("client_id:",self.client_id)


if __name__ == '__main__':
    MqttConfig= MqttConfig('broker','port','topic_pub','topic_sub','client_id')
    MqttConfig.readSettings()