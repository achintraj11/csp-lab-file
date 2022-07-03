# 16	Write a program to check whether a given number is prime or not.	
from tkinter.tix import Tree


num = int(input('Enter a number: '))
if num>1:
    for i in range (2,num):
        if(num%i == 0):
            print('not prime')
            break
    else:
        print('prime')
else:
    print('Not Prime')