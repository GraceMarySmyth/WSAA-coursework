import requests
import json

urlBegining= "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd= "/JSON-stat/2.0/en"

def getAll(dataset):
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll(FIQ02)), file=fp)
 
