import cv2
import numpy as np
import time

start=time.time()

img=cv2.imread('lemons1.jpeg')
smooth=cv2.bilateralFilter(img, 15, 50, 50)
kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
sharpen=cv2.filter2D(smooth, -1, kernel)

gray_img = cv2.cvtColor(sharpen, cv2.COLOR_BGR2GRAY)

blur = cv2.medianBlur(gray_img, 5)
cimg = cv2.cvtColor(blur,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)



print("There are", len(circles[0]), "lemons present")
print("Program took", time.time()-start)    


cv2.imshow('image', img)
cv2.imshow('lemons', cimg)

k = cv2.waitKey(0) & 0xFF               
if k == 27:  
    cv2.destroyAllWindows()

    