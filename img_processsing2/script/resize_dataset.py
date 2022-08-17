import cv2
import os
import glob
folder_gambar_cats = "../dataset/cats"
data_path = os.path.join(folder_gambar_cats, '*g')
files = glob.glob(data_path)
number = 1
for file in files:
    gambar = cv2.imread(file)
    gray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
    gambar2 = cv2.resize(gray, (25, 25))
    cv2.imwrite("../dataset/training_neg/{}.jpg".format(number), gambar2)
    print("Gambar {}berhasil di resize &ubah ke grayscale".format(number))
    number += 1
# gambar = cv2.imread(gambar_path)
# gambar_resize = cv2.resize(gambar, (25, 25))
# cv2.imshow("cat", gambar)
# cv2.waitKey(0)
# time.sleep(5)
# cv2.imwrite("../dataset/resized_cat/1.jpg".gambar_resize)
# print("resize_done")
