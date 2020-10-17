import cv2
import numpy as np


cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()



    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower = np.array([38, 86, 0])
    upper = np.array([121, 255, 255])

    mask=cv2.inRange(hsv,lower,upper)

    contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for i in contours:
        area=cv2.contourArea(i)


        if area > 18000:
            print(area)

    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)


    cv2.imshow("image",frame)
    cv2.imshow("mask",mask)


    k=cv2.waitKey(500)

    if k== 27 & 0xff:
        break
cap.release()
