import requests
import json
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    handlers=[logging.StreamHandler()])

logger = logging.getLogger(__name__)

def getIdfmApiData(line, stop_area):
    url = "https://api-iv.iledefrance-mobilites.fr/lines/v2/line:{}/stops/stop_area:{}/realTime".format(line, stop_area)
    return requests.get(url);

def storeTimesByShortNameAndLineDirection(response):
    result = {}
    if response.status_code != 200:
        logging.error("The IDFM API is down.")
        raise Exception("API down")

    json_data = response.json()
    for data in json_data["nextDepartures"]["data"]:
        key = (data["shortName"], data["lineDirection"])
        if key in result:
            result[key].append(data["time"])
        else:
            result[key] = [data["time"]]

    return result

def main():
    response = getIdfmApiData("IDFM:C01304", "IDFM:70868")
    result = storeTimesByShortNameAndLineDirection(response)
    logger.info("(360, La Defense) - next stop in {} minutes".format(result[("360", "La Defense")][0]))
    logger.info("(360, La Defense) - following in {} minutes".format(result[("360", "La Defense")][1]))
    logger.info("(360, Hopital de Garches) - next stop in {} minutes".format(result[("360", "Hopital de Garches")][0]))
    logger.info("(360, Hopital de Garches) - following in {} minutes".format(result[("360", "Hopital de Garches")][1]))

if __name__ == "__main__":
    main()