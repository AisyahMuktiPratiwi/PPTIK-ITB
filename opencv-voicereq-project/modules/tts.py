class TextSpeech:
    def __init__(self, text="", output="", voice_type=""):

        self.text = text
        self.output = output
        self.voice_type = voice_type

    def PPTIKSpeech(self):
        import requests
        import os
        if self.voice_type == "1":
            from gtts import gTTS
            tts = gTTS("Halo"+self.txt)
            tts.save(self.ouput+"/"+self.text+".mp3")
        elif self.voice_type == "2":
            data = requests.post("http://11sanx.pptik.1d",
                                 data="Halo "+self.text)
            with open(self.output+"/"+self.text+".mp3", "wb") as f:
                f.write(data.content)

            # pip install playsound

        from playsound import playsound
        playsound(self.output+'/'+self.text+'.mp3')
