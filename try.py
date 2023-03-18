# while (True):
#     try :
#         print("trying ...")
#         user = input("enter a number : ")
#         user = int(user) 
#         print("prees q for quit ")
#         if user == "q":
#             break
#         if user > 6 :
#             print("number is greater then 6 .")
#         print("keep trying")
#     except Exception as e :
#         print(f"you entered something wrong : {e}")




# try :
#     a = int (input("enter a number : "))
#     c = 1 / a 
#     print(c)

# except ValueError as e :
#     print("enter a valid number .")

# except ZeroDivisionError as e :
#     print("Make sure that number can not divide by zero. ")

# print("thanks for using code ")






# def increment(num) :
#     try :
#         a = int(num) + 1 
#         return a 
#     except :
#         raise ValueError("this is not good dhruv")


# a = increment('dhruv35')
# print(a)



#  try else      else excecute when your code don'n go to except section


# try :
#     a = int (input("enter a number : "))
#     i = 1/a 
#     print(i)

# except Exception as e  :
#     print(e)

# else :
#     print("we are successfull ")




#  try    finally

# try :
#     a = int(input("enter a number : "))
#     i =1 /a
#     print(i)

# except Exception as e :
#     print(e)
#     exit()

# finally :
#     print("we are done ")

# print("code run successfully .")