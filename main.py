import speech_recognition as sr
import pyttsx3 as voz
import pywhatkit as wp
name= "pablo"
listener = sr.Recognizer()

# engine = voz.init()

# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[0].id)

# def talk(text):
#     engine.say(text)
#     engine.runAndWait()
def listen():
    try:
        i=0
        with sr.Microphone() as source:
            print("Escuchando...")
            voice=listener.listen(source)
            rec =listener.recognize_google(voice,language="es-CO")
            rec=rec.lower()
            if name in rec:
                rec =rec.replace(name, "")
            #    talk()
    except:
        pass
    return rec

def run():
    rec=listen()
    if 'reproduce' in rec:
        music= rec.replace("reproduce", "")
        print("Reproduciendo "+ music)
        wp.playonyt(music)
run()