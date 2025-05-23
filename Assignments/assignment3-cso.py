from ast import Pass
import requests
import json

urlBegining= "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd= "/JSON-stat/2.0/en"

def getAllasFile(dataset):
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)

def getAll(dataset):
    url = urlBegining + dataset + urlEnd
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    getAllasFile("FIQ02")
 
