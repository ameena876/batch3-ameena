#day:4
#whileloop
#break using while loop
#iterate from 20 to 30 and break the loop in 27
'''
i = 20
while i<31:
    if i ==27:
        break
    print(i)
    i+=1

i = 20
while i<31:
    if i ==27:
        break

    
i = 27
while i<31:
    print(i)
    if i ==27:
        continue
        break

#while to iterate from 12 to 22
i = 12
while i<23:
    print(i)
    i+=1
    sum 0
    sum=sum+i
     print(sum)
     i+=1
#find the sum of all numbers
i = 12
while i<23:
    sum 0
    sum=sum+i
     print(sum)
     i+=1

#1
i = 12
 sum=0
while i<23:
    sum=sum+i
     i+=1

#find the average of value from 20 to 25
i=20
sum=0
count=0
while i<30:
    sum=sum+i
    count+=1
    i+=1
print(sum/count)
#NESTED FOR LOOP
#eg:1
for i in range(1, 3+1):
    for j in  range(1, 4+1):
        print(i, j)

#eg:2
for i in range(4):
    for j in  range(4):
        print("*", end="") 
    print()
#eg:4
for row in range(5):
    for col in range(5):
        print(row, end=" ")
  print()

#to print stars in right angled triangle

#5
sum=0
for  row in range(5):
    for col in range(5):
        sum= sum+1
        print(sum, end=" ")
    print()
#to print stars in right angle triangle
sum = 0
for row in range(0,6):
    for col in range(0,row+1):
        print("*",end=" ")
    print()

for row in range(5):
    for col in range(5):
         if col==0 or col==5-1 or row ==0 or row ==5-1:
             print("*", end=" ")
         else:
             print(" ", end=" ")
    print()

for row in range(0,5):
    for col in range(0,6):
        if (row==0 and col==3) or (row==1 and(col>=2 and col<=4)or(row==2 and (col>=1 and col<=5))):
                                
             print("*", end=" ")
        else:
             print(" ", end=" ")
    print()
#LIST
#DATA TYPES
#PRIMARY
#NUMBER
#STRING
#BOOLEAN
#NONE
#COLLECTION
#LIST
#TUPLE
#SET
#DICTONARY
# 1.) if the collection of elements are surrounded by Square brackets, it is considered to be list.
# ! ---> Eg:
# l1 = [4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]
    
# Characteristics of list
# 1.) List have to be surrounded []
# 2.) It is mutable (the elements in the list are changable)
# 3.) Every elements inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous
#to access yhe elements in the list
l1=[1,4,1,7,89.7,7,5,"p","i"]
print(11)
#indexing:
# In the collection datatypes like list, tuple, string, the elements will be alloted
# with predefined unique value called index value

# We have 2 types of indexing
# Positive indexing --> starts with @ from left hand side
# Negative indexing --> starts with -1 from right hand side

#positive indexng
print(l1[4])

# ---->Negative indexing
#lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
#print(lst1[-1])
#print(lst1[-5])

# ? ----> slicing
# lst1[start_index:end_index:step]
'''
lst1 = [1,2,3,4,56,34,"p","i",]
print(lst1[-7:-1:2])
#! To insert ot add element inside list
# append()-> used to add elelement at last position of list
# 11 [9, 8, 0, 6]
# 11.append("car")
#print(11)





































    







     
