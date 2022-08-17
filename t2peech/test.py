from gtts import gTTS
import playsound

mytext = ('Ciumbuleuit ada di bandung')

language = 'id'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj. save("welcome.mp3")

playsound.playsound("welcome.mp3")
