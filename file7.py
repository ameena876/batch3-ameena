#DAY:7
'''
d1={'ten':10,'twenty':20,'thirty':30}
d2={'thirty':30,'fourty':40,'fifty':50}
d1.update(d2)
print(d1)

#
set1={'python','java','datascience'}
set2={'ML','AI','R Language', 'Python'}
set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
c=0
flag=0
for val in range(3):
    c=c+1
    if c==1:
        for val in set1:
            if val in set2 or val in set3:
                flag=1
                break
    if c==2:
         for val in set2:
             if val in set1 or val in set3:
                flag=1
                break

    if c==3:
         for val in set3:
            if val in set2 or val in set1:
                flag=1
                break
if flag==0:
    print("disjoint")
else:
    print("joint")

#3
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
l3=[]
for val in range(len(list1)):
    ans=list1[val]+list2[val]
    l3.append(ans)
print(l3)

#
#while loop:
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
i=0
while i<len(list1):
    l3.append(list1[i]+list2[i])
    i+=1
print(l3)

# ! Functions
DEF
# Function is a block of code which is used to perform a specific functionality
# Function can be created using def keyword


# ? Function has 3 parts
# Function declaration
# Function defination
# function call
'''

#eg:2

def greeting(name):
    print("welcome",name)
for val in range(3):
    username=input("enter the name:")
    greeting(username)

#eg:3
def profile(name,age,place):
    print(name,age,place)
profile("sid",29,"che")



















































































    





















































