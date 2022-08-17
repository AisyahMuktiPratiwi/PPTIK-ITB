import cv2
detector_wajah = cv2.CascadeClassifier(
    "../model/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
while True:
    image = cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bounding_box = detector_wajah.detectMultiScale(gray, scalefactor=1.01,
                                                   inNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in bounding_box:
        # x,y koordinat awal box
        # w, h ukuran box lebar & tinggi
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # grayb = cv2.cytColor(box_wajah, cv2.COLOR_BGR2GRAY)
        # end = x
        # start = y
    cv2.imshow("hasil", image)
    cv2.waitKey(0)
cv2.destroyAllWindows()
