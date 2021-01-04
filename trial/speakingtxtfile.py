import pyttsx3
# userinput= input('enter file name')
with open('project.txt') as f:
    talk= f.read()
# with open('mom.txt') as m:
#     momy = m.read()
engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio) 
    engine.runAndWait()
# a = input('select mom or dad poem: ')
# if a==str('dad'):
#     print('LISTEN CAREFULLY')
#     speak(talk)
print('LISTEN CAREFULLY')
speak(talk)

#     print('POEM IS OVER')

# elif a==str('mom'):
#     print('LISTEN CAREFULLY')
#     speak(momy)
#     print('POEM IS OVER')

# else:
#     print('PLEASE SELECT AN OPTION FROM MOM AND DAD')

# SELF RELIENT INDIA,