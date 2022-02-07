import random

import mqtt.MqttClient
from settings.init_settings import mqttInit


class MqttListener(mqtt.MqttClient.MqttClient):
    def __init__(self, dataholders, name):
        mqttDatas = mqttInit(name)
        mqtt.MqttClient.MqttClient.__init__(self, mqttDatas, name)
        self.subscribe()
        self.dataholders = dataholders
        self.running = False

    def subscribe(self):
        self.client.subscribe(self.data["topic"])
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("RECIEVER -- Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    def on_message(self, client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        try:
            msgSplit = msg.payload.decode().split("/")
            if msgSplit[0] == "print":
                print(msgSplit[1])
            else:
                self.dataholders[msgSplit[1]][msgSplit[2]].push(float(msgSplit[0]))
            '''for subtopic in self.dataholders.keys():
                for name in self.dataholders[subtopic].keys():
                    self.dataholders[subtopic][name].push(float(msg.payload.decode()))'''
        except:
            print("--FAILURE-- dataholder push fail")

    def run(self):
        if not self.running:
            self.subscribe()
            self.client.loop_start()
            # print("-------MQTT LISTENER STARTED-------")
            self.running = True

    def stop(self):
        if self.running:
            self.client.loop_stop()
            # print("-------MQTT LISTENER STOPPED-------")
            self.running = False
