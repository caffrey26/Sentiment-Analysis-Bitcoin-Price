# calls Coindesk API to get the bitcoin price index in USD
# Powered by CoinDesk https://www.coindesk.com/price/
# code inspired from: https://stackoverflow.com/questions/17301938/making-a-request-to-a-restful-api-using-python

import requests
import json

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
myResponse = requests.get(url)
if(myResponse.ok):
    jData = json.loads(myResponse.content)
    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    print jData["time"]["updated"]
    print jData["bpi"]["USD"]["rate_float"]
else:
  # If response code is not ok (200), print the resulting http error code with description
    myResponse.raise_for_status()