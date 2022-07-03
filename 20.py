# write a program to find the factorial of a number
from math import factorial


num = int(input('Enter a number: '))
factorial = 1
if num < 0:
    print('Sorry no Factorial for this number')
elif num ==0 :
    print('Factorial is 0')
else:
    for i in range (1,num+1):
        factorial = factorial * i
print(f'factorial is {factorial}')


