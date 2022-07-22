from datetime import datetime
import logging
import time
from pytz import timezone, utc

import requests

def customTime(*args):
        utc_dt = utc.localize(datetime.utcnow())
        my_tz = timezone("Asia/Baku")
        converted = utc_dt.astimezone(my_tz)
        return converted.timetuple()
logging.Formatter.converter = customTime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.FileHandler("data.log", encoding="utf8")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)



if __name__ == "__main__":
    r = requests.get("https://weather.talkpython.fm/api/weather?city=baku&country=AZ")

    if r.status_code == 200:
        data = r.json()
        temperature = data["forecast"]["temp"]
        weather = data["weather"]["description"]
        logger.info(f"Weather in Baku: {temperature}°C - {weather}")