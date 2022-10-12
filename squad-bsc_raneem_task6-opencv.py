from statistics import mode
import cv2 as cv
import cv2

import numpy as np

draw=False
ix,iy=-1,-1
mode=True

list=[]

def rectangle_shape(event,x,y,flag,param):
   global list

   if event==cv.EVENT_LBUTTONDOWN :
     list=[(x,y)]
   elif event==cv.EVENT_LBUTTONUP:
        list.append((x,y))

        cv2.rectangle(imgResize, list[0], list[1], (0, 255, 0), 2)
   if event==cv.EVENT_RBUTTONDOWN :
     list=[(x,y)]
   elif event==cv.EVENT_RBUTTONUP:
        list.append((x,y))

        cv2.rectangle(imgResize, list[0], list[1], (255, 0, 0), 2)

print("Left click and dragging the blue rectangle for diferance in Colour and Right click and dragging for differance in shape ")
img=cv.imread("coral4.jpg")
img1=cv.imread("coral3.jpg")
img1Resize = cv2.resize(img1,(500,400))
imgResize = cv2.resize(img,(500,400))
cv.imshow("Original",img1Resize)
img2=imgResize.copy()
img2Resize=cv2.resize(img2,(500,400))
cv.imshow("image2",img2)

cv.namedWindow("Image")
cv.setMouseCallback("Image",rectangle_shape)
while True:
    cv.imshow("Image",imgResize)

#cv.imshow("out",blank)
    cv.waitKey(1)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
cv.destroyAllWindows