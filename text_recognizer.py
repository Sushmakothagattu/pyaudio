import pyttsx3
data = input("Enter the text that you want to convert to speech :\n")
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',rate+1) 
voices = engine.getProperty('voices')
for voice in voices :
       engine.setProperty('voice',voice.id)
       engine.say(data)      
engine.runAndWait()
