import os

import requests

camera_address = os.environ['camera_address']
capture_url = 'http://' + '/'.join([camera_address, 'capture'])

with open('capture.jpg', 'wb') as handler:
    handler.write(requests.get(capture_url).content)