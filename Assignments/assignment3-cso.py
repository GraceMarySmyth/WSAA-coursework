import requests
import json

url = "https://ws.cso.ie/public/api.jsonrpc"

def getAll():
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    with open("cso.json", "wt") as fp:
        json.dump(getAll(), fp)

