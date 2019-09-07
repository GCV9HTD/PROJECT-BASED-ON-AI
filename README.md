## Applications
This can be used by drivers who tend to drive for a longer period of time that may lead to accidents


### Code Requirements
The example code is in Python ([version 2.7](https://www.python.org/download/releases/2.7/) or higher will work). 

### Dependencies

1) import cv2
2) import imutils
3) import dlib
4) import scipy


### Description

A computer vision system that can automatically detect driver drowsiness in a real-time video stream and then play an alarm if the driver appears to be drowsy.

### Algorithm

Each eye is represented by 6 (x, y)-coordinates, starting at the left-corner of the eye (as if you were looking at the person), and then working clockwise around the eye:.

### How to execute

1) first you want to install python IDLE
2) Then open your command prompt -move directory- to the place where python has installed
3) Use the command "py -m pip install module_name"
4) for this you need to install opencv , scipy  ,imutils, dlib modules
5) for dat file click here "http://dlib.net/files/" and download "shape_predictor_68_face_landmarks.dat file"
6) To run this application use command  "python filename.py"
