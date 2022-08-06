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
logger_file_handler = logging.FileHandler("../data/data.log", encoding="utf8")
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s", datefmt="%d-%m-%Y %H:%M:%S"
)
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


if __name__ == "__main__":
    r = requests.get("https://weather.talkpython.fm/api/weather?city=baku&country=AZ")

    if r.status_code == 200:
        data = r.json()
        temperature = data["forecast"]["temp"]
        description = data["weather"]["description"]
        logger.info(f"Weather in Baku: {temperature}°C - {description}")

        with open("../data/data.csv", mode="a") as csv_file:
            fieldnames = ["date_time", "temperature", "description"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writerow(
                {
                    "date_time": datetime.now(tz_Baku).strftime("%d-%m-%Y %H:%M:%S"),
                    "temperature": temperature,
                    "description": description,
                }
            )

        with open("../data/data.json", "r") as f:
            json_data = json.load(f)

        json_data.append(
            {
                "date_time": datetime.now(tz_Baku).strftime("%d-%m-%Y %H:%M:%S"),
                "temperature": temperature,
                "description": description,
            }
        )

        with open("data/data.json", "w") as f:
            json.dump(json_data, f, indent=4, separators=(",", ": "))
