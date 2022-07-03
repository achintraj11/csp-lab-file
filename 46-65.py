Q46.
rows =3
columns= 2
mylist = [[0 for x in range(columns)] for x in range(rows)]
for i in range(rows):
 for j in range(columns):
 mylist[i][j] = '%s,%s'%(i,j)
print(mylist)


Q47.
import numpy as np
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float')
print ("Array created using passed list:\n", a)
b = np.array((1 , 3, 2))
print ("\nArray created using passed tuple:\n", b)
c = np.zeros((3, 4))
print ("\nAn array initialized with all zeros:\n", c)
d = np.full((3, 3), 6, dtype = 'complex')
print ("\nAn array initialized with all 6s."
 "Array type is complex:\n", d)
e = np.random.random((2, 2))
print ("\nA random array:\n", e)
f = np.arange(0, 30, 5)
print ("\nA sequential array with steps of 5:\n", f)
g = np.linspace(0, 5, 10)
print ("\nA sequential array with 10 values between" "0 and 5:\n", g)
arr = np.array([[1, 2, 3, 4],
 [5, 2, 4, 2],
 [1, 2, 0, 1]])

newarr = arr.reshape(2, 2, 3)

print ("\nOriginal array:\n", arr)
print ("Reshaped array:\n", newarr)
arr = np.array([[1, 2, 3], [4, 5, 6]])
flarr = arr.flatten()

print ("\nOriginal array:\n", arr)
print ("Fattened array:\n", flarr)

Q48.
import numpy as np
ar1 = np.array([[4,7,8],[7,9,8],[5,3,8]])
ar2 = np.array([[2,5,4],[8,9,4],[7,2,3]])
add = ar1+ar2
difference = ar1-ar2
print(add)
print(difference)

Q49.
import numpy as np
ar1 = np.array([[4,7,8],[7,9,8],[5,3,8]])
ar2 = np.array([[2,5,4],[8,9,4],[7,2,3]])
prod = ar1*ar2
print(prod)

Q50.
tuple1 = tuple()
print(tuple1)
list1= [ 1, 2, 3, 4 ]
tuple2 = tuple(list1)
print(tuple2)
dict = { 1 : 'one', 2 : 'two' }
tuple3 = tuple(dict)
print(tuple3)
string = "PythonClass"
tuple4 = tuple(string)
print(tuple4)

Q51.
myset ={1,2,3}
print(myset)
myset.add(2)
print(myset)
myset.discard(3)
print(myset)
myset1 ={1,2,3,4,5}
myset1.clear()
print(myset1)
print(myset.pop())
myset2 ={1,2,3,4,5}
u = myset2.union(myset)
print(u)
diff = myset1.difference(myset2)

Q52.
mydict ={
 'name':'Achint','age':21,'University': 'SMVDU'
}
mydict2 ={
 'name' :'Sir','age':39,"University" : 'SMVDU'
}
value = mydict['name']
print(value)
mydict['email']='arun@smvdu.ac.in'
del mydict['name']
print(mydict)
print(mydict.pop('age'))
print(mydict.popitem())
mydict_cpy = dict(mydict)
print(mydict_cpy)
mydict.update(mydict2)
print(mydict)

Q53.
from itertools import product
point = namedtuple('Point',['x','y'])
pt = point(1,-4)
pt2 = point(4,6)
prod = product(pt,pt2)
print(list(prod))
Q54.
iterable_value = 'INDIA'
iterable_obj = iter(iterable_value)
while True:
 try:
 item = next(iterable_obj)
 print(item)
 except StopIteration:
 break

Q55.

country ={
1:'Afghanistan',
2:'Albania',
3:'Algeria',
4:'Andorra',
5:'Angola',
6:'Antigua',
7:'Argentina',
8:'Armenia',
9:'Australia',
10:'Austria',
11:'Azerbaijan',
12:'Bahamas',
13:'Bahrain',
14:'Bangladesh',
15:'Barbados',
16:'Belarus',
17:'Belgium',
18:'Belize',
19:'Benin',
20:'Bhutan',
21:'Bolivia',
22:'Bosnia',
23:'Botswana',
24:'Brazil',
25:'Brunei',
}
print(country[23])

