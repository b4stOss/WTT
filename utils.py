from abc import ABC, abstractmethod
import aiofiles
import json, asyncio, requests, pprint, aiohttp, time, numpy as np, sys
from crypto import Crypto
from aiohttp import ClientSession
from configuration import JSONParser, Configuration
from abc import ABC
import timeit

configuration = Configuration(JSONParser, "config.json")

class Endpoint:
    base_url = "https://min-api.cryptocompare.com/data/v2"
    period = f"{base_url}/"

class API:
    pass

async def crypto_async(info):
    crypto = Crypto.create_with_info(info)
    await crypto.get_periods(configuration.periods)
    return crypto

async def get_top_100_cryptos(indicator, period):
    tasks = []

    async with ClientSession() as session:
        async with session.get("https://min-api.cryptocompare.com/data/top/mktcapfull?limit=100&tsym=USD") as resp:
            response = (await resp.json())["Data"]

            for crypto in response:
                if crypto["CoinInfo"]["Name"] not in configuration.stablecoins:
                    info = crypto["CoinInfo"]        
                    tasks.append(crypto_async(info))
                        

    parts = np.array_split(tasks, 3)
    info = []

    for part in parts:
        info += await asyncio.gather(*list(part))  

    output = ""

    if indicator == "MA":
        output += f"Hi there! \nThese coins are close to their {indicator}{period} daily, you should check these out :\n\n"
    
    elif indicator == "RSI":
        output += f"Hi there! \nThese coins are on good {indicator}14 daily levels, you should check these out :\n\n"
    
    elif indicator == "ALL":
        output += f"Hi there! \nThese coins are on good levels according to RSI14 and MA{period} daily, you should check these out :\n\n"

    restrain_crypto = [str(x) for x in info if x.is_ready(indicator)]
    output += ", ".join(restrain_crypto)

    return output