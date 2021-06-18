#! /usr/bin/env python3


import os
import requests
import re


descriptions_dir = os.path.abspath("./descriptions/")
images_dir = os.path.abspath("./images/")


url = "<external IP>/fruits"


def image_and_descriptions():
    image_and_desc = []
    for descriptions in os.listdir(descriptions_dir):
        desc_basename = descriptions.strip(".txt")
        for images in os.listdir(images_dir):
            if images.strip(".jpeg") == desc_basename:
                image_and_desc.append([images,descriptions])
    return image_and_desc


def get_content_data(contents):
    web_content = []
    for data in contents:
        values = []
        keys = ["name","weight","description","image_name"]
        file_path = os.path.join(descriptions_dir,data[1])
        with open(file_path, 'r') as f:
            lines = f.read().split("\n")[0:3]
            lines[1] = int((re.search(r'\d+', lines[1])).group())
            for line in lines:
                # if re.search(r'\d+', line) == True:
                values.append(line) 
        values.append(data[0])
        content = dict(zip(keys, values))
        web_content.append(content)
    
    return web_content

def upload_content(contents):
    for content in contents:
        response = requests.post(url, json=content)
    return response

if __name__ == "__main__":
    data = image_and_descriptions()
    content = get_content_data(data)
    upload_content(content)