from os import access
from sre_constants import SUCCESS
from turtle import distance
import cv2
import time
import math
g1=530
g2=300
xs=[]
ys=[]
video=cv2.VideoCapture('PRO-C107-Reference-Code-main/bb3.mp4')
tracker=cv2.TrackerCSRT_create()
ret,image=video.read()
bbox=cv2.selectROI('tracking',image,False)
tracker.init(image,bbox)
def drawbox(image,bbox):
    x,y,h,w=int(bbox[0]),int(bbox[1]),int(bbox[3]),int(bbox[2])
    
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),3,1)
def gt(image,bbox):
    x,y,h,w=int(bbox[0]),int(bbox[1]),int(bbox[3]),int(bbox[2])
    c1=x+int(w/2)
    c2=y+int(h/2)
    cv2.circle(image,(c1,c2),2,(0,255,0),3)
    cv2.circle(image,(g1,g2),2,(0,0,255),3)
    distance=math.sqrt(((c1-g1)**2)+((c2-g2)**2))
    if distance <=20:
        cv2.putText(image,'goal achived',(350,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    xs.append(c1)
    ys.append(c2)
    for i in range(len(xs)-1):
        cv2.circle(image,(int(xs[i]),int(ys[i])),2,(0,0,255),5)
while True:
    ret,image=video.read()
    success,bbox=tracker.update(image)
    if success==True:
        drawbox(image,bbox)
    gt(image,bbox)
    cv2.imshow('ojbect tracking',image)
    if cv2.waitKey(1)==32:
        break
video.release()
cv2.destroyAllWindows()