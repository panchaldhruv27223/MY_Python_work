d1={
    "name":"dhruv",
    "surname":  "panchal",
    1:10100,
    "friend":"chintan",
    "marks":[1,2,4,5,7,8],
    "class":{
        2:3245,
        4:4534,
        6:45435
    }
}

print(d1)
print(d1.keys())
print(d1.values())
print(type(d1))
print(list(d1.items()))

print(d1["name"])
d1["marks"]=[45,6,78,8,43]
print(d1["marks"])
print(d1["class"][2])

d2={
    "pravin": "friend",
    "chintan":"friend",
    "abc":"becdcs"
}

d1.update(d2)

print(d1)


# print(list(d1.items()))
# d1.update({"dhruv":"it"})
# print(list(d1))
# print(list(d1.items()))

# print(d1["dhruv"])
# print(d1.get("dhruv"))

# print(d1.get("it"))   # it returns none if we can not get key value pair
# print(d1["it"])      # throw an error 



#  sets 

# s ={1,3,5,6,8}
# print(s)
# print(type(s))

# s={}  # empty dictionary
# print(type(s))

# s=set()  # empty set 
# print(type(s))


# method 



# s= set()
# s.add(4)
# s.add(45)     # add an element
# s.add(345)
# s.add("dhruv")
# print(s)
# print(type(s))

# s.remove("dhruv")     # remove an element 
# # s.remove("panchal")   # throw a error 
# print(s)


# s.pop()     # remove random element from set

# print(s)

# s.clear()    # empty set  (clear set)

# print(s)

# s = {1,2,4,5}

# s1=s.union({5,6,8,9})
# print(s1)

# s1=s.intersection({4,5,6,7,8})
# print(s1)


# pr

# mydic ={
#     "pankha" : "fan",
#     "vastu" : "item",
#     "dabba" : "box",
# }

# print("options are : " , mydic.keys())
# a = input("enter your choise " )
# print("meaning of your word is :" , mydic.get(a))

# n1 = int(input("enter a number 1 :" ))
# n2 = int(input("enter a number 2 :" ))
# n3 = int(input("enter a number 3 :" ))
# n4 = int(input("enter a number 4 :" ))
# n5 = int(input("enter a number 5 :" ))
# n6 = int(input("enter a number 6 :" ))
# n7 = int(input("enter a number 7 :" ))
# n8 = int(input("enter a number 8 :" ))


# s ={n1,n2,n3,n4,n5,n6,n7,n8}
# print(s)
 

 # take 3 differant element

# s = {11,"11", 11.454}
# print(type(s))
# print(s)
# print(len(s))

# s = set()
# s.add(20)
# s.add(20.0)   # take as same  20 = 20.0
# s.add("20")
# print(s)
# print(len(s))

# s ={}      # it is a dictionary 
# print(type(s))    

# s={}

# dhruv = input("dhruv enter your favourate language : ")
# ankita = input("ankita enter your favourate language : ")
# vidhi = input("vidhi enter your favourate language : ")
# ani = input("ani enter your favourate language : ")

# s["Dhruv"]=dhruv
# s["Ankita"]=ankita
# s["Vidhi"]=vidhi
# s["Ani"]=ani

# print(s)

# s={}

# dhruv = input("dhruv enter your favourate language : ")
# ankita = input("ankita enter your favourate language : ")
# vidhi = input("vidhi enter your favourate language : ")
# ani = input("ani enter your favourate language : ")

# s["Dhruv"]=dhruv
# s["Vidhi"]=vidhi
# s["Vidhi"]=ankita
# s["Ani"]=ani

# print(s)
