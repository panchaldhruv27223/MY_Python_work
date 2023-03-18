# i=0
# while i<=5 :

#     print("wow " + str(i))
#     i = i+1

# print("done")

# i = 1
# while (i<=50):
#     print(i)
#     i=i+1
# print("our task is completed")

# fruits = ["mango","banana","chiku","kivi","dragon fruit"]
# i=0
# while i<len(fruits):
#     print(fruits[i])
#     i=i+1

# fruits = ["mango","banana","chiku","kivi","dragon fruit"]

# for item in fruits:
#     print(item)


#  PR



# num = int(input("enter a number \n"))
# for i in range(1,11):
#     mul =num * i
#     print(num," X ",i," = ",mul)
# print("done")



# i=1
# num = int(input("enter a number \n"))
# while i<11:
#     print(num," X ",i," = ",i*num)
#     i=i+1



#   f string 

# num = int(input("enter a number \n"))
# for i in range(1,11):
#     print(f"{num } X {i} = {num*i}")
# print("done")


# l = ["dhruv","palu","pravin","pavan"]

# for name in l:
#     if ( name.startswith("p") ):
#         print("hello " + name)



##   prime number  

# number = int(input("enter a number "))

# prime = True

# for i in range (2,number):
#     if(number%i == 0):
#         prime = False

# if prime:
#     print(f"the {number}  is prime  ")
# else :
#     print(f"the {number}  is not prime ")


##     n natural number sum   --->  1,2,3,4,5,6,7,...
 



# sum = 0
# n = int (input("enter a number :\n"))
# i=1
# while i<=n:
#     sum = sum +i
#     i=i+1

# print("sum :" + str(sum))


## factorial using a for loop

# n = int (input("enter a number :\n"))
# fac = 1
# for i in range (1,n+1):
#     fac = fac*i

# print("fac : " ,str(fac))


#  print("5"*(2))     ----> 55

##    pattern
# *
# **
# *** 

# n = int (input("enter a number :\n"))
# for i in range (n):
#     print("*" * (i+1))


##   pattern

#  *  
# *** 
#*****

n = int (input("enter a number :\n"))
for i in range(n):
    print(" "*(n-i-1), end="")
    print("*" * (2*i+1) , end="")
    print(" "* (n-i-1))


## multiplication table in reverse ordered

# n = int (input("enter a number :\n"))
# for i in range(10,0,-1):
#     print(f"{n} X {i} = {n*i}")

# n = int (input("enter a number :\n"))

for i in reversed(range(1,11)):
    print(f"{n} X {i} = {i*n}")

