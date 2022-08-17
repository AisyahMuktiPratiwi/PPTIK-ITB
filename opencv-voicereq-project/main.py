import modules.capturing as capturing
import modules.training as training
import modules.testing as testing
Running = True

while Running:
    print("1. Capturing")
    print("2.Cleaning")
    print("3. Training")
    print("4. Testing")
    print("5. exit")

    pilihan = input("Masukkan pilihan yang diinginkan :")
    if pilihan == "1":
        print("1. Webcam")
        print("2. Video")
        pilihan_take = input("Masukan Pilihan yang diinginkan:")
        if pilihan_take == "1":
            capture = capturing.Capture(
                "models/haarcascade_frontalface_alt.xml", source="input", output="output",)
            capture.DetectFaceFromImage()
        elif pilihan_take == "2":
            print("1. Webcam")
            print("2. Video")
            input_type = input("Masukan tipe pengambilan video:")
            source = input("Masukan sumber video:")
            seconds = 0
            if input_type == "1":
                source = int(input_type)
            elif input_type == "2":
                seconds = int(input("Masukan waktu mulai divideo(ms):"))
                source = "input/"+source
            capture = capturing.Capture(
                model="models/haarcascade_frontalface_alt.xml",
                source=source,
                output="output",
                total_data=200,
                start_sec=seconds
            )
        capture.CaptureImage()
    train = training.Training(
        model_path="output",
        model_output="models/dataset_image"
    )
    if pilihan == "2":
        train.Cleaning("models/haarcascade_frontalface_alt_tree.xml")
    if pilihan == "3":
        train.Train()
    if pilihan == "4":
        test = testing.Testing(
            models="models/haarcascade_frontalface_default.xml",
            trained_models="models/dataset_image",
            input="input/video.mp4"
        )
        test.Test()
    if pilihan.lower() == "X".lower():
        Running = False
        print("Program dihentikan")
    print(pilihan)
