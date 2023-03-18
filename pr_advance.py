# pr 1


# def readfile(filename):
#     try :
#         with open(filename , "r") as f :
#             content = f.read()
#             print(content)
#     except Exception as e :
#         print(f"this {filename} file is not found ")

# readfile("t1.txt")
# readfile("t2.txt")
# readfile("t3.txt")


# pr 2 

# list = [1,2,3,4,5,6,7,8,9]

# for i,item in enumerate(list) :
#     if i==2 or i==4 or i==6 :
#         print(i,item)


# pr 3 

# user = int(input("enter a number : "))

# table = [user*i for i in range(1,11)]
# print(table)


# pr 4 

# a = int(input("enter a number a : "))
# b = int(input("enter a number b : "))

# try :
#     c = a/b 
#     print(c)
    
        
    

# except :
#     if a==0 and b==0 :
#         print("0")

#     elif b==0 :
#         print("infinite")



#  pr 5 

# num = int(input("enter a number : "))
# l = [num*i for i in range(1,11)]

# print(l)

# with open("table.txt", "a") as f :
#     f.write(str(l))
#     f.write("\n")