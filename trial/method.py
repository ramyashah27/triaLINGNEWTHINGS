import random
method= input('which type: ,add ,sub,division,multiplication,average,percentage,square,grade: ')
# if method==str('m') or str('multiplication'):
#     num7=int(input('NO1. FOR MULTIPLICATION: '))
#     num8=int(input('NO2. FOR MULTIPLICATION: '))
#     print(num8*num7)
if method==str('add'):
    num1=int(input('number 1 to add: '))
    num2=int(input('number 2 to add: '))
    print(num1+num2)
elif method==str('sub'):
    num3=int(input('number 1: '))
    num4=int(input('number 2: '))
    print(num3-num4)
elif method==str('average'):
    a=input ("enter first number: ")
    b=input ("enter secound number:" )
    a=int(a)
    b=int(b)
    avg= (a+b)/2
    print("the average of a and b is", avg)
if method==str('multiplication'):
    m1=int(input('enter number 1 for multiplication'))
    m2=int(input('enter number 2 for multiplication'))
    print(m1*m2)
elif method==str('division'):
    d1=int(input('numerator: '))
    d2=int(input('denominator: '))
    print(d1/d2)
elif method==str('percentage'):
    p2=int(input('enter number 1 '))
    p1=int(input('enter number 2 '))
    p=(p2/p1)*100
    print( p)
if method==str('grade'):
    grade=int(input("enter ur marks\n"))
elif   grade>90:
   print("A++")
elif grade>80:
   print("A")
elif grade>70:
   print("b") 
elif grade>60:
   print('c')
elif grade>50:
   print('D') 
elif grade<40:
   print('FAIL')

if method=='':
    print('invalid please select any type of calculation')
if method==str('square'):
    s1=int(input('enter number 1 for square'))
    print(s1*s1)