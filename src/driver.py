from read_conf import Config_sys 
from pyModbusTCP.client import ModbusClient
import snap7
# import lgpio

class Gpio_Con:
    num = []
    type_ = []

class S7_Con:
    ip = []
    port = []
    rack = []
    slot =[]

class ModbusTCP_Con:
    ip = []
    port = []

class S7_data:
    data = []
    def getData():
        pass

class Modbus_data:
    data = []
    def getData():
        pass

class Gpio_data:
    data = []
    gpio_num = []
    gpio_type = []

    def getData():
        pass