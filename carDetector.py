import numpy as np
import cv2

car_cascade = cv2.CascadeClassifier('D:\\Workspace\\Python\\Company\\Car detection\\cars.xml')
cap = cv2.VideoCapture('D:\\Workspace\\Python\\Company\\Car detection\\video2.avi')

x1 = 0
y1 = 300
height = 300
width = 1200

while True:
    ret, img = cap.read()
    cv2.rectangle(img, (x1, y1), (x1 + width, y1 + height), (0, 255, 255), 2)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_area = gray[y1:y1+height,x1:x1+width]

    cars = car_cascade.detectMultiScale(gray_area, 1.1, 4)
    for (x,y,w,h) in cars:
        cv2.rectangle(gray_area,(x,y),(x+w,y+h),(0,255,0),2)
        car_size = gray_area[y1:y1+height,x1:x1+width]
        cv2.rectangle(img, (x+x1, y+y1), (x+x1 + w, y+y1 + h), (255, 0, 0), 2)

    cv2.imshow('img',img)
    cv2.imshow('imggray',gray_area)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()