# class Employee:
#     company = "google"

# Dhruv = Employee()
# print(Dhruv.company)




# class maths :

#     def sum(self):
#         return self.a + self.b

# sumation = maths()
# sumation.a = 34
# sumation.b = 30
# c = sumation.sum()
# print(c)



# class Railway :
#     formtype = "Railwayreservation"

#     def data(self):
#         print(f"the name of pasanger : {self.name}")
#         print(f"your train number is : {self.train_no}")


# DhruvApplication = Railway()
# DhruvApplication.name ="Dhruv Panchal"
# DhruvApplication.train_no =22959


# print(DhruvApplication.formtype)
# DhruvApplication.data()




# class employee :
#     company = "google"

#     def info(self):
#         print(self.name)
#         print(self.company)

# dhruv = employee()
# dhruv.name = "Dhruv Panchal"
# dhruv.company = "youtube"
# dhruv.info()

# # self 

# class employee:
#     company = "google"

#     def getsalary(self):
#         print(10000)

# dhruv=employee()
# dhruv.getsalary()

# employee.getsalary(dhruv)


# class employee:
#     company = "google"

#     def getsalary(self):
#         print(f"company = {self.company}")
#         print(f"salary = {self.salary}")

# dhruv=employee()
# dhruv.salary= 123344445
# dhruv.getsalary()    #  employee.getsalary(dhruv)

# static   -->  no need to write self 

# class you :
#     @staticmethod
#     def greet(name, signature ):
#         print(f"good morning  {name} sir \n{signature}")


# dhruv = you()
# dhruv.greet("Dhruv","Thanks")



# constructor

# class employee :
    
    #  this is a constructor this is use explicetly it is use for intiallizing        -----      setter

#     def __init__(self,name,salary,subunit):
#         print("i am a constructor")
#         self.name = name 
#         self.salary = salary
#         self.subunit = subunit
    
#     @staticmethod
#     def greeting():
#         print ("good morning")
    
#     def info(self):
#         print(self.name)
#         print(self.salary)
#         print(self.subunit)

# dhruv =  employee("dhruv",2334554,"youtube")
# dhruv.info()
# dhruv.greeting()




#    __str__()         -----     gatter

# class employee :
#     def __init__(self, name , age):
#         self.a = age
#         self.n = name 

#     def __str__(self) :
#         return (f"{self.n}")

#     def details (self):
#         print(f"your name is : {self.n}")
#         print(f"your age is : {self.a}")

# dhruv = employee("Dhruv",19)

# dhruv.details()

# print(dhruv)







#  pr
# q -1

# class employee:
#     company = "micoshoft" 
#     def __init__(self,name,salary,department):
#         self.name = name 
#         self.salary=salary
#         self.department=department
#         print("employee is added")
    
#     def getinfo(self):
#         print(f"the employee of {self.company} name : {self.name} \n work at this department {self.department} & your salary : {self.salary}")

# employee = employee("Dhruv",23434343,"coding")
# employee.getinfo()


#  Q - 2
# square cube squerroot

# class calculatter :
#     def square(self,n):
#         mul = n*n
#         return mul
#     def cube(self,n):
#         mul = n*n*n
#         return mul
#     def sqroot(self,n):
#         for i in range (1,n):
#             if i*i == n :
#                 return i
#         return f"sqroot of {n} is not avalable"

# cal = calculatter()
# print("welcome to the dhruv's calculator")


# print('''which opration you want to perform ,
# your option are :
# 1.square 
# 2.cube
# 3.sqroot''')

# item = int(input("enter a number \n"))

# r = True

# if (item != 1 ) and (item != 2) and ( item != 3) :
#     for j in range(1,4):
#         print("opps you take wrong option take another chance")
#         if j == 3 :
#             print("this is you last try .")
        
#         item = int(input("enter your choice : \n"))

#         if (item == 1 ) or (item == 2) or ( item == 3) :
#             r = True
#             break
#         r = False    

# if r == True :

#     User =int(input("enter a number : \n"))

#     if (item) == 1 :
        # print(f"the square of {User} is : {cal.square(User)}")

#     elif (item) == 2 :
#         print(f"the cube of {User} is : {cal.cube(User)}")

#     elif (item) == 3 :
#         print(f"the sqroot of {User} is : {cal.sqroot(User)}")

# print("thanks for visit >...")

# by another methods 





# class calculator :
#     def __init__(self,number):
#         self.num = number

#     def square(self):
#         print(f"the square of {self.num} is = {self.num **2}")
#     def cube(self):
#         print(f"the cube of {self.num} is = {self.num **3}")
#     def squareroot(self):
#         print(f"the squareroot of {self.num} is = {self.num **0.5}")

# cal = calculator(9)
# cal.square()
# cal.cube()
# cal.squareroot()




# class sample :
#     a = 565
#     def info (self):
#         print(self.a)

# cal = sample()
# cal.a = 3454

# print(cal.a)
# print(sample.a)
# cal.info()






# class calculator :
#     @staticmethod
#     def greet():
#         print("welcome to the best calculator of the world")

#     def __init__(self,number):
#         self.num = number

#     def square(self):
#         print(f"the square of {self.num} is = {self.num **2}")
#     def cube(self):
#         print(f"the cube of {self.num} is = {self.num **3}")
#     def squareroot(self):
#         print(f"the squareroot of {self.num} is = {self.num **0.5}")

# cal = calculator(9)
# cal.greet()
# cal.square()
# cal.cube()
# cal.squareroot()






class train :
    def __init__(self,name,fare,seats):
        self.name = name 
        self.fare =  fare 
        self.seats = seats 

    def getstatus(self):
        print(f"the  name of the train : {self.name}")
        print(f"the avalible sets in the train : {self.seats}")

    def traininfo(self):
        print(f"the cost of set is {self.fare}")

    def bookticket(self):
        if (self.seats >0):
            print(f"your ticket is booked and your seat number : {self.seats}")
            self.seats = self.seats - 1 
        else :
            print("sorry !!! train is full plz try in tatkal")

intercity = train("intercity express : 22959" , 90 , 300) 
intercity.getstatus()
intercity.traininfo()
intercity.bookticket()
