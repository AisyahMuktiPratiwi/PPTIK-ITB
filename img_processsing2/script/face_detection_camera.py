import cv2
detector_wajah = cv2.CascadeClassifier(
    "../model/haarcascade_frontalface_default.xml")
image = cv2.VideoCapture('../video/video.39')
counter = 0
while True:
    ret, frame = image.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bounding_box = detector_wajah.detectMultiScale(gray, scaleFactor=1.01,
                                                   minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in bounding_box:
        counter += 1
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # x,y koordinat awal box
        # w,h ukuran box lebar & tinggi
        gambar_wajah = frame[y:(y+h), x:(x+w)]
        cv2.imwrite("../output_model/{}.jpg".format(counter), gambar_wajah)
        wajah_blur = cv2.blur(gambar_wajah, (40, 40))
        frame[y:(y+h), x: (x+w)] = wajah_blur
        # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # g   # end = xrayb = cv2.cvtColor(box, cv2.COLOR_BGR2GRAY)

        # start = y
    cv2.imshow("vid", frame)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
image.release
cv2.destroyAllWindows()