Q56.
factorial = {
1:1,
2:2,
3:6,
4:24,
5:120,
6:720,
7:504,
8:40320,
9:362880,
10:3628800,
11:39916800,
12:479001600,
13:6227020800,
14:87178291200,
15:1307674368000,
16:20922789888000,
17:355687428096000,
18:6402373705728000,
19:121645100408832000,
20:2432902008176640000,
21:51090942171709440000,
22:1124000727777607680000,
23:25852016738884976640000,
24:620448401733239439360000,
25:15511210043330985984000000
}
print(factorial[23])

Q57.
class Dog:

 attr1 = "mammal"
 attr2 = "dog"
 def fun(self):
 print("I'm a", self.attr1)
 print("I'm a", self.attr2)
Rodger = Dog()
print(Rodger.attr1)
Rodger.fun()

Q58.
class Marks () :
 dict1={}
 n=int(input ("Enter the number of students: "))
 m=int(input ("Enter the number of subjects: "))
 for i in range(1,n+1) :
 marks=[]
 print("Enter the marks of",i," student: ", end="")
 for j in range(1,m+1) :
 x=int(input())
 marks.append (x)
 dict1[i]=marks
obj=Marks()
print (obj.dict1)

Q59.
class Animals:
 c1= 'hair'
 c2= 'heart'
 c3= 'blood'
class Birds (Animals) :
 c4= 'feathers'
 c5= 'beak'
 c6= 'two legs'
class Dogs (Animals) :
 c7= 'four legs'
 c8= 'canines'
 c9= 'Tails'
class Humans (Animals) :
 c10= 'Two hands and Two legs'
 c11= 'Most developed'
 c12= 'variety of organs'
obj1=Animals ()
obj2=Birds ()
obj3=Dogs ()
obj4=Humans ()
print (obj1.c1)
print (obj2.c2)
print (obj2.c4)
print (obj3.c3)
print (obj4.c3)

Q60.
class Shape (object):
 sides = None
 def __init__(self, sides) :
 self.sides = sides
 def perimeter (self) :
 perimeter = 0
 for side in self.sides :
 perimeter += side
 return perimeter
class Triangle (Shape):
 def __init__(self, side1, side2, side3) :
 self.sides = [side1, side2, side3]
class Rectangle (Shape):
 def __init__(self, length, width) :
 self.sides = [length, width, length, width]
class Square (Shape) :
 def __init__(self, side) :
 self.sides = [side, side, side, side]
triangle = Triangle (3, 4, 5)
print("Triangle sides: ", triangle.sides)
print("Perimeter of triangle: ", triangle.perimeter ())
rectangle = Rectangle (4, 2)
print("Rectangle sides: ", rectangle.sides)
print ("Perimeter of rectangle: ", rectangle.perimeter ())
square = Square (2)
print ("Square sides: ", square.sides)
print("Perimeter of square: ", square.perimeter ())

Q61.
class tree :
 def __init__(self, n, c) :
 self.name = n
 self.colour = c
class fruits (tree) :
 def __init__(self, n, c) :
 tree. __init__(self, n, c)
 def p(self) :
 print ("The fruit is:", self.name)
 print("The colour is:", self.colour)
class veg (tree) :
 def __init__(self, n, c) :
 tree. __init__(self, n, c)
 def p(self) :
 print ("The vegetable is:", self.name)
 print ("The colour is:", self.colour)
class juice (tree) :
 def __init__(self, n, f) :
 tree. __init__(self, n, f)
 def p(self) :
 print("The juice is of fruit:", self.colour)
class dry (tree) :
 def __init__(self, n, c) :
 tree. _init_(self, n, c)
 def p(self) :
 print("The dry fruit is:", self.name)
 print("The colour is:", self.colour)
n = input ("Enter the type of food (Fruit/Vegetable/Juice/Dry Fruit) :")
if n == "Fruit":
 a=input("Enter the name: ")
 b=input("Enter the colour: ")
 f1 =fruits (a, b)
 f1.p()
elif n == "Vegetable" :
 a=input("Enter the name: ")
 b=input("Enter the colour: ")
 v1 =veg (a, b)
 v1.p()
elif n == "Juice" :
 a=input("Enter the fruit it is made of:")
 j1 = juice ("Juice",a)
 j1.p()
elif n == "Dry Fruite" :
 a=input("Enter the name: ")
 b=input("Enter the colour: ")
 d1 = dry (a, b)
 d1.p()
else :
 print ("Invalid Input. ")
Q62.
class CSE:
 def __init__(self, a, b) :
 self.sub1 = a
 self.sub2 = b
 def subCSE (self) :
 print ("The first subject is: ", self.sub1)
 print("The second subject is: ", self.sub2)
