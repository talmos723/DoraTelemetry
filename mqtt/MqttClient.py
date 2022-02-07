import abc

import paho.mqtt.client as mqtt
from communication.ComModul import ComModul


class MqttClient(ComModul):
    def __init__(self, mqttDatas:dict, name, shouldSubscirbe=True):
        self.name = name
        self.data = mqttDatas

        self.client = self.connect()
        if shouldSubscirbe:
            self.subscribe()

    def connect(self):
        client = mqtt.Client(self.name)
        client.username_pw_set(self.data["username"], self.data["password"])
        client.on_connect = self.on_connect
        client.connect(self.data["broker"], self.data["port"])
        return client

    def subscribe(self):
        self.client.subscribe(self.data["topic"])

    def getClient(self):
        return self.client

    @abc.abstractmethod
    def on_connect(self, client, userdata, flags, rc):
        pass

