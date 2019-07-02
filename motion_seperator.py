#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 09:20:24 2019

@author: spidey
"""



import cv2 
import numpy as np 
  
# Read the main image 
import glob
import os
from datetime import datetime
import shutil

search_dir = "/home/spidey/seperate_files/"

new_files=[]
files = filter(os.path.isfile, glob.glob(search_dir + "*"))
for file in files:
    new_files.append(file)
new_files.sort(key=lambda x: os.path.getmtime(x))
print(new_files)
    
if 'triggered.JPG' in new_files:
    new_files=new_files.remove("/home/spidey/seperate_files/triggered.JPG")

for file in new_files:
    #print(file[-1]) !='G'
    #print(reference_time,file)
    if file[-1] == 'G' or file[-1]=='g':
        img_rgb=cv2.imread(file)
#img_rgb = cv2.imread('05140082.JPG') 
  
# Convert it to grayscale 
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) 
  
# Read the template 
        template = cv2.imread("/home/spidey/seperate_files/triggered.JPG",cv2.IMREAD_GRAYSCALE)
# Store width and heigth of template in w and h 
#w, h = template.shape[::-1] 
  
# Perform match operations. 
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) 
#cv2.imshow('result', res)

# Specify a threshold 
        threshold = .9
  
# Store the coordinates of matched area in a numpy array 
        loc = np.where( res >= threshold)  
        #print(loc)
# Draw a rectangle around the matched region. 
#for pt in zip(*loc[::-1]): 
#    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2) 
        a,b=loc
        if len(a)==0:
            print('No Action!')
            shutil.move(file, '/home/spidey/seperate_files/no_action')
        else:
            print('Action')
            shutil.move(file, '/home/spidey/seperate_files/action')
# Show the final image with the matched area. 
#cv2.namedWindow("Detected", cv2.WINDOW_NORMAL) 
#imS = cv2.resize(img_rgb, (1024, 960))  
#cv2.imshow('Detected',imS)
#cv2.waitKey(0)
#cv2.destroyAllWindows() 