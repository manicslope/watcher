import logging
import os
import time
from datetime import datetime

import requests
from PIL import Image

logging.basicConfig(format='%(asctime)s [%(levelname)-2s] %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')

camera_address = os.environ['camera_address']
capture_url = 'http://' + '/'.join([camera_address, 'capture'])
timeout = 60
time_format = '%Y-%m-%dT%H%M%S'


def take_current_picture(filename):
    with open(filename, 'wb') as handler:
        handler.write(requests.get(capture_url).content)


def watch():
    while True:
        filename = datetime.today().strftime(time_format) + '.jpg'
        take_current_picture(filename)
        with Image.open(filename) as image:
            width, height = image.size
        logging.info(f"Taking picture {width}x{height}...")
        time.sleep(timeout)


if __name__ == "__main__":
    watch()