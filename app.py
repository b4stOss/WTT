import json
import requests
import pprint

from requests.models import Response
from requests.sessions import PreparedRequest

LIMIT = 50
pp = pprint.PrettyPrinter(indent=4)

class Endpoint:
    base_url = "https://min-api.cryptocompare.com/data/v2"
    period = f"{base_url}/"


class API:
    pass

class Crypto: 
    def __init__ (self, id, name, limit=LIMIT):
        self.id = id
        self.price_list = []
        self.name = name 
        self.limit = limit

        self.get_periods()

    def get_periods(self):
        response = requests.get(f"https://min-api.cryptocompare.com/data/v2/histoday?fsym={self.name}&tsym=USD&limit={self.limit}").json()

        if response["Response"] == "Success":
            data = response["Data"]["Data"]

            for period in data:
                self.price_list.append(period["close"])
    
    @property
    def mooving_average(self):
        if len(self.price_list) != 0:
            return sum(self.price_list) / len(self.price_list)
        
        return "NaN"
        

    @staticmethod
    def create_with_info(info):
        return Crypto(info["Id"], info["Name"])

    def __str__(self):
        return f"{self.id} - {self.name} - {self.mooving_average}"

def get_top_100_cryptos():
    response = requests.get("https://min-api.cryptocompare.com/data/top/mktcapfull?limit=100&tsym=USD")
    response = response.json()["Data"]

    for crypto in response:
        info = crypto["CoinInfo"]
        yield Crypto.create_with_info(info)


for crypto in get_top_100_cryptos():
    print(crypto)       