import cv2
cascade = cv2.CascadeClassifier("cascade.xml")

cam=cv2.VideoCapture(0) 
while True:
    ret,frame=cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    face= cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
    
    for x,y,w,h in face:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("This is my face detect from video",frame)
    
    if cv2.waitKey(1)==32:
        break
    
cam.release()
cv2.destroyAllWindows()
