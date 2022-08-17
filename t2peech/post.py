# import requests

# import playsound

# import time

# url = 'http://lisanx.pptik.id/'

# myobj = "Halo Mia"

# x = requests.post(url, data=myobj)

# file = "{}.mp3".format("file_respon")

# with open(file, "wb") as f:

#     f.write(x.content)

# time.sleep(1)

# playsound.playsound(file)
def speechRun(kata):
    import requests
    import os
    data = requests.post('http://lisanx.pptik.id', data="Halo"+kata)
    with open("test.mp3", "wb")as f:
        f.write(data.content)
        from playsound import playsound
        playsound('test.mp3')
