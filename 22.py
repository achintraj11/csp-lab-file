# 22	Write a program to generate the first “n” Fibonacci numbers.	
num = int(input('How many terms? '))

n1, n2 = 0, 1
count = 0

if num <= 0:
   print("Please enter a positive integer2")
elif num == 1:
   print("Fibonacci sequence upto",num,":")
   print(1)
else:
   print("Fibonacci sequence:")
   while count < num:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1