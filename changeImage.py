#!/usr/bin/env python3

import os
from PIL import Image
directory = os.path.abspath("./supplier-data/images/")

for image in os.listdir(directory):
    image_path = os.path.join(directory,image)
    new_name = image+'.JPEG'
    try:
        with Image.open(image_path) as im:
            new_im = im.rotate(-90).resize((600,400)).convert('RGB').save(directory+new_name)
    except Exception as e:
        print(e)
