import cv2
import pyttsx3  #this is a package which will allow a voice to say whatever u have written
#text to speech
def my_speak():
    engine = pyttsx3.init()
    engine.say("Alert Fire has been detected!!! Please Run")
    engine.runAndWait()
fire_cascade=cv2.CascadeClassifier("fire_detection.xml")
cam=cv2.VideoCapture(0)
while(True):
    ret,frame=cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    fire=fire_cascade.detectMultiScale(frame,1.2,5)
    
    for x,y,w,h  in fire:
        cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(0,255,0),3)
        roi_gray=gray[y:y+h,x:x+w]  #region of interest
        roi_color=frame[y:y+h,x:x+w]    #region of interest
        
        print("Fire is detected!!!")
        for i in range(3):
            my_speak()    #calling the function
    cv2.imshow("frame",frame)
    if cv2.waitKey(1)==32:
        break
cam.release()
cv2.destroyAllWindows()
        