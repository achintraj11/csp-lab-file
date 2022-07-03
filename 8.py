# Write a program to find the largest string (size wise & alphabetical wise) among two strings
import string

str1 = input('Enter 1st String: ')
str2 = input('Enter 2nd String: ')

x = len(str1)
y = len(str2)

if (x > y):
    print(f'{x} is the largest string')
else:
    print(f"{y} is the largest string")
