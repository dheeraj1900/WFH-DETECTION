import face_recognition
import cv2
import numpy as np
import pyautogui
from selenium import webdriver
import time
import os
import capture as cp


# gmail = "monu.196d@gmail.com"
# password = "8700243345"
# video_capture = cv2.VideoCapture(0)

# root_image = face_recognition.load_image_file("dheeraj1.jpg")
root_image=cp.capturephoto()
# root_image=cv2.cvtColor(root_image, cv2.COLOR_BGR2RGB)

test_image=cp.capturephoto()
# test_image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# # cv2.imshow('test',root_image)
# cv2.waitKey()
# root_encoding = face_recognition.face_encodings(root_image)[0]
# test_encoding=face_recognition.face_encodings(test_image)[0]
# print()
if root_image==0 or test_image==0:
	print("image not captured")
else:
	result=face_recognition.compare_faces(root_image,test_image[0])
	print(result)
