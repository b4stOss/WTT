import json
import requests


def getTop100 () :
    top100 = {}
    response = requests.get("https://min-api.cryptocompare.com/data/top/mktcapfull?limit=100&tsym=USD")
    response = response.json()["Data"]
    for i in range(len(response)): 
        top100[i] = {
            "id": response[i]["CoinInfo"]["Id"],
            "name": response[i]["CoinInfo"]["Name"]
        }
    
    #print(json.dumps(top100, indent = 4))
    return top100
    
def main(): 
    top100 = getTop100()
    print(json.dumps(top100, indent=4))


main()