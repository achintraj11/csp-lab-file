num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))

if (num1 > num2):
    print(f'{num1} is greatest')
elif(num1 == num2):
    print("Both are equal")
else:
    print(f'{num2} is greatest')