import cv2
import numpy as np


cap=cv2.VideoCapture(0)


while True:
    _,frame=cap.read()

    edges=cv2.Canny(frame,100,100)
    cv2.imshow("Frame",frame)
    cv2.imshow("Edges",edges)


#Generating the final output




    cv2.waitKey(1)

    k=cv2.waitKey(46)

    if k== 27 & 0xff:
        break
cap.release()
