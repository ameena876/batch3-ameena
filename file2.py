#Day2:
'''
a, b=c=7,8
print(a)
print(b)
prnt(a,b,c)
'''
#---->swaping of varibles
a=3
b=15
temp=a
a=b
b=temp
print(a,b)
#eg:1
'''
a=a+b#a=35
b=a/b#b=35/7=5.0
a=a/b#a=35/5=7.0
print(int(a),int(b))
id()--->used to find the memory address of the variable
a=7
b=8
print(id(a))
print(id(b))
#keywords
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

#literals
#literal is the constant value assigned to a variable
#A variable is considers to be constant when it is defines
#in caps

#a=78# ais variable
#A=78#A is constant
'''
#arithmetic operator
a=8
b=7
c=8
print(a-b-c)
'''
#floor division
a=580957
b=87456
print(a/b)
print(a/b)
#used for power of a number
print(8*16)
print(2**4)
a=8
a=-5
print(a)
a=30
a-=5
print(a)
#comparsion
a=8
b=4
print(a==b)
a=7
b=4
print(a&b)

#logical
a=6
print(a>3 and a<10)
print(not(a>8 and a<10))
#identify
#is is not
a=8
b=8
print(a is b)
print(a==b)
a=[1,2,3,]
b=[1,2.3]
print(a is not b)

#member ship operator
# in,not in
1=[3,11,15,20]
num=3
print(num in 11)
#conditional statement
#if,elif,else
eg:1
a=6
if a:
print("yes")
else:
print("no")
#eg:3
if 7>8:
print("hello")
'''
eg:4
a=0
a=None
a=False
a=""
if a:
    print("yes")
else:
    print("no")
'''
#a number ids even or odd
n=int(input("enter the number"))
if n%2==0:
    print(n,"is even")
else:
          print(n,"is odd")
'''
#name,age,nationality
name=(input("enter the name:"))
age=int(input("enter the age:"))
age=int(input("enter the nationallty indian:"))
if age> = 19 and nationality=="indian":
     print("eligible")
     else:
         print("not eligible")
 




