#DAY:8
'''
def profile(name,age,place):
    txt="my name is {}. i am {} years old. i am from{}."
    print(txt.format(name,age,place))
profile("sid","29","che")

#eg:4
#function with return statement

#return
#1.) A variable declared inside the function can be accessed outside the function
#using return
#2.) return does not prrint anything
#3.) we cannot write any code below return statement


def f1():
    c=a*b
    return c
print(f1(6,8))
obj  = f1(6,8)
obj1 = f1(4,6)

def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)

'''
#123
def palindrome(n):
    string =str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n,"Palindrome")
    else:
        print("not palindrome")
a=int(input("enter the value:"))
palindrome(a)
'''
#based on the declartion of parameter and args
#functions are divided into 5 categories

#Positional args
#keyword args
#default args
#variable length args
# keyword variable length args

# Positional args
#the position of parameter have to be same as position as agrements
def profile(name,phone,mark):
    txt ="My name is{}.My phone number is {}. I got {} marks."
    print(txt.format(name,phone,mark))
profile(8579568990,"Ramesh",95)

#keyword args
#eg:1
to overcome the disadvantage of position args,we use keyword args
it is the process of initialising the parmeter with the args while calling the 
#function
#def profile(name,phone,mark):
  #txt ="my name is{}. my phone number is {}.i got {} marks."
   #print(txt.format(name,phone,mark))

#profile(name="Usman",mark=100,phone=96668686)

#exception of keyword args function

def profile(name,phone,mark):
  txt ="my name is{}. my phone number is {}.i got {} marks."
  print(txt.format(name,phone,mark))   
#profile(name="Usman",mark=100)#error
#profile(5652289338 name='usman',marks=95)
profile('usman',mark=97,phone=6942522362)

#default args
#the method of assigning the argument to the parameter while declaring the function
#eg:1
def profile(name,phone,place='kadapa'):
    txt='my name is{}.my phone number is {}.i am from{}.'
    print(txt.format(name,phone,place))

profile("sid",78679475,"guntur")

#eg:1
name="sid",'name2','name3'
def profile(*name):
    for val in name:
        print("my name is",name)
profile("sid",'name2','name3')

#eg:2
def profile(age, *name):
    for val in name:
        print("my name is"val,"may age is",age)
profile(28,"sid",'name2','name3')


#keyword variable length args
#eg:1
def price(**price_list):
    print(price_list)

price(shirt=1000,iphone=8000)
d1={"a":100,"b":200,"c":300}
d1=dict(a=100,b=200,c=300)
print(d1)


#object oriented programming
#the paradigms of objects oriented programming are

#class
#objects
#inheritance
#polymorphism
#abstraction
#encapsulation
#class is a blue print of an object
l1=[1,2,3,4,5,6]

#eg:1
class c1:
    name1="sindhu"
    print(name1)

#eg:2
class person:
    name="sindhu"

c=person()
print(c.name)

#eg:3
#create of method
#when the function is created with a class is called as method

class person:
    def display(person):
        print("hello welcome to classes")

p=person()
p.dislay()


#eg:4
#method with parameter
class person:
    def display(person,name,age):
        print(name,age)
        

p=person()
p.dislay("sidhu",28)

#eg:5
class person:
    name3="sidhu" #attribute or static variable
    lname="T"

    def first_name(person):
        print(person.fname)

    def full_name(person):
        print(person.fname+""+person.lname)

p = person1()
p.first_name()
p.full_name()
'''

#! Eg:6
# constructors  -->__init__()
# This is a special method which has the ability to execute to itself without
# calling it manullay through the process of instantiation

class profile:
    def __init__(self): # constructor method
        print("hey")
p = profile() # throught this process
p.__init__()


















































































    


    

    

palindrome(a)
