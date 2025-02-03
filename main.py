import logging
import os
import time
from datetime import datetime

import requests

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
        logging.info("Taking picture...")
        take_current_picture(datetime.today().strftime(time_format) + '.jpg')
        time.sleep(timeout)


if __name__ == "__main__":
    watch()