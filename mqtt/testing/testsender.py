import random
import time
from mqtt.MqttClient import MqttClient


class MqttSender(MqttClient):
    def __init__(self, mqttDatas: dict, seconds: int, name):
        MqttClient.__init__(self, mqttDatas, name, False)
        self.seconds = seconds
        self.running = True

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("SENDER -- Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    def run(self):
        num = 250
        while self.running:
            self.publish(f"{num}/esp8266/resultCM")
            time.sleep(self.seconds)
            num -= 5
            if num < 0:
                num = 250

    def stop(self):
        self.running = False

    def publish(self, msg):
        result = self.client.publish(self.data["topic"], msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{self.data['topic']}`")
        else:
            print(f"Failed to send message to topic {self.data['topic']}")

def testrun(recipe:dict, seconds:int, name):
    MqttSender(recipe, seconds, name).run()
