import cv2
import numpy as np

cam=cv2.VideoCapture(0)
canvas=np.zeros((450,450,3),np.uint8)
cv2.namedWindow("kamera");

def nothing(a):
    pass

cv2.createTrackbar("Hmin","kamera",0,179,nothing)
cv2.createTrackbar("Hmax","kamera",179,179,nothing)
cv2.createTrackbar("Smin","kamera",0,255,nothing)
cv2.createTrackbar("Smax","kamera",255,255,nothing)
cv2.createTrackbar("Vmin","kamera",0,255,nothing)
cv2.createTrackbar("Vmax","kamera",255,255,nothing)

while True:
    res,frame=cam.read()
    frame=cv2.flip(frame,1)
    framehsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    hmin=cv2.getTrackbarPos("Hmin","kamera")
    hmax=cv2.getTrackbarPos("Hmax","kamera")
    smin=cv2.getTrackbarPos("Smin","kamera")
    smax=cv2.getTrackbarPos("Smax","kamera")
    vmin=cv2.getTrackbarPos("Vmin","kamera")
    vmax=cv2.getTrackbarPos("Vmax","kamera")

    h=cv2.getTrackbarPos("Hmin","kamera")
    s = cv2.getTrackbarPos("Smin","kamera")
    v = cv2.getTrackbarPos("Vmin","kamera")


    altdeger=np.array([hmin,smin,vmin])
    ustdeger=np.array([hmax,smax,vmax])
    canvas[:]=[h,s,v]
    mask=cv2.inRange(framehsv,altdeger,ustdeger) #burda ornegın sarı renk ayarladık sarı renk dısındakı yerlerı silicek 
    sonuc=cv2.bitwise_and(frame,frame,mask=mask)


   # cv2.imshow("hsv",framehsv)
    cv2.imshow("kamera",frame)
    cv2.imshow("sonuc",sonuc)
    cv2.imshow("canvas",canvas)
    if cv2.waitKey(25) & 0XFF==ord("q"):
        break


cam.release()
cv2.destroyAllWindows()