from gtts import gTTS
import os

text = open('dem1.txt','r').read()

language = 'en'
output = gTTS(text=text,lang=language,slow=False)
output.save('fileoutput.mp3')
os.system("fileoutput.mp3")