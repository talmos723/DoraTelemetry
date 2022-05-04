import logging

import serial
from serial.serialutil import SerialException

from communication.ComBase import ComBase


class SerialBase(ComBase):
    def __init__(self, port):
        self.logger = logging.getLogger('robotlog')

        #ports = serialModul.tools.list_ports.comports()
        self.serialInst = serial.Serial()
        self.serialInst.baudrate = 115200
        self.serialInst.port(port)

        '''if not re.match("^COM[0-9]+$", port):
            raise TypeError("Port's name must be in the form of COM[number]")'''


    def connect(self):
        try:
            self.serialInst.open()
            self.logger.info("Connected to UART serialModul port!")
        except SerialException as e:
            self.logger.warning(f"Failed to connect to UART serialModul port, return code {e}")

    def run(self):
        pass

    def stop(self):
        pass

