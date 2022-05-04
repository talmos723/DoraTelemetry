import time

from communication.ComOut import ComOut
from mqttModul.MqttBase import MqttBase
from settings.init_settings import mqttInit


class MqttSender(MqttBase, ComOut):
    def __init__(self, name):
        mqttDatas = mqttInit(name)
        MqttBase.__init__(self, mqttDatas, name, False)

    def run(self):
        if not self.running:
            MqttBase.run(self)
            self.logger.info("-------MQTT SENDER STARTED-------")


    def stop(self):
        if self.running:
            MqttBase.stop(self)
            self.logger.info("-------MQTT SENDER STOPPED-------")

    def send(self, message):
        result = self.client.publish(self.data["topic"], message)
        status = result[0]
        if status == 0:
            self.logger.debug(f"Send `{message}` to topic `{self.data['topic']}`")
        else:
            self.logger.debug(f"Failed to send message to topic {self.data['topic']}")


def testrun():
    sender = MqttSender("mqtt_connect_sender")
    sender.run()
    num = 100
    while True:
        sender.send(f"{0x00}{num}/esp8266/Humidity")
        num -= 5
        if num < 50:
            num = 100
        time.sleep(2)


def testrun2():
    sender = MqttSender("mqtt_connect_sender2")
    sender.run()
    num = 50
    while True:
        sender.send(f"{0x01}{num}/esp8266/Humidity")
        num -= 5
        if num < 0:
            num = 50
        time.sleep(2)
