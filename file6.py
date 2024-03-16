#DAY:6
#python Program to capitalize the first and last character of each
#word in a string
'''
s1=input("enter string")
fst=s1[0].upper()
lst=s1[-1].upper()
print(fst+s1[1:len(s1)-1]+lst)

#2.
n=128
temp=n
f1=0
while n!=0:
      rem=n%10
      check=temp%rem
      if check!=0:
        f1 = 1
        n=n//10
        
      if f1==0:
            print("yes")
     else:
        print("no")

#3.
l1=[1,3,15,28]
l2=[7,8,5,45]
l3=[]
for val in range(len(l1)):
    ans=l1[val]+l2[val]
    l3.append(ans)
    print(l3)

l1 = [8, 9, 0, 7]
l2 = [7, 6, 5, 4]

#print(l1[0]+l2[0], l1[1]+l2[1])
l3 = []
for val in range(len(l1)):
    ans = l1[val]+l2[val]
    l3.append(ans)
print(l3)


# ! -----> set
# characteristics of set
#1.) set can be created using{}
#2.) The element inside set are not indexed
#3.) Does not allow duplicate values
#4.) it unordered
#5.) heterogenous
#6.) mutable or changable
# ! -----> set

#eg:1
s1 ={9,9,89,7.76,8+7j,(8,7,5),"truck",'e'}
print(s1)
#eg:2
#error coz accept only unmutable data types
s2={5,8,98,[3,15],}
print(s2)


#eg:3
#min(),max(),len()

#eg:
#to add element inside set
s1={8,78,67,'u'}
s1.add(43)
print(s1)
s1.update(9,0)
print(s1)

#to delete element inside the set
#pop--->to delete one element randomly
s1={8,78,67,'u'}
s1.pop()
print(s1)
#remove
s1.remove(78)
print(s1)


discard()
s1.discard(67)
print(s1)

# clear()
l1 = {}
print(type(l1))
s1 = set() # to create empty set
print(type(s1))
s1 = {8,9,0}
s1.clear()
print(s1)

#
s1={8,9,0}
s2={6,7,5,8,9,0}
print(s1.issubset(s2))
print(s2.issubset(s1))

#o/p--->its a joinset
s1={1,2,3,4,5}
s2={3,2,7,8,9}
for val in s2:
    str1="its joint set"
print(str1)
#---->dictionary
#eg:1
d1={1:100,'a':200,5.4:"hello"}
print(d1)



 ? dictionary  based function
# to add element(key and value pair) in dict
d1 = {1:100, 2:200, 3:300, 4:400}
d1[5] = 500
print(d1)

d1 = {1:100, 2:200, 3:300,4:400}
d1[2]="mango"
print(d1)




# 1.
n=int(input("enter num of times :"))
integer=[]
float_value=[]
string=[]


for val in range(n):
    value=eval(input("enter the values:"))
    if type(value)==int:
        integer.append(value)
    elif type(value) == float:
        float_value.append(value)
    elif type(value) ==str:
        string.append(value)
    else:
        print("Pls provide data in int, float, string")
print(integer)
print(float_value)
print(string)
'''
# Return a set of elements present in Set A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set()
for val in set1:
    if val not in set2:
        set3.add(val)
for val in set2:
    if val not in set1:
        set3.add(val)
print(set3)


#! ---> problem 3
l1=[1,2,3,4] # key
l2=["a","b","c","d"]  # value
l3=(l1[0],l2[0]or l1[1],l2[1] or l1[2],l2[2]or l1[3],l2[3])
print(l3)

#!------> problem 3
l1=[1,2,3,4] # key
l2=["a", "b", "c", "d"] # value

#{1:'a'}
d1 = {}
for val in range(len(l1)):
    d1[l1[val]]=l2[val]
print(d1)








































    

