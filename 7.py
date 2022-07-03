num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))
num3 = int(input("Enter Number3: "))

if num1>num2 and num1 > num3:
    print(f"{num1} is greatest")
elif num2>num3 and num2 > num3:
    print(f"{num1} is greatest")
elif num3>num1 and num3 > num2:
    print(f"{num1} is greatest")
else:
    print('input not expected')