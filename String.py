# a=34
# b=" dhruv's "
# c=' dhruv"s '
# D =''' hey 'dhruv' "panchal" 
# you are so good in eyerything '''
# print(a)
# print(b)
# print(c)
# print(D)  

# ''               ""        ''' '''


name = "dhruv panchal"
greeting ="good morning"
# print(name)
# print(type(name))
# print(greeting + name)
print(greeting , name )

# concatenating of two string 
# c = greeting + name 
# print(c)


#  string are arrays 

# print(name[2])
# print(name[4])

#  we can not change 
# name[4]="d"

# slysing
# name = " dhruv panchal"
# print(name[1:4])
# print(name[:4]) # start from first 
# print(name[2:]) # end from last index 
#       start from 1 to 3 (4 is not countable) for [1:4] 

#  negative indexing   index start from last potison    ( -5 -4 -3 -2 -1 )

# name = " dhruv panchal"
# print(name[-3:-1])
# print(name[-3:])


#   for skiping 

# name = " dhruvpanchal"
# print(name[0::1])
# print(name[0:5:2])
# print(name[0::3])


story = '''once upon a time there was a movie which is a favourate of dhruv panchal upon'''

# print(len(story))




# print(story.upper())
# print(story.lower())
# a.strip()    --  remove whitespace



#        split()       split a string in every part in array 

a = "hello , Dhruv , Panchal"
print(a.split())
print(a.split(","))


# a.replace()





# print(story.endswith("panchal"))

# print(story.capitalize())

# print(story.count("o"))

# print(story.find('dhruv'))
# print(story.find("code"))           #-1 if not found otherwise it return a integer number or index number 

# print(story.index("dhruv"))
# print(story.index("code"))          # if not found get error 

# print(story.replace("dhruv" , "code with dhruv"))

# print(story.count("upon"))

# escapseqvance 
# \n  \t  \\  \' 

# story = "hey \n\tdhruv panchal \n\tgood \\  \' morning "
# print(story)

# problems

# name = input("enter your name :")
# print("good afternoon " + name )

# name = input("enter your name :")
# date = input("enter a date :")
# letter = '''\ndear |<name>| 
# greeting from abc coding house , i am happy tell about your selection 
# ypu are selected !
# have a great day ahead
# thanks and regared 
# Bharat.
# DATE : |<date>|'''
# letter = letter.replace("|<name>|",name)
# letter = letter.replace("|<date>|",date)
# print(letter)


# st ="this is a code for  detecting dounble    space."
# doublespace= st.find("  ")
# doublespace=st.replace("  "," ")
# print(doublespace)
# letter ='''Dear Dhruv Panchal you are a nice person thanks!'''
# print(letter)
# formated_letter ='''Dear Dhruv Panchal , \n\t\tyou are a nice person \n\t\tthanks.'''
# print(formated_letter)















#   

a = "hello Dhruv Panchal"

print(len(a))

print("Dhruv" in a)

#  we can use this two     in or     not in   we get ans in true false means in boolean

if "Panchal" in a :
    print("welcome welocme !!!")



d = 18
name = "my name is dhruv panchal and my age is :" 
print( name + str(d) )


c = 24 

name = "my name is dhruv panchal and my age is : {}  {}" 
print(name.format(d,c))






# escape = '''hey it's Dhruv Panchal "woooww"  your are a coder'''
# print(escape)



y = 2000


print(isinstance(y,int))