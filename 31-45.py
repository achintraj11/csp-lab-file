'''
#31

def my_function(fname, lname):


    print(fname + " " + lname)

my_function("Achint", "Raj")'''

'''
# 34. This function uses global variables
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


f = factorial(5)
print("factorial of 5 is ", f)'''

'''#32
x = "global "
def fun():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)
fun()'''

'''def recur_sum(n):
    if n <= 1:
        return n
    else:
        return n + recur_sum(n - 1)


num = int(input("Enter a number : "))
if num < 0:
    print("Enter a positive number")
else:
    print("The sum is", recur_sum(num))'''

'''
#35
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


nterms = int(input("Enter the range of fibonacci series "))
if nterms <= 0:
    print("Enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))'''

# 36

'''def doubler(d):
    return lambda x: x * d


def triplet(t):
    return lambda x: x * t


dub = doubler(2)
trip = triplet(3)
var = int(input("Enter a number "))
print("Doubler of", var, " is", dub(var))
print("Triplet of", var, " is", trip(var))
var1 = int(input("Enter a number "))
print("Doubler of", var1, " is", dub(var1))
print("Triplet of", var1, " is", trip(var1))
x
'''
'''
# 37 a)
import math

print(math.sqrt(4))
print(math.pi)
print(math.e)
print(math.sqrt(64))
print(math.sin(45))
print(math.cos(90))
print(math.tan(60))
print(math.log(8))
print(math.pow(4, 3))
print(abs(-7.25))
'''
'''
# b)
from matplotlib import pyplot as plt

# Plotting to our canvas

plt.plot([1, 2, 3], [4, 5, 1])

# Showing what we plotted

plt.show()
'''
'''
# 37 c
import turtle

star = turtle.Turtle()
for i in range(50):
    star.forward(50)
    star.right(144)

turtle.done()'''
'''
import numpy as np

arr = np.array( [[ 1, 2, 3],
 [ 4, 2, 5]] )

print("Array is of type: ", type(arr))

print("No. of dimensions: ", arr.ndim)

print("Shape of array: ", arr.shape)

print("Size of array: ", arr.size)

print("Array stores elements of type: ", arr.dtype)
'''
'''
import random

print("A random number from list is : ", end="")
print(random.choice([1, 4, 8, 10, 3]))
print("A random number from range is : ", end="")
print(random.randrange(20, 50, 3))
'''
'''#38
import custom_module

a = custom_module.person1["age"]
c = custom_module.person1["country"]
print(a)
'''
'''
import math

mfun = [0, 30, 45, 60, 90]
for i in mfun:
    print(math.sin(i))
    print(math.cos(i))
''''''
#40
friend = ["Achint", "Tom", "Kia", "Elly", "Alia"]
print(friend[0])
print(friend[1:3:-1])
print(friend)
friend.append("John")
print(friend)
friend.insert(2, "Me")
print(friend)
friend = ["Achint", "Tom", "Me", "Kia", "Elly", "Alia"]
friend.remove("Me")
print(friend)
friend.clear()
print(friend)
friend = ["Achint", "Tom", "Me", "Kia", "Elly", "Alia"]
friend.pop()
print(friend)
print(friend.index("Me"))
friend = ["Achint", "Tom", "Me", "Kia", "Elly", "Alia", "Me", "Me"]
print(friend.count("Me"))
luck_num = ["8", "46", "48", "66", "23", "91"]
luck_num.sort()
print(luck_num)
luck_num.reverse()
print(luck_num)'''
'''#41
luck_num = ["89", "78", "45", "56", "73", "39"]
d = luck_num.copy()
print(d)'''
'''
#42
my_list = [8, 5, 2, 0, 4]
print(my_list[:])
print(my_list[2:])
print(my_list[:2])
print(my_list[2:4])
print(my_list[::2])
print(my_list[::-2])
print(my_list[1:4:2])
''''''''

result1 = slice(3)
print(result1)
result2 = slice(1, 5, 2)
print(slice(1, 5, 2))
py_string = 'Achint'
slice_object = slice(3)
print(py_string[slice_object])
slice_object = slice(1, 6, 2)
print(py_string[slice_object])
pystring = 'Python'
slice_object = slice(-1, -4, -1)
print(pystring[slice_object])
mary = 'This is CSL 1028'
mary.split()
words = mary.split()
print(words)
print(mary.join(words))''''''''
# 44.
friend = "Achint", "Tom", "Me", "Kia", "Elly", "Achint"
print(friend.count("Achint"))
print(friend.index("Me"))
if 'Ravi' in friend:
    print('Yes')
else:
    print('No')'''

# 45
a_list = [[2, 3, 4], [5, 6, 7]]
print(a_list[0][0])
print(a_list[0][0] * a_list[1][0])
for i in a_list:
    print(i)
b_list = [[2, 3, 4], [5, 6, 7], [8, 4, 1]]
print(int(b_list[0][0][0]))
print(b_list[0][0][0] * b_list[1][0][1])
for j in b_list:
    print(j)