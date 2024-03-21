#DAY:9
'''
#find the uncommon words from 2 strings
s1="hello how are you"
s2="hello how is"
s1=s1.split(" ")
s2=s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)

#find the 8th fibonochi number
num=8
n1=0
n2=1

for val in range(num):
    ans=n1+n2
    n1=n2
    n2=ans
print(ans)


#constructors
#eg:2
#unparameterised constructor
class profile:
    def __init__(self):
        print("hello world")
obj=profile()
obj.__init__()#if we call the function it will print 2 times
#eg:3
#parametarised constructor
class profile:
    def __init__(self,id,name,age):
        print(id, name, age)

obj = profile(12,"sid",29)

#eg:4
class c1:
    name="sid"
    place="cbe"

    def m1(self):
        print()
object=c1()
object.m1()

#eg:5
class c1:
    def m1(self):
        age=28

    def display(self):
        print(name,age)
        print(self.name,self.age)
    
object=c1()
object.display()

#eg:6
class class1:
    def __init__(self):
        self.name="sid"
        self.email="sid@gmail.com"


    def display(self):
        print(self.name,self.email)


c1=class1()
c1.display()

#inheritance:
#the process of utilising the methods and attributes of parent class
#throught the object of child class it is called s inheritance
#5 types of inheritance
#single inheritance
#multilevel inheritance
#multiple inheritance
#hybrid inheritance
#herachical inheritance

#1. single inheritance
#it has only one parent class and only one chid class
#eg:1
class parent:
    def m1(self):
        print("i am parent class")


class child(parent):
    def m2(self):
        print("i am child class")


obj=child()
obj.m1()

#eg:2
class c1:
    def __init__(self):
        print("i am constructor from parent class")

class child1(c1):
    pass

obj=child1()

#eg:3
class parent:
    name ="sidhu"

class child (parent):
    name="name1"

    print(self.name)
d=child()
d.display()

#multilevel inheritance
class voice:
    def sound(self):
        print("All the animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")
        
class cat(dog):
    def cat_voice(self):
        print("Meow")
        
class parrot(cat):
    def dog_voice(self):
        print("speak")

all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()


class honda_city:
    def engine_specs(self, cc, Hp, torque, fuel_type,num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)

    def honda_city_body_specs(self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)
class amaze(honda_city):
    def engine_specs(self, cc, Hp, torque, fuel_type,num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)

def amaze_body_specs(self, color, weight, height, length)



# Multiple Inheritance
 #? It has multiple parent and 1 child
class while_pertol:
    def function_w(self):
        print("used to Airplans")

class Organic_petrol:
    def function_o(self):
        print("used for Bike, cars")
class premium_petrol:
    def function_p(self):
        print("spots cars, bikes")
class petrol(while_pertol, Organic_petrol, premium_petrol):
    def defanition(self):
        print("Petrols types")
p=petrol()
p.defanition()
p.function_o()


# hybrid Inheritance
 # The combination of above 4 inheritance is called Hybrid inheritance
class c1:
    def m1(self):
        print("Class1")
class c2:
    def m2(self):
        print("class2")
class c3:
    def m3(self):
        print("Class 3")
class c4:
    def m4(self):
        print("Class 4")
class c5:
    def m5(self):
        print("Class 5")
class c6:
    def m6(self):
        print("Class 6")



# * Polymorphism in builtin functions
# len() --> which is used to find the length of list, tuple, dict etc...
# index()
# max()
# min()
# count()
# pop()
# and more...
'''
#+
print(8+8)
print("k"+'1')
print([1,2,3]+[5,6])

#*
print(6*7)
l1={1,2,3,4,5,6}
print(*l1)
def f1(*args):
l1=[1,2,3,4]
print(l1*10)











































        














































