# function defination

# def name():
#     print("hello")

# name()

# arguments

# def greeting(name):
#     print("good morning " + name )

# greeting("dhruv")


#  default perameter

# def greeting(name = "Stanger"):
#     print("good morning " + name )

# greeting()


# recurtion

# def  may or may not  return 

#  itration 


# def fac(n):
#     factorial = 1
#     for i in range(1,n+1):
#         factorial = factorial*i
#     return factorial

# f = fac(4)
# print(f)

# recursive       n! = n * (n-1)!



# def fac_rec(n):
#     if n == 0 or n== 1 :
#         return 1 
#     factorial= n * fac_rec(n -1)
#     return factorial

# print(fac_rec(5))


#pr 


# def max(n1,n2,n3):
#     if(n1>n2):
#         if(n1>n3):
#             print (n1)
#         else :
#             print(n3)
#     else:
#         if(n2>n3):
#             print(n2)
#         else:
#             print(n3)

# max(3,45,6)
# max(34,6,8)
# max(2,5,56)



## C TO F

# def cel(c):
#     F = (c*(9/5)) + 32
#     return F

# c = 0
# f =cel(c)
# print(f)


## print( )  -- > use

# print("hello" ,end=" ")
# print("how", end=" ")
# print("are", end=" ")
# print("you", end=" ")
# print("!", end=" ")


##  n natural number sum 

# def sum(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum = sum + i
#     return sum


# number = int(input("how many natural number you want to sum :"))
# print(sum(number))




# write a program to print a pattern


# def pattern(n):
#     for i in range(n,0,-1):
#         print("*"*(i))


# n = int(input("enter a number : \n"))
# pattern(n)

##   strip() =  remove a space from starting and ending
# 
# split == for spliting a string   

# this = "    dhruv panchal    "
# print(this.strip())
# print(this)


# remove and strip

# def rm_strip(this,word):
#     new_st = this.replace(word," ")
#     return new_st.strip()

# string ="     hello i am dhruv       "

# s=rm_strip (string , "dhruv")
# print(s)

# MULTIPLICATION TABLE 

# def multi(n):
#     for i in range (1,11):
#         print(f"{n} X {i} = {i*n}")
    
# num = int(input("Enter a number to which print a multiplication table : \n"))
# multi(num)