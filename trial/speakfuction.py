# from win32com.client import Dispatch
# # import win32com
# def speak(str):
#     speak = Dispatch(("SAPI.Spvoice"))
#     # speak = Dispatch((SAPI.sp))
#     speak.speak(str)

# if __name__ =='__main__':
#     talk=str(input('enter text\n'))
# if talks==str('wishme'):
#     speak('goodevening hello sir how can i help u , u are stupid')
# if talks==str('what is your name'):
#     speak('i am gotiya the indian bot')
# else:
#     speak(talks)
import pyttsx3
engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[1].id)
def speak(audio):

    engine.say(audio) 
    engine.runAndWait()
talks=(input('enter the text: '))
speak(talks)
# if talks==str('wishme') or str('wish me'):
#     speak('goodevening hello sir how can i help u , u are stupid')
# if talks==str('what is your name'):
#     speak('i am gotiya the indian bot')
# else:
#     speak(talks)