import os
from datetime import datetime
import logging
from pytz import timezone, utc

import requests
import csv
import json

tz_Baku = timezone("Asia/Baku")


def customTime(*args):
    utc_dt = utc.localize(datetime.utcnow())
    converted = utc_dt.astimezone(tz_Baku)
    return converted.timetuple()


logging.Formatter.converter = customTime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.FileHandler("../public/data/data.log", encoding="utf8")
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s", datefmt="%d-%m-%Y %H:%M:%S"
)
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


if __name__ == "__main__":
    try:
        API_KEY = os.environ["API_KEY"]
    except KeyError:
        raise

    url = "https://api.openweathermap.org/data/2.5/weather?q=baku&units=metric&appid=" + API_KEY

    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        logger.info(f"Weather in Baku: {temperature}°C - {description}")

        with open("../public/data/data.csv", mode="a") as csv_file:
            fieldnames = ["date_time", "temperature", "description"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writerow(
                {
                    "date_time": datetime.now(tz_Baku).strftime("%d-%m-%Y %H:%M:%S"),
                    "temperature": temperature,
                    "description": description,
                }
            )

        with open("../public/data/data.json", "r") as f:
            json_data = json.load(f)

        json_data.append(
            {
                "date_time": datetime.now(tz_Baku).strftime("%d-%m-%Y %H:%M:%S"),
                "temperature": temperature,
                "description": description,
            }
        )

        with open("../public/data/data.json", "w") as f:
            json.dump(json_data, f, indent=4, separators=(",", ": "))
