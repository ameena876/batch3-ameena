#DAY:10
'''
#method riding
#ploymorphism in classes
#eg:1
class bank:
    def ratio(self):
        print('all banks has repo rate')
class SBI(bank):
    def ratio(self):
        print("SBI rate is 90%")
class IOB(bank):
    def ratio(self):
        print("SBI rate is 90%")
i=IOB
i.ratio()

s=SBI
s.ratio
#eg:2
class USA:
    def language(self):
        print("english")
        
    def capital(self):
        print("washington dc")

class India(USA):
    def language(self):
        print("none")
        
    def capital(self):
        print("newdelhi")
I=India()
I.language()
I.capital()

#eg:3
class c1:
    def f1(self):
        print('class 1')

class c2:
    def f1(self):
        super().f1()
        print('class 2')
obj=c2()
obj1.f1()

#eg:4
class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        print("calss 2")

obj1 = c2()
obj2 = c1()

def display(a):
    a.f1()
display(obj1)
display(obj2)

#changing the functionality of builtin functions
a=15
b=3
print(a.__add__(b))#dunder method magic method
#
a=15
b=3
int()
print(a.__sub__(b)

#changing the functionality of builtin functions
class shooping:
    def __init__(self,l1):
        self.items =l1


#method over loading
#eg:1
class suming:
    def add(slf,a,b):
        print(a+b)

    def add(self,a,b,c):
        print(a+b+c)

s=suming()
s.add(4,3)
s.add(4,5,1)


#eg:2
class summing:
    def add(self, a=none, b=none, c=none):
        if a!=none and b!=none and c!=none:
            print(a+b+c)

        elif a!=none and b!=none:
            print(a+b)
        else:
            print(a)
obj=summing()
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)

#ABSTRACTION
# the process of hiding the implementation details is abstraction
class shapes:
    def sides(self):
        print('All shapes have sides except circle')

class triangle(shapes):
    def triangle_sides(self):
        print("3 sides")
    def name(self):
        print("i am triangle")
class square(shapes):
    def square(self):
        print("4 sides")
    def sides(self):
        pass
tr = triangle()
tr.triangle_sides()
tr.name()


# ! Rules to define abstract class 1
#1.) Abstract class cannot be instantiated
#2.) From abc import ABC, abstractmethod
#3.) subclass the normal class with ABC
#4.) Convert the normal method inside the abstract class to abstract method
#5.) All the child classes have to be subclassed with abstract class
#6.) The abstract method should be present in the child classes
#eg:2
from abc import ABC,abstractmethod
class c1(ABC):
    @abstractmethod

#eg:3
from abc import ABC,abstractmethod
class password(ABC):
     @abstractmethod
     def pwd(self):
         pswd="siddi994$"
         return pswd
        
class login(password):
     def validate(self,name,passwrd):
         if super().pwd() == password:
            print("welcome", name, '!!')
            print("Login Sucessful")
         else:
            print("Please check the password")

     def pwd(self):
        pass


Login = login()
name = input("Enter the name: ")
pwd = input("enter the password: ")
Login.validate(name, pwd)

#eg:1
class car:
    __name ="BMW"
    private(__name)
c1=car()
print(c1.name)
c1.name="Audi"
print(c1.name)

#accessing private date outside the class
class c1:
    __phone='9956234621'


    def display(self):
        print(self.__phone)

c=c1()
c.display()

#eg:3
#declare private method
class class1:
    def m1(self):
        print("i am private method")

c=class1()
c.__m1()


#nested class
class class1:
    class class2:
        name="sindhu"

        def display(self):
            print(self.name)
    obj1=class2()

obj=class1()
obj.obj1.display()
'''

d1 = {"shirt":1000, "pant":1500, "Shoes":900, "hudi":30}
for val in d1:
    if d1[val] == min(d1.values()):
        print(val)
for val in d1:
    if d1[val] == max(d1.values()):
        print(val)
for val in d1:
    if val.startswith('s') or val.startswith('S'):
        print(val)















    
    



















        




























