#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

import os
import time
import random
from os import listdir
from os.path import isfile, join
from random import randint
from InstagramAPI import InstagramAPI
import urllib

PhotoPath = "/home/psi/python/ig/feybeclaudia_/"  # Change Directory to Folder with Pics that you want to upload
# Change to your Photo Hashtag
IGCaption = "Your Caption + #Hashtag"

thumb_uri = 'https://instagram.fcgk6-1.fna.fbcdn.net/vp/d9a7b1df0e691f3663644aaed820b1e3/5A63F236/t51.2885-15/e35/26157933_212816202622096_909866749820665856_n.jpg'
thumbnail = thumb_uri.split("/")[-1]
thumbnail = os.path.dirname(os.path.abspath(__file__)) + '/' + thumbnail
print(thumbnail)
#
#urllib.urlretrieve(video_url, video_local_path)
#urllib.urlretrieve(thumb_uri, thumbnail)

x = os.chdir(PhotoPath)
ListFiles = [f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))]
print("Total Photo in this folder:" + str(len(ListFiles)))

# Start Login and Uploading Photo
igapi = InstagramAPI("feybeclaudya", "poiuy09876")
igapi.login()  # login

for i in range(len(ListFiles)):
    photo = ListFiles[i]
    print("Progress :" + str([i + 1]) + " of " + str(len(ListFiles)))
    print("Now Uploading this photo to instagram: " + photo)
    igapi.uploadVideo(photo,thumbnail, caption=IGCaption)
    # sleep for random between 600 - 1200s
    n = randint(600, 1200)
    print("Sleep upload for seconds: " + str(n))
    time.sleep(n)
