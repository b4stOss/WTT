import sys, json
from abc import ABC, abstractmethod

class Configuration:
    def __init__(self, config_file, filename):
        with open(filename, "r") as filecontent:
            self.content = config_file().parse(filecontent.read())

    @property
    def stablecoins(self):
        return self.content["stablecoins"]
    
    @property
    def periods(self):
        if self.indicator == "RSI" or self.indicator == None:
            return 14

        return 14
    
    @property
    def indicator(self):
        try:
            return sys.argv[1]
        except IndexError:
            return None 

class ConfigurationParser(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def parse(self):
        pass
    
class JSONParser(ConfigurationParser):
    def __init__(self):
        super().__init__()

    def parse(self, content):
        return json.loads(content)