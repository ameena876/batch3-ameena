#eg:3
'''
length = int(input())
breadth = int(input())
if length==breadth:
    print("its a square")
else:
     print("its not square")
     '''
'''
#eg:4
n = int(input("enter the number:"))
if n%5==0 and n%7==0:
    print("yes")
else:
    print("no")
'''
#eg:5
'''
    cost Price (in Rs)                         Tax
    > 100000                                    15 % + discount 6%
    > 50000 and <= 100000                       10%
    < = 50000                                   5%
'''
'''
price = int(input("enter the price:"))
amount = 0
if price>=100000:
    discount = 100000*(6/100)
    value = price-discount
    amount=value*(15/100)
    print(value+amount)
else:
    tax = price*(5/100)
    total = price+tax
    print("the onroad cost of bike is total is:",total)
# if elif else:
a=7
b=9
c=30

if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
elif c>a and c>b:
   print("C is greater")
'''
#eg:6
'''
A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.
mark = int(input("enter mark:"))
if mark>=80 and mark<=100:
    print("A")
elif mark>=60 and mark<=80:
    print("B")
elif mark>=50 and mark<=60:
    print("C")
elif mark>=45 and mark<=50:
    print("D")
else:
    print("fail")
# using short hand if else
* rules
1.)statement inside the if condition have to be present at first
2.)elif cannot be used in short hand if else
3.)always it have to end with else
'''
'''
a=90
b=80
print("A") if a>b else print("B")

#code to check the given char is vowel or consent
char = input("enter the char:")
if char=="a" or char =='e' or char =='i' or char =='o' or char =='u':
    print("is a vowel")
else:
    print("its consonent")

#shorthand if else
char = input("enter the char:")
str1 ="aeiouAEIOU"
print("vowels")if char in str1 else print("consoent")

#elif ladder using short hand if else
#eg:1
a=8
b=5
c=9
print("a is greater")if a>b and a>c else print("b is greater")if b>a and b>c else print("c is greater")

#---------> looping
#looping can be implemented using
#for loop
#while loop
#for loop:
#for loop is use for iteration,if we know the number of times the loop have to run
#it is used to iterate the iterables eg(string,list,tuple,etc...)

#for syntax in python
#for userdefine_variable in range(start,end,step):default step value is 1
#statement
#statement
#statement

#eg:1
# To print the value from 1 to 10 using for loop

for i in range(0,10):#(n,n-1)
   # print(i)
   print("hello")

#eg:2
for val in range(1,15,2):
    print(val)
#3
for val in range(1,15,3):
    print(val)

#eg:3
#to decrement the value
for val in range(1,10,-1):
    print(val)
for val in range(10,0,-2):
    print(val)
for val in range(10,0,1):
    print(val)#no output

#eg:4
#print the outut of 7th multiplication table from 21 to 43
method:1
for val in range(1,10+1):
    print('7','x',val,'=',val*7) 
method:2
ans="7 x {} = {}"
print(ans.format(val, val*7))
method:3
print(f"7 x {val}={val*7}")
#eg:5
#break statement
for val in range(1,10):
    if val ==6:
        break
    print(val)
#1
    for val in range(1,10):
        print(val)
            if val ==6:
            continue
        print(val)

for val in range(1,30):
    if val ==6 or val ==8 or val ==21:
        continue
    print(val)
#practise problrems
#print the even number between 20 to 40
for val in range(20,40+1,2):
    print(val)
#1
for val in range (20,41):
    if val %2==0:
        print(val)
#1
for val in range(20,41):
    if val %2==0:
        print(val)
#while loop:
# while loop is used with number of times the loop have to run
# to iterate the non iterable the elements while loop is ussed
#syntax of while loop
#initialisation
#while condition:
statement
increment or decrement
'''
#EG:1
# to iterate number from 1 to 10
i=0
while i<11:
    print(i)
    i=i+1
#EG:1




















