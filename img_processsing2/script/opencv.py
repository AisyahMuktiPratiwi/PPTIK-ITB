import time
import cv2
cap = cv2.VideoCapture(0)  # video
# 0 device bawaan si laptop
# 1 device external camera
# gambar = cv2.imread("../images/panda.jpg") #BGR
# gray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
# while True:
#     cv2.imshow("Frame",  gray)
#     cv2.waitKey(1)

_, image = cap.read()
cv2.imwrite("img1.jpeg", image)
#cv2.imshow("frame", image)
# cv2.waitKey(0)

cv2.destroyAllWindows()
