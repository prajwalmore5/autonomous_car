import cv2
import numpy as np
import requests

#vid=cv2.VideoCapture('road_car_view.mp4')

url = 'http://192.168.26.233:8080/shot.jpg'

while True:
   # ret ,frame=vid.read()
    #if not ret:
    #    vid=cv2.VideoCapture('road_car_view.mp4')
     #   continue
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    frame = cv2.imdecode(img_arr, -1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    low_yellow=np.array([15,126,142])
    up_yellow=np.array([48,255,255])
    mask=cv2.inRange(gray,low_yellow,up_yellow)
    edges=cv2.Canny(mask,100,200)
    lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2=line[0]
            cv2.line(frame,(x1,y1),(x2,y2),(255,255,255),5)
    

        
    cv2.imshow('FINAL',frame)


    if cv2.waitKey(1) & 0xFF==ord('e'):
        break
frame.release()
cv2.destroyAllWindows()
