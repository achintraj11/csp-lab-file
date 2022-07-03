# 14	Write a program to print each digits of a number.	
from unicodedata import digit


numb = int(input('Enter a number: '))
while(numb > 0):
    digit = (numb % 10)
    numb = numb //10
    print(digit,', ',end="")
