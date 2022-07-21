import logging
import logging.handlers

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "data.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8"
)
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