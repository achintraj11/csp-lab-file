# Write a program to check whether a given year is leap year or not
year = int(input('Enter a Year: '))

if year%100 == 0 and year%400 ==0:
    print('Leap year')
elif year%4 == 0 and year%100 != 0:
    print('Leap Year')
else:
    print('No Leap year')

