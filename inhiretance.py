# class person():
#     country = "india"

#     def takebreath(self):
#         print("i am breathing ...")

# class employee(person) :
#     company = "google"

#     def takebreath(self):
#         print("i am employee hardly taking breath ...!")

# class programmer(employee):
#     company = "tcs"

#     def takebreath(self):
#         print("i am a program i am taking breathing ++...")

# p = person()
# p.takebreath()

# e = employee()
# e.takebreath()
# print(e.country)
# print(e.company)

# pr = programmer()
# pr.takebreath() 
# print(pr.country)
# print(pr.company)


# ##   super 

# class person():
#     country = "india"

#     def __init__(self):
#         print("initiliazing a person ...")

#     def takebreath(self):
#         print("i am breathing ...")

# class employee(person) :
#     company = "google"
#     def __init__(self):
#         super().__init__()

#         print("initiliazing a employee ...")

#     def takebreath(self):
#         # super().takebreath()

#         print("i am employee hardly taking breath ...!")

# class programmer(employee):
#     company = "tcs"

#     def takebreath(self):
#         super().takebreath()

#         print("i am a program i am taking breathing ++...")



# p = person()
# p .takebreath()

# e = employee()
# e.takebreath()







#### class methods 
#### to chnage the instance of class use the class methods

# class employee:
#     company = "cello"
#     salary= 1000
#     location = "ahmedabad"


#   to change the class variable value use this method 
    # def changesalary(self, sal ):
    #     self.__class__.salary= sal

    # def changesalary(self, sal ):
    #     self.salary= sal

#   to change the class variable value use this method 

#     @classmethod
#     def changesalary(cla, sal ):
#         cla.salary= sal
    

# e = employee()
# print(e.salary)

# e.changesalary(34545)
# print(e.salary)

# print(employee.salary)




## PROPERTIES   getter setter 



# class employee :
#     company = "one plues"
#     salary = 5600
#     salarybonus = 400


#     @property    ## getter 
#     def totalsalary(self):
#         return self.salary +self.salarybonus

#     @totalsalary.setter              # setter
#     def totalsalary(self,val):
#         self.salarybonus = val - self.salary
#         return self.salarybonus



# e = employee()
# print(e.totalsalary)
# e.totalsalary = 5800
# print(e.salary)
# print(e.salarybonus)
# print(e.totalsalary)

##  oprator overloading

# class number :
#     def __init__(self, num) :
#         self.num = num
    
#     def __add__(self,num2):
#         print("lets add")
#         return self.num + num2.num
    
#     def __mul__(self,num2) :
#         print("lets multiplication")
#         return self.num * num2.num


# n1 = number(4)
# n2 = number(6)
# n3 = number(34)


# print(n1.__add__(n2))  


# sum = n1 + n2
# print(sum)
# mul = n1 * n2
# print(mul)



# __str __         __len__  



# class number :

#     def __init__(self, num) :
#         self.num = num
    
#     def __add__(self,num2):
#         print("lets add")
#         return self.num + num2.num
    
#     def __mul__(self,num2) :
#         print("lets multiplication")
#         return self.num * num2.num
    
#     def __str__(self):
#         return f"decimal number : {self.num}"

#     def __len__(self):
#         return 10


# n = number(19)
# n1 = number(9)
# sum =n.__add__(n1)
# sum =n + n1
# print(sum)
# mul = n *n1
# print(mul)
# print(n)
# print(len(n))

## pr 
# q - 1


# class d2vec :
    
#     def __init__(self, i , j):
#         self.i = i 
#         self.j = j
#     def __str__(self):
#         return f"{self.i} i  + {self.j} j "

# class d3vec (d2vec):
#     def __init__(self, i, j,k):
#         super().__init__(i, j)
#         self.k = k 

#     def __str__(self):
#         return f"{self.i} i  + {self.j} j + {self.k} k"


# v2d = d2vec(3,4)
# v3d = d3vec(3,4,7)

# print(v2d)
# print (v3d)

# q - 2


# class animal:
#     animaltype : "mammal"

# class pets(animal):
#     colour = "white"

# class dog(pets):

#     @staticmethod
#     def bark():
#         print("bow bow !!")

# d = dog()
# d.bark()
# print(d.colour)


# q - 3

# class employee:
#     company = "google"
#     def __init__(self,salary,increment):
#         self.salary = salary
#         self.increment = increment

#     @property
#     def totalsalary(self):
#         return(self.salary +self.increment)

#     @totalsalary.setter
#     def totalsalary(self,val):
#         self.increment = val - self.salary
#         return (self.increment)

# e = employee(30000,2000)
# # print(e.totalsalary)
# e.totalsalary =40000
# print(e.salary)
# print(e.increment)



# class employee :
#     salary =20000
#     increment = 1.5
#     @property
#     def salaryafterincrement(self):
#         return self.salary*self.increment

#     @salaryafterincrement.setter
#     def salaryafterincrement(self,val):
#         self.increment = val / self.salary
#         return self.increment

# e = employee()
# print(e.salaryafterincrement)
# e.salaryafterincrement = 40000
# print(e.increment)
# print(e.salary)


#   complex number 



# class complex :
#     def __init__(self,r,i):
#         self.real = r
#         self.imaging = i

#     def __add__(self,val):
#         return f"{self.real + val.real} + {self.imaging + val.imaging} i"
 

# n1 = complex(3,5)
# n2 = complex(2,1)
# sum = n1 + n2
# print(sum)


