import random
guessg= random.randint(1,3)
num = int(input('ENTER THE NUMBER: '))

if num>3:
    print('enter number less than 3')
elif num==guessg:
    print('U ARE LUCKY THE NO. IS' , guessg)
else:
    print(' U ARE STUPID',guessg)
