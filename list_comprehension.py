list1 = [1,4,5,7,2,9,0,87,3,4121,4345,56,23,87]

# list2 = []

# for i in list1 :
#     if i%2 == 0:
#         list2.append(i)

# print(list2)




#  using comprehension making list

list2 = [i for i in list1 if i <1000]
print(list2)

# for making set
s = {i for i in list2 if i%2 == 0}
print(s)