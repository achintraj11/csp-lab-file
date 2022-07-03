# 17	Write a program to check whether a given number is palindrome or not.	
numb = int(input('Enter a number'))
tumb = numb
rev = 0
while(numb > 0):
    div=numb%10
    rev = rev*10 + div
    numb = numb//10
if(rev == tumb):
    print(True)
else:
    print(False)