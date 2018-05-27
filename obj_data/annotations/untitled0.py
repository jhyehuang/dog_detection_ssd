# -*- coding: utf-8 -*-
"""
Created on Thu May 24 19:13:07 2018

@author: admin
"""

import os
files=os.listdir('./')
for file in files:
    if not 'xml' in file:
        continue
    fp1=open(file,'r')    
    fp2=open('./tmp/'+file,'w')
    all_str=fp1.readlines()
    for line in all_str:
        if 'D:\GitHub\dog_detection_ssd\obj_data\images' in line:
            print(line)
        line=line.replace('D:\GitHub\dog_detection_ssd\obj_data\images','/home/zhijie.huang/github/dog_detection_ssd/obj_data/images')
        fp2.write(line)
    fp1.close()
    fp2.close()
