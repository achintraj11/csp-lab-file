# Write a program to input marks of a student and to find the percentage & grade as per the SMVDU norms

m2 = int(input('Input Marks of m2: '))
mech = int(input('Input Marks of mech: '))
electric = int(input('Input Marks of electric: '))
programing = int(input('Tnput Marks of programing: '))
DHV = int(input('Enter the marks of DHV: '))

total = m2+mech+electric+programing+DHV
percent = total/5

print(f'percentage is {percent}')


