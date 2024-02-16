import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("group.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face=face_cascade.detectMultiScale(gray,1.02,5)
for (x,y,w,h) in face:
    img=cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),3)
cv2.imshow("Face detected in image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()