#DAY:5
'''
# COMMOM FUNCTION FOR LIST
l1=[6,7,8,9]
print(len(l1))
print(max(l1))
print(min(l1))
#l[6,8,9,"p","u"]
#print(max(l1))---> error coz its a combination of int and string
#print(min(l1))---> error coz its a combination of int and string
l1=[6, 7, 8, 9, 0, 8.89, -5, 0.78]
#index() --> to get index value of specific element
print(l1.count(6))

#some functions which is specifically used for list
#to add element inside the list
#insert(index_value,element) --> to add element at spcific index position
l1=[6,6,6, 7, 8, 9, 0, 8.89, -5, 0.78]
l1.insert(2,"cars")
print(l1)

#remove(element)--->used to delete element directly
l1=[6,7,8,9,0,3.5,8.89,-5]
l1.remove(7)
print(l1)
#remove(element)--->used to delete all element directly
l1=[6,7,8,9,0,3.5,8.89,-5]
l1.remove(7)
print(l1)

#del--->to delete the list
l1=[6,7,8,9,0,3.5,8.89,-5]
del l1
prnt(l1)

l1=[4,5,6]
l2=[7,8,9]
print(l1+l2)
#or
#extend () --->to combine 2 lists
l1.extend(l2)
print(l1)

# ? ---> copy()
# l1 = [6,7,8,9,0,3.5,8.89,-5]
# l2 = l1.copy()
# print(l2)
# print(l1)

# print(id(l1))
# print(id(l2))

# * deep copy ---> used to copy the list with nested list
#import copy
l1=[8,9,0,[5,6],[3,2,1]]
l2=copy.copy(l1)
#l1.append(209)
#print(l1)
#print(l2)

# M:-2 --> descending order

l1 = [9,7,2,3,5,23,63,32]
l1.sort(reverse=True)
print(l1)

#list constructor
l3=((8,9,0))
print(list(l3))
l4 = (8, 9)
print(list(l4))


# ! ---> nested list

l1 = [8, 9, [0, 8, 7],['p', 'o', 'y'],[8,'t']]
print(11[-2][1])



# to delete "t" from l1
l1 = [8, 9, [0, 8, 7],['p', 'o', 'y'],[8,'t']]
l1[-1].remove('t')
print(l1)

#combine these ["p","o",'y'],[8,'t'] lists in l1 to["p","o",'y',8,'t']
l1[-2].extend(l1[-1])
l1.pop(-1)
print(l1)

# ! ----> Tuple

#1.) tuple have to be surrounded by ()
#2.) The element inside tuple are not changable
#3.) The element inside tuple are indexed
#4.) The element will excuted in order
#5.) It is heterogenous
#6.) It allow duplicate element

#eg:
t1=(8,8,9,6,5.78,[9,0],(6,8),"hey",9+6j)
print(t1)
print(type(t1))

#indexcing,slicing are all same as list
l1 =(8)
print(type(11))#tuple

#2.
t1 = 8,9
print(type(t1))#tuple

#3.
t2 = 8
print(type(t2))#tuple

#len(),min(),max(),index(),count()-->all Same as list

#to add element inside tuple--> cannot add
#cannot delete any element from tuple

# * join  2 tuples
t1 =(1,2,3)
t2 =(4,5,6) 
print(t1+t2)

# To add all element inside list and tuple
sum()
l1 = (8, 9, 7, 6)
print(sum(l1))

#sort tuple
t1 =(8,9,0,89,12)
print(tuple(sorted(t1)))
print(tuple(sorted(t1, reverse=True)))

# *iterate list and tuples
#iterate based on elements
l1 =[9,8,0,6,5]
for i in l1:
    print(i)

# * iterate based on index value
l1 =[9,8,0,6,5]
for i in range(0,len(l1)):
     print(l1[i])


#string
s1 ="o"
print(type(s1))
s1 ="u"
print(type(s1))

s1 ="hello world"
print(type(s1))

s1 ="hello world"
print(s1[0:5]

#common function

len(),min(),max(),index(),count()
s1 ="hello world"
      print(len(s1))
      print(min(s1))
      print(min(s1))

#ord()---> used to find the ASCII value of a character
      s1 = 'u'
print(ord(s1))
     

#functions string
s1="hello world"
#to convert all charcters to uppercase
#strip()--->to eliminate the space in beginning and end of string
s1=" sodium"
print(s1.lstrip())


# --> strip()
# --> to eliminating the space in beginnning and end of string
# M:-1
# --> to eliminate left space
'
s1 = "   where are you.?"
print(s1.lstrip())

# M:-2
# --> to eliminate right space

s1 = "where are you.?  "
print(s1.rstrip())

# M:-3
# --> to eliminate right and left space

s1 = "   where are you.?    "
print(s1.strip())


# ---> split()-->
# --> to split the words in string based on a character
s1= "where are you.?"
print(s1.split(" "))
# replace() --> to replace a specific char in the string

s1= "where are you.?"
print(s1.replace('r','&&'))


# swapace() --> to convert capital to small and small to capital at a time

s1 = "HEY there"
print(s1.swapcase())

# join the strings

s1 = "hello"
s2 = "world"
print(s1+s2)

s1="where is maneesha "
s2="nenu ameena"
s3="nenu  afrin ne manesha friend"
print(s1+s2+s3)


# Swapcase()---> to convert capital to small and small to capital

s1="HEY there"
print(s1.swapcase())


# Title() --> to write the string in format of title
s1='never giveUP'
print(s1.title())  # --> Never Giveup


# Capitalize() ---> 1st char of string will be converted to capital

s1='never giveUP'
print(s1.capitalize())

# Join the strings
s1 = "hello"
s2 = 'world'
print(s1+s2)
'
#s1 = "hello world"
#print(s1.find('z'))
#print(s1.index('z'))


# * join() -->
l1 = ["hey" ,"there"]
print(" ".join(l1))

# * join() -->
l1 = ["hey" ,"there"]
print(" ".join(l1))
print("$".join(l1))

s1 = "welcome to all"
print(s1.endswith('1'))
print(s1.startswith('w'))

s1 = "67"
print(type(s1))
print(s1.isdigit())



s1 = "welcome to all"
print(s1.endswitch('1'))
print(s1.startswitch('w'))

s1 = "67"
print(type(s1))
print(s1.isdigit())


# * print the string in reverse manner
s1 = "Welcome to all"
print(s1.endswith('L'))

s1 = "Welcome to all"
print(s1[::-1])

#eg:1
#wap  to find the number of lower case letters
s1 ="hey there you are"
count = 0
for i in s1:
     if i.islower():
          count+=1
print ("the total num of lower case letters:",count)

'''
#eg:2
s1 = 'restarter'
s1 = "imagin"


print(s1.replace('r',"$"))
s1="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"
characters=len(s1)
print(characters)

words = s1.split("")
print(len(words))
sentenses=s1.split(".")
for val in sentenses:
    if val =='':
        index = sentences.index('')
        sentences.pop(index)
print(len(sentences))
















