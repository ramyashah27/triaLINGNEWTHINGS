from win32com.client import Dispatch
from playsound import playsound
def speak(str):
    speak = Dispatch(("SAPI.Spvoice"))
    # print(speak[1].id)
    speak.speak(str)
talk= input('listing to guarav sir: ')
if talk==str('please play Dheeme Dheeme by tony kakar') :
    speak('NOW PLAYING dheeme dheeme for kiara topa')
    playsound('C:\\Users\\ADMIN\\Desktop\\python\\chapter 1\\Dheeme Dheeme.mp3')
if talk==str('play truck driver songs') :
    speak('NOW PLAY TRUCK DRIVER SONGS FOR JADI MOM PLEASE STOP IT FAST SO ATLEAST I CAN SURVIVE')
    playsound('C:\\Users\\ADMIN\\Desktop\\python\\chapter 1\\Dheeme Dheeme.mp3')
elif talk==str('what did u ate in lunch'):
    speak('atta dal sabji')
elif talk==str('start the vlog'):
    speak('hey guys welcome to my vlog today is october nahi november nahi december')
elif talk==str('how to ask for water'):
    speak('mam pie heeeeeeea')
elif talk==str('please say politly'):
    speak('please PAPAA laloooooooooooo')
elif talk==str('mo baa'):
    speak('LALALA')
# if __name__ =='__main__':
#     talk=str(input('enter text\n'))
# if talk==str('wishme'):
#     speak('goodevening hello sir how can i help u , u are stupid')

else:
    
    speak(talk)
# import speech_recognition as sp
# rec = sp.Recognizer()
# my_micro = sp.Microphone(device_index=1)
# with my_micro as source:
#     print('listing')
#     audio = rec.listing(source)
#     to_text = rec.recognize_google(audio)
# print(to_text)
