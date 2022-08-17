import cv2
import requests
import playsound

detector_wajah = cv2.CascadeClassifier(
    "../model/haarcascade_frontalface_default.xml")

image = cv2.imread("../images/img1.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# while True:
bounding_box = detector_wajah.detectMultiScale(gray, scaleFactor=1.01,
                                               minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

orang = []

for (x, y, w, h) in bounding_box:
    # x,y koordinat awal box
    # w,h ukuran box lebar & tinggi
    box = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2),
    orang.append(box)
url = 'http://lisanx.pptik.id/'
if (len(orang)) > 0:

    teks = "welcome, Maudy"
cv2.imshow("hasil", image)

x = requests.post(url, data=teks)

file = "../output_suara/{}.mp3".format("file_respon")

with open(file, "wb") as f:
    f.write(x.content)

playsound.playsound(file)

cv2.imwrite("../output/hasil_4.jpg", image)
cv2.waitKey(0)
