import cv2
img = cv2.imread('me.jpg') //read the image
//Blur Image Through Averaging 
blurImg = cv2.blur(img,(10,10))
cv2.imshow('Blurred image', blurImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
