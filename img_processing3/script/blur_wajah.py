import cv2
# cv2.circle(image, center_coordinates, radius, color, thickness)
detector_wajah = cv2.CascadeClassifier(
    "../model/haarcascade_frontalface_default.xml")
image = cv2.imread("../images/img1.jpeg")  # BGR
# image = cv2.blur(image, (10,10))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # grayscale
bounding_box = detector_wajah.detectMultiScale(
    gray, scaleFactor=1.01, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
for (x, y, w, h) in bounding_box:
    # ini kode untuk membuat persegi pada suatu gambar
    # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    box_wajah = cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 0, 0), 1)
    # mau slicing gambar koordinat awal persegi (x,y) , koordinat akhir ((x+w),(y+h))
    gambar_wajah = image[y:(y+h), x:(x+w)]  # Ambil gambar spesifik
    wajah_blur = cv2.blur(gambar_wajah, (40, 40))
    image[y:(y+h), x:(x+w)] = wajah_blur
    # cv2.putText(image, "wajah disamarkan", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    oval = cv2.circle(wajah_blur, (int(w/2), int(h/2)),
                      int(w/2), (255, 255, 0), 2)

cv2.imshow("hasil", image)
cv2.waitKey(0)
