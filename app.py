from cv2 import cv2

face_cascade = cv2.CascadeClassifier("c:\\Users\\aksha\Desktop\\haarcascade_frontalface_default.xml")#read haarcascade stored on your computer
img = cv2.imread("c:\\Users\\aksha\Desktop\\akshata.png")#read an image stored on your computer
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#coverting to grey colour image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors = 5)
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, h+y), (0, 255, 0), 3)
resize=cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Gray", resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
