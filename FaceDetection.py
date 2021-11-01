#First to import cv2 package,that contain classes for face detection
import cv2

#casecade system that contain features to read face in python
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

#Reading image
img = cv2.imread("60.jpg");

#Reading the img as gray scale
grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);

#search the co-ordinater of the image
faces = face_cascade.detectMultiScale(grey_img, scaleFactor = 1.05, minNeighbors = 5);

print(type(faces))
print(faces);

for x,y,w,h in faces:
	img = cv2.rectangle(img,(x,y), (x+w,y+h),(0,255,0),3)

resized_image = cv2.resize(img,(500,600));
cv2.imshow("60.jpg",resized_image);
cv2.waitKey(0);

print(type(img));
print(img.shape);
