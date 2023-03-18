from operator import truediv

# varible name are case sensitive

a= "dhruv panchal"
A=232
d='''dhruv
is
a
good
boy
'''
b=34
c = 458.78
print(A)
print(a)
print(b)
print(c)
print(d)

e =True
f = False 
print(e)
print(f)

g = None
print(g)



x,y,z="dhruv","pravin","chintan"

print(x)
print(y)
print(z)

#  type of variable 

print(type(a))
print(type(A))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))


fruits = ["apple" , "banana" ,"greeps"]

x,y,z = fruits

print(x)
print(y)
print(z)

print(type(x))


x= "dhruv "
y = "panchal "
z="is a coder "

# print(x,y,z)
# print(x+y+z)

x= 5

y= 10

print(x+y)
print(x,y)



#  global variable 


x = "awesome"

def myfun():
    x= "fantastic "
    print("dhruv panchal is a " + x + " guys")

myfun()
print("hello  dhruv panchal you are a " +x)


# 
# we use global 


x= "awesome"

def myfun():
    global x 
    x = "fantastic "
    print("dhruv panchal is a " + x + "gues")

myfun()
print("hello  dhruv panchal you are a " + x)





'''
x = "hello Dhruv "   -- string
x=5  -- int
x = 5.o --float

x = false -- bool

x =["apple" , 'banana' , 'mango'] --list

x =("apple" , 'banana' , 'mango') -- tuple

x ={"apple" , 'banana' , 'mango'} --  set

x ={"name1" :"apple" ,"name": 'banana' ,"name3" : 'mango'} --  dict

x = range() --range



python  number 

1 int   ---   1,2,3,..    -9328547351394
2 float  ---  1.4 ,547.658...
3 complex  --  1j , 2x  ,...



casting   :  int()  , float()  , complex()  ,  str()




for using of random 


import random

ramdom.randrange(1,10)
 


'''