# Write a program to find the area and perimeter of shapes (triangle, rectangle and circle).
print('Enter the sides of Rectangle')
rectL=int(input('Enter length!: '))
rectB=int(input('Enter length!: '))
areaRec = rectL* rectB
periRec = rectL*2 + rectB*2

print('Enter the sides of square')
sqSide = int(input('Enter Side of the square: '))
areaSq = sqSide*sqSide
periSq = sqSide*4

print('Enter the sides of Triangle')
s1 = int(input('Enter Side 1 of Triangle: '))
s2 = int(input('Enter Side 2 of Triangle: '))
s3 = int(input('Enter Side 3 of Triangle: '))
periTri = s1 +s2 +s3
print('Enter height and width of triangle')
h = int(input('Enter height of Triangle: '))
b = int(input('Enter bredth of Triangle: '))
areaTri = 1/2 * b * h

print(f"Perimeter of the Rectangle is {periRec}")
print(f"Perimeter of the Square is {periSq}")
print(f"Perimeter of the Triangle is {periTri}")
print(f"Area of the Rectangle is {areaRec}")
print(f"Area of the Square is {areaSq}")
print(f"Area of the Triangle is {areaTri}")
