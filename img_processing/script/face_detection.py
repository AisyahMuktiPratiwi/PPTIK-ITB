import cv2
detector_wajah = cv2.CascadeClassifier(
    "../model/haarcascade_frontalface_default.xml")
image = cv2.imread("../image/img1.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# while True:
bounding_box = detector_wajah.detectMultiScale(gray, scaleFactor=1.05,
                                               minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
for (x, y, w, h) in bounding_box:
    box = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # grayb = cv2.cvtColor(box, cv2.COLOR_BGR2GRAY)
    # end = x
    # start = y
cv2.imshow("hasil", image)
cv2.imwrite("hasil_3.jpeg", image)
cv2.waitKey(0)
