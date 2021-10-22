import json, asyncio, requests, pprint, aiohttp, time, numpy as np, sys
from crypto import Crypto
from requests.models import Response
from requests.sessions import PreparedRequest

pp = pprint.PrettyPrinter(indent=4)
STABLECOINS = ["USDT", "USDC", "DAI", "UST", "BUSD"]


INDICATOR = sys.argv[1]
if(INDICATOR == "ALL"):
    PERIODS = 50
else:
    PERIODS = int(sys.argv[2])

class Endpoint:
    base_url = "https://min-api.cryptocompare.com/data/v2"
    period = f"{base_url}/"

class API:
    pass

async def crypto_async(info):
    crypto = Crypto.create_with_info(info)
    await crypto.get_periods(PERIODS)
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
        if INDICATOR == "MA":
            f.writelines(f"Hi there! \nThese coins are close to their {INDICATOR}{PERIODS} daily, you should check these out :\n\n")
        if INDICATOR == "RSI":
            f.writelines(f"Hi there! \nThese coins are on good {INDICATOR}{PERIODS} daily levels, you should check these out :\n\n")
        if INDICATOR == "ALL":
            f.writelines(f"Hi there! \nThese coins are on good levels according to RSI14 and MA50 daily, you should check these out :\n\n")

        for x in info:
            if x.is_ready(INDICATOR):  
                f.writelines(str(x) + ", ")
    
#asyncio.run(get_top_100_cryptos())
asyncio.get_event_loop().run_until_complete(get_top_100_cryptos())