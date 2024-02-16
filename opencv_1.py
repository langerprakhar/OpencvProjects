import cv2

img=cv2.imread("cat.jpg")

cv2.imshow("This is a cat image",img)

cv2.waitKey(10000)
cv2.destroyAllWindows()  #  destroy all windows when any key passes
