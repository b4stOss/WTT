import json
import asyncio
from os import pipe
import requests
import pprint
import aiohttp
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

    async def get_periods(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://min-api.cryptocompare.com/data/v2/histoday?fsym={self.name}&tsym=USD&limit={self.limit}&api_key=4a6601d2ebd6b909fdd91bbfc7f45016438a536204390ee6bbb01f30e2cee65b") as response:
                json = await response.json()
                if json["Response"] == "Success":
                    data = json["Data"]["Data"]

                    for period in data:
                        self.price_list.append(period["close"])
                else:
                    print(json["Message"])
    
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


async def crypto_async(info):
    crypto = Crypto.create_with_info(info)
    await crypto.get_periods()
    await asyncio.sleep(1)
    return crypto

async def get_top_100_cryptos():
    tasks = []
    response = requests.get("https://min-api.cryptocompare.com/data/top/mktcapfull?limit=100&tsym=USD")
    response = response.json()["Data"]

    for crypto in response:
        info = crypto["CoinInfo"]        
        tasks.append(crypto_async(info))
        
    r = await asyncio.gather(*tasks)
    #[print(x) for x in r]

asyncio.run(get_top_100_cryptos())