# -*- coding: utf-8 -*-
"""
Created on Fri May 25 16:24:47 2018

@author: admin
"""
import hashlib
import io
import logging
import os
import random
import re

from lxml import etree
import numpy as np
import PIL.Image
import tensorflow as tf
import sys

image_subdirectory='D:/GitHub/dog_detection_ssd/obj_data/images'
images_paths =os.listdir(image_subdirectory)
for img_file in images_paths:
#    print(img_file)
    img_path = os.path.join(image_subdirectory, img_file)
    xml_path = os.path.join('D:/GitHub/dog_detection_ssd/obj_data/annotations/xmls', img_file.replace('.JPG','.xml'))
    with tf.gfile.GFile(img_path, 'rb') as fid:
        encoded_jpg = fid.read()
        encoded_jpg_io = io.BytesIO(encoded_jpg)
        image = PIL.Image.open(encoded_jpg_io)
        if image.format == 'MPO':
            print(img_file)
            try:
                os.remove(img_path)
            except:
                pass
            try:
                os.remove(xml_path)
            except:
                pass