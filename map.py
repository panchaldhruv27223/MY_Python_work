def square(num):
    return num*num

l =[1,2,3]

# method - 1 

# l2 = []

# for item in l :
#     l2.append(square(item))

# print(l2)



# mehtod -2 

# print(map(square,l))
print(list(map(square,l)))