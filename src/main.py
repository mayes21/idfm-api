import requests
import json

url = "https://api-iv.iledefrance-mobilites.fr/lines/v2/line:IDFM:C01304/stops/stop_area:IDFM:70868/realTime"

response = requests.get(url)
result = []
if response.status_code == 200:
    json_response = json.dumps(response.json())
    json_data = json.loads(json_response)
    for item in json_data['nextDepartures']["data"]:
        print(item)
        shortName = data["shortName"]
        lineDirection = data["lineDirection"]
        time = data["time"]

        result_dict[shortName] = (lineDirection, time)
else:
    raise Exception("API down")
