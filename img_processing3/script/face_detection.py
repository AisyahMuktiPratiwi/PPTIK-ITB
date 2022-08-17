# pertama
# import cv2
# detector_wajah = cv2.CascadeClassifier(
#     "../model/haarcascade_frontalface_default.xml")

# image = cv2.imread("../images/img1.jpeg")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # while True:
# bounding_box = detector_wajah.detectMultiScale(gray, scaleFactor=1.01,
#                                                minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

# for (x, y, w, h) in bounding_box:
#     # x,y koordinat awal box
#     # w,h ukuran box lebar & tinggi
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#     # grayb = cv2.cvtColor(box, cv2.COLOR_BGR2GRAY)
#     # end = x
#     # start = y
# cv2.imshow("hasil", image)
# cv2.imwrite("../output/hasil_4.jpg", image)
# cv2.waitKey(0)


# kedua
import cv2
import os
import glob
detector_wajah = cv2.CascadeClassifier(
    "../model/haarcascade_frontalface_alt_tree.xml")


data_path = os.path.join('../output_model/videos', '*g')
files = glob.glob(data_path)
# image = cv2.VideoCapture(0)
output = 1
for file in files:
    print(file)
    image = cv2.imread(file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # while True:
    bounding_box = detector_wajah.detectMultiScale(gray, scaleFactor=1.01,
                                                   minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    for (x, y, w, h) in bounding_box:
        output += 1
        # x,y koordinat awal box
        # w,h ukuran box lebar & tinggi
        gambar_wajah = image[y:(y+h), x:(x+w)]
        cv2.imwrite(
            "../output_model/wanita/a_{}.jpg".format(output), gambar_wajah)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # grayb = cv2.cvtColor(box, cv2.COLOR_BGR2GRAY)
        # end = x
        # start = y
# cv2.imshow("hasil", image)
# cv2.imwrite("../output/hasil_4.jpg", image)
    cv2.waitKey(1)
