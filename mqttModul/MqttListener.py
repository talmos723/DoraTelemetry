from communication import ComSystem
from communication.ComIn import ComIn
from mqttModul.MqttBase import MqttBase
from settings.init_settings import mqttInit


class MqttListener(MqttBase, ComIn):

    def __init__(self, name):
        mqttDatas = mqttInit(name)
        MqttBase.__init__(self, mqttDatas, name)
        self.subscribe()

    def subscribe(self):
        MqttBase.subscribe(self)
        self.client.on_message = self.mqttMessage

    def mqttMessage(self, client, userdata, msg):
        if int(msg.payload[0:1].decode()) == 0:     # TODO: outsource literal
            self.logger.debug(f"Own message `{msg.payload[1:]}` from `{msg.topic}` topic dropped")
            return
        self.logger.debug(f"Received `{msg.payload[1:]}` from `{msg.topic}` topic")
        self.onMessage(msg.payload[1:].decode(), msg.topic)

    def onMessage(self, message, topic):
        try:
            msgSplit = message.split("/")
            if msgSplit[0] == "print":
                print(msgSplit[1])
            else:
                ComSystem.ComSystem.getInstance().Dataholders[msgSplit[1]][msgSplit[2]].push(float(msgSplit[0]))
            '''for subtopic in self.dataholders.keys():
                for name in self.dataholders[subtopic].keys():
                    self.dataholders[subtopic][name].push(float(msg.payload.decode()))'''
        except:
            self.logger.warning("--FAILURE-- dataholder push fail")

    def run(self):
        if not self.running:
            MqttBase.run(self)
            self.subscribe()
            self.client.loop_start()
            self.logger.info("-------MQTT LISTENER STARTED-------")

    def stop(self):
        if self.running:
            MqttBase.stop(self)
            self.client.loop_stop()
            self.logger.info("-------MQTT LISTENER STOPPED-------")
