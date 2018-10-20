import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import ReleaseKey, PressKey, W, A, S, D

def process_img(orignal_image):
    processed_img = cv2.cvtColor(orignal_image, cv2.COLOR_BGR2GRAY) #converts image into gray colour
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300) #edge detection on gray image
    return processed_img

#contdown loop
for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

last_time = time.time() #gives time before execution of while loop
while(True):
    #creates window of required resolution of orignal display
    screen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    new_screen = process_img(screen) #calls process_img and applys affects to display window

    #controls character movement
    print('down')
    PressKey(W)
    time.sleep(3)
    print('up')
    ReleaseKey(W)

    print('Loop took {} seconds'.format(time.time()-last_time)) #prints time while executing while loop
    last_time = time.time()
    cv2.imshow('window',new_screen) #displays window converted to gray
    #cv2.imshow('window2',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)) #displays window and converts color scheme
    if cv2.waitKey(25) & 0xFF == ord('q'):  #exception
        cv2.destroyAllWindows()
        break
