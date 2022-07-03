# 10	Write a program to print the multiplication table of a number up to a range.	
x = int(input('Enter krde bhai koi sa bhi number: '))
y = int(input('Bol bhai kitne tak print karwana hai Multiplication table: '))

for i in range (1,y+1):
    print(f'{x} X {i} = {x*i}')

