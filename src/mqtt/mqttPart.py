import datetime
import json
import random
import time
from src.mqtt import database
from paho.mqtt import client as mqtt_client

broker = '192.168.1.114'
port = 1883
topic_pub = "testtopic/1"
topic_sub = "testtopic/1"
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def connect_mqtt(broker, port, client_id):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, client_id)
    client.on_connect = on_connect

    client.connect(broker, port)
    return client
#建立Mqtt连接

def publish(client, topic_pub, msg):
    msg_count = 0
    
    # time.sleep(1)
        # # msg = {'number': msg_count, 'date': datetime.datetime.now().timestamp(), 'temp': random.randrange(20, 25),
        # #        'humi': random.randrange(45, 50), 'illu': random.randrange(3000, 3100)}
    res = client.publish(topic_pub, json.dumps(msg))
    status = res[0]
    if status == 0:
        print(f"Sent '{msg}' to topic {'topic'}")
    else:
        print(f"Failed to send {msg} to topic {'topic'}")
    msg_count += 1
#进行消息的发送

def subscribe(client: mqtt_client,topic_sub):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        data = json.loads(msg.payload.decode())#解析Json
        database.writedata(data['temp'], data['humi'], data['illu'], data['date'])
        time_str = datetime.datetime.fromtimestamp(data['date'], datetime.UTC)
        print(time_str)
#进行消息的订阅

    client.subscribe(topic_sub)
    client.on_message = on_message


