# 12	Write a program to calculate the net salary of an employee.
# (Net salary = BP+TA+DA+HRA, TA = 5% BP, DA = 10% BP, HRA = 15% BP)	
bp = int(input('Enter bp: '))
# ta = int(input('Enter ta'))
# da = int(input('Enter da'))
# hra = int(input('Enter hra'))

ta = 5 *( bp/ 100)
da = 10 *( bp/ 100)
hra = 15 *( bp/ 100)

total = bp + ta + da + hra

print(f'Total salary is {total}')
