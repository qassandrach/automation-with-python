#!/usr/bin/env python3

import os
import requests

directory = os.path.abspath("./supplier-data/images/")

url = "<input django api url here>"

for image in os.listdir(directory):
    image_path = os.path.join(directory,image)
    with open(image_path, 'rb') as f:
        r = requests.post(url, files={'file': f})
