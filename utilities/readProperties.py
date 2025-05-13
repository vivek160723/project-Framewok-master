import yaml
import os

class ReadConfig:
    def __init__(self):

        base_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_path, "../config.yaml")
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)['common_info']

    def getApplicationURL(self):
        return self.config['base_url']

    def getUsername(self):
        return self.config['username']

    def getPassword(self):
        return self.config['password']