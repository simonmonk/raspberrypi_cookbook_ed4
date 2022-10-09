import cv2, pkg_resources

haar_file = pkg_resources.resource_filename('cv2', 'data/haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(haar_file)

img = cv2.imread('faces.jpg', cv2.IMREAD_GRAYSCALE)

scale_factor = 1.4
min_neighbors = 5

faces = face_cascade.detectMultiScale(img, scale_factor, min_neighbors)
print(faces)

for (x,y,w,h) in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (255, 255, 255), 2)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
