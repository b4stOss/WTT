import json, asyncio, requests, pprint, aiohttp, time, numpy as np
from crypto import Crypto
from requests.models import Response
from requests.sessions import PreparedRequest

LIMIT = 50
STABLECOINS = ["USDT", "USDC", "DAI", "UST", "BUSD"]
pp = pprint.PrettyPrinter(indent=4)

class Endpoint:
    base_url = "https://min-api.cryptocompare.com/data/v2"
    period = f"{base_url}/"

class API:
    pass

async def crypto_async(info):
    crypto = Crypto.create_with_info(info)
    await crypto.get_periods()
    return crypto

async def get_top_100_cryptos():
    tasks = []
    response = requests.get("https://min-api.cryptocompare.com/data/top/mktcapfull?limit=100&tsym=USD")
    response = response.json()["Data"]

    for crypto in response:
        if crypto["CoinInfo"]["Name"] not in STABLECOINS:
            info = crypto["CoinInfo"]        
            tasks.append(crypto_async(info))
    
    parts = np.array_split(tasks, 3)

    info = []

    for part in parts:
        info += await asyncio.gather(*list(part))  
    
    with open("result.txt", "w") as f:
        f.writelines(f"Hi there! \nThese coins are close to their ma{LIMIT} daily, you should check these out :\n\n")
        for x in info:
            if x.is_ready:  
                f.writelines(str(x) + ", ")
    
#asyncio.run(get_top_100_cryptos())
asyncio.get_event_loop().run_until_complete(get_top_100_cryptos())