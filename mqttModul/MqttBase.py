import logging

import paho.mqtt.client as mqtt
from communication.ComBase import ComBase


class MqttBase(ComBase):
    def __init__(self, mqttDatas:dict, name, shouldSubscirbe=True):

        self.logger = logging.getLogger('robotlog')

        self.name = name
        self.data = mqttDatas

        self.client = self.connect()
        if shouldSubscirbe:
            self.subscribe()

        self.running = False

    def connect(self):
        client = mqtt.Client(self.name)
        client.username_pw_set(self.data["username"], self.data["password"])
        client.on_connect = self.on_connect
        client.connect(self.data["broker"], self.data["port"])
        return client

    def subscribe(self):
        self.client.subscribe(self.data["topic"])

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self.logger.info("Connected to MQTT Broker!")
        else:
            self.logger.warning("Failed to connect to MQTT Broker, return code %d\n", rc)

    def run(self):
        if not self.running:
            self.logger.info("-------MQTT BASE STARTED-------")
            self.running = True

    def stop(self):
        if self.running:
            self.logger.info("-------MQTT BASE STOPPED-------")
            self.running = False