class ECE:
 def __init__(self, a) :
 self.sub3 = a
 def subECE (self) :
 print("The third subject is: ", self.sub3)
class ENG:
 def __init__(self, a):
 self.sub4 = a
 def subENG (self) :
 print ("The fourth subject is: ", self.sub4)
class PSC:
 def __init__(self, a) :
 self.sub5 = a
 def subPSC (self) :
 print("The fifth subject is: ", self.sub5)
class Student(CSE, ECE, ENG, PSC) :
 def __init__(self, n, s1, s2, s3, s4, s5) :
 self.name = n
 print("\nThe student is of CSE Dept.\nHis name is: ", self.name)
 CSE.__init__(self, s1, s2)
 ECE.__init__(self, s3)
 ENG.__init__(self, s4)
 PSC.__init__(self, s5)
a = "Data Structure using C"
b = "Programming using Python"
c = "Digital Electronics"
d = "Science"
e = "Discourse on Human Virtues"
n = input("Enter the student name: ")
s = Student(n, a, b, c, d, e)
s.subCSE ()
s.subECE ()
s.subENG ()
s.subPSC ()
Q63.
import tkinter
a = tkinter.Tk()
a.title ("All shapes")
c = tkinter.Canvas(a, width=700, height=700)
c.pack()
c.create_line(50,100,500,200,fill="green")
c.create_line(50,200,100,300,150,200,50,200,fill="blue")
c.create_rectangle(200,200,300,300,fill="green",outline="green")
c.create_rectangle(500,200,800,300,fill="yellow",outline="white")
c.create_oval(100,100,400,200, fill="pink",outline="white")
c.create_oval(100,400,200,500,fill="red",outline="white")
c.create_polygon(100,550,300,500,400,600,300,750,300,800,200,800,1
00,550, fill="orange",outline="white")
Q64.
import tkinter
a = tkinter.Tk()
a.title("3*3 cells")
c = tkinter.Canvas(a, width=1000, height=1000)
c.pack ()
lst1 = ["red","blue","green","yellow","pink","light blue","light
green","purple","orange"]
lst2 = [100,200,300,400]
x = 0
for i in range((len(lst2))-1) :
 for j in range(len(lst2)-1) :
 n = c.create_rectangle (lst2[i],lst2[j],lst2[i+1],lst2[j+1],fill =
lst1[x],outline="white")
 x+=1
a.mainloop()
Q65.
import tkinter
a = tkinter.Tk()
a.title("Registration Form")
f1 = tkinter.Frame(a).grid(row=0)
l1 = tkinter.Label(f1,text= "First Name")
l1.grid(row=0, column=0)
fName = tkinter.Entry(a)
fName.grid(row=0,column=1)
l2 = tkinter.Label(f1, text = "Last Name")
l2.grid(row=1, column=0)
lName = tkinter.Entry(a)
lName.grid(row=1, column=1)
f2 = tkinter.Frame(a).grid(row = 1)
l3 = tkinter.Label(f2, text = "Sex")
l3.grid(row=2,rowspan=3, column=0)
var =tkinter.IntVar()
R1 = tkinter.Radiobutton(f2, text="Male", variable = var, value = 1)
R1.grid(row=2, column = 1, sticky="W")
R2 = tkinter.Radiobutton(f2, text="Female", variable = var, value = 2)
R2.grid(row=3, column = 1, sticky="W")
R3 = tkinter.Radiobutton(f2, text="other", variable = var, value = 3)
R3.grid(row=4, column = 1, sticky="W")
l4 = tkinter.Label(f2, text = "Age")
l4. grid(row=6, column=0)
W = tkinter.Spinbox(f2, from_=18, to=60)
W.grid(row = 6, column=1)
l5 = tkinter.Label(f1, text = "Address")
l5.grid(row = 8, column = 0)
A1 = tkinter.Entry(a)
A1.grid(row=8, column=1)
l6 = tkinter.Label(f2, text = "Mobile Number")
l6. grid(row = 9, column = 0)
M = tkinter.Entry(a)
M.grid(row = 9, column =1)
var1 = tkinter.IntVar()
c1 = tkinter.Checkbutton (text = "I agree all the terms and condition",
variable= var1)
c1.grid(row = 10, column = 0)
B1 = tkinter.Button(text = "Submit")
B1.grid(row = 11, column = 1)