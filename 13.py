# 13	Write a program to find the factors of a number.	
num = int(input('Enter a number: '))
print('Factors are:-')

for i in range (2,num):
    if (num%i == 0 ):
        print(f'{i}')