# 45	Write a program to create a 2D list and a 3D list.	
# studemts= ['ayush','raina','solana']
# marks= [34,43,43]
# subject= ['jAVA','Python','js']
# grade= ['A','A+','b+']
# print('\n')
# for i in range (3):
#     print(studemts[i],subject[i],marks[i],grade[i],"\n")


def TwoD(a,b):
    lst = [['#' for i in range (a)] for j in range (b)]
    return lst
a = 3
b = 4
print(TwoD(a,b))

def ThrD(x,y,z):
    lst = [[['#' for i in range (x)] for i in range (y)] for j in range (z)]
    return lst
a =3
b = 4
c = 6
print(ThrD(a,b,c))