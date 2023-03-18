# f =open("myfirstfile.txt","r")
# f =open("myfirstfile.txt")
# content = f.read()
# print (content)
# f.close

# f =open("myfirstfile.txt","w")
# f.write("hello Diya panchal ")
# f.close
# f =open("myfirstfile.txt")
# content = f.read()
# print (content)
# f.close

# f = open("myfirstfile.txt")
# content = f.readline()
# print(content , end="")
# content = f.readline()
# print(content)

  #  r = reading  w =writing   + = reading and  writing
  #  a = appending 
  # rt  # rb
# read only some charecters
# f = open("myfirstfile.txt")
# content = f.read(7)
# print(content)
# f.close

# with open("myfirstfile.txt") as f :
#     content=f.read()
#     print(content)


# with open ("this.txt","w") as f :
#     f.write("this is another text file")

# with open ("this.txt") as f :
#     content = f.read()
#     print(content)

# with open ("sample.txt","w") as f :
#     f.write("twinkle twinkle littel star\nhow are wonder what you are")

# q -1

# with open("sample.txt") as f :
#   content = f.read()
#   if "twinkl" in content:
#     print ("present")
#   else :
#     print("absent")

# q - 2

# def game(number):
#   num = number 
#   return num

# n = game(50)

# with open( "highscore.txt") as f :
#   content = f.read()

# with open( "highscore.txt","w" ) as f :
#   if content=="":
#     f.write(str(n))
#   elif n > int(content) :
#     f.write(str(n))
#   else :
#     f.write(str(content))


# Q-3


# for n in range (2,21):
#   with open (f"TABLE/multiplication_{n}.txt","w") as f :
#     for i in range(1,11):
#       f.write(f"{n} x {i} = {i*n}")
#       if i != 10:
#         f.write("\n")

# print("done")


# Q-4   ---> word replace 


# with open ("sample.txt" ) as f :
#   content = f.read()

# if "donkey" in content :
#   content =content.replace("donkey","##@#@#")
#   with open ("sample.txt","w") as f :
#     f.write(content)



# Q - 5

# list = ["gabi","vandri","donkey"]
# with open ("another.txt") as f :
#   content = f.read()

# for i in range (len(list)):
#   if list[i] in content :
#     content = content.replace(list[i],"##@#")
#     with open ("another.txt","w") as f :
#         f.write(content)



# words =["gabi","vandri","donkey"]
# with open ("another.txt") as f:
#   content = f.read()
# for word in words :
#   content = content.replace(word,"#@@@##")
# with open("another.txt","w") as f :
#   f.write(content)

# Q - 6 


# with open ("log.txt","r") as f :
#   content = f.read()
#  # lower() 
# if "python" in content :
#   print("present")
# else:
#   print("absent")

# q - 7

# with open ("log.txt","r") as f :
#   content = f.read()
  # content = f.read().lower()
# if "python" in content :
#   print("present")
# else:
#   print("absent")
 # lower()

# if "python" in content.lower() :
#   print("present")
# else:
#   print("absent")
# content = True
# i = 1 
# with open("log.txt") as f :
#   while content :
#     content = f.readline()
#     if "python" in content.lower() :
#       print (content,end="")
#       print("present" , i)
#     i = i +1

#  q - 8

# with open ("this.txt") as f :
#   content = f.read()

# with open ("copy.txt" , "w") as f :
#   f.write(content)

# q - 9

# file1 = "this.txt"
# file2 = "copy.txt"

# with open (file1) as f:
#   f1 = f.read()

# with open (file2) as f:
#   f2 = f.read()

# if f1 == f2 :
#   print ("files are identical")
# else :
#   print("files are not identical")

# q - 10   --> clear a file 

# with open ("copy.txt" , "w") as f:
#   f.write("")

# q-11  rename 
#  os module

# import os

# old_name = "this.txt"
# new_name = "name_changed_by_python.txt"

# with open (old_name) as f :
#   content = f.read()

# with open (new_name,"w") as f :
#   f.write(content)

# os.remove(old_name)
