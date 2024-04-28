import yaml

class Model:
    name = ''

class Connect:
    type = ''
    s7 = {}
    modbus = {}
    gpio = {}

class Data:
    s7 = {}
    modbus = {}
    gpio = {}

class Driver:
    model = Model()
    connect = Connect()
    data = Data()

class Config_sys:
    driver = Driver()
    conf_dict = any
    
    def read_conf(self):
        with open('./config/config.yaml') as conf_file:
            conf_dict = yaml.safe_load(conf_file)
        self.driver.model.name = conf_dict['config']['driver']['model']['name']
        self.driver.connect.type = conf_dict['config']['driver']['connect']['type']
        self.driver.connect.s7 = conf_dict['config']['driver']['connect']['s7']
        self.driver.connect.modbus = conf_dict['config']['driver']['connect']['modbus']
        self.driver.connect.gpio = conf_dict['config']['driver']['connect']['gpio']
        self.driver.data.s7 = conf_dict['config']['driver']['data']['s7']
        self.driver.data.modbus = conf_dict['config']['driver']['data']['modbus']
        self.driver.data.gpio = conf_dict['config']['driver']['data']['gpio']
        # return conf['config']
    def __init__(self) -> None:
        self.read_conf()