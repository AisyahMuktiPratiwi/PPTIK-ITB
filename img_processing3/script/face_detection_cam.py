import cv2
detector_wajah = cv2.CascadeClassifier("../model/haarcascade_frontalface_alt_tree.xml")

# image = cv2.imread("../images/picture_1.jpg")
image = cv2.VideoCapture(0)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
counter = 0
while True:
    ret, frame = image.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bounding_box = detector_wajah.detectMultiScale(gray, scaleFactor=1.01,
    minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    
    for (x, y, w, h) in bounding_box:
        # x,y koordinat awal box
        # w,h ukuran box lebar & tinggi
        counter+=1
        #Proses untuk blur wajah
        gambar_wajah = frame[y:(y+h),x:(x+w)]
        # cv2.imwrite("../output_model/luthfi/{}.jpg".format(counter), gambar_wajah) #Melakukan save foto
        wajah_blur = cv2.blur(gambar_wajah, (40,40))
        frame[y:(y+h),x:(x+w)] = wajah_blur
    # start = y
    cv2.imshow("Vid", frame) #Yang ini
    # cv2.waitKey(1)
    if cv2.waitKey(1) and 0xFF == ord('q'): #Yang ini
        break

# cv2.imwrite("../output/hasil_4.jpg", image)
image.release() #Yang ini
# cv2.waitKey(0)
cv2.destroyAllWindows()
