
'''Programs Create two class first parent class and second child class and do single level 
inheritance, use init
and super function. create two method in first class and create one method in second class. 
Do any
calculation in first method and in second class method.'''



'''x = np.array([[1,2,3,4,5]])


print(type(x))
print(x.ndim)   #it represents the length of the array. means numbers of square brackets.
print(x.dtype)
print(x.size)'''


'''x = np.array([[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]]])
#print(type(x))
#print(x.ndim)
#print(x)
print(x[0][0][0][0])
print(x[0][0][2][1:4])'''



'''
x = np.array([[[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]]]])

find the type, dimenstion,print this array, size of this array, and extract these values
of this array.

extract theses values:

return 7, 12, 18, 1, 20, 3 
return 7 to 10
return 12 to 13
reverse this array [16,17,18,19,20]
return 6 to 10 
return 2 to 3

print each array seprately'''









x = "Arunachal Predesh"
#print(x[2])
#print(x[-15])
#print(x[4])
#print(x[-13])
#print(x[2:6])
#print(x[-15:-11])
#print(b[2:5])

'''x = "Arunachal Predesh"
Return P
return sixth item 
return thrteenth item 
return fourth item
return eight item
return third to fifth item
return second to last item
return second last to first item
return fifth to eight item'''

'''a = " Good morning "
print(a)
print(a.strip())'''    # returns "Good morning" 


'''a = "Arunachal Pradesh"
#print(a.replace("a", "b"))
print(a.replace("a", "@"))'''


'''x= "Good Morning India"
print("Good morning\nIndia")'''      



'''x= "Good Morning India"
print("Good morning\t India")'''

'''x = "Good \bmorning India" 
print(x) '''


'''x = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday","dff","ggh")
y = list(x)

y[1:4] = ("January",)
#print(y)
x = tuple(y)
print(x)
print(type(x))'''


'''x = ("sunday", "monday", "tuesday")

(jan,feb,march) = x

print(jan)
print(feb)
print(march)
print(march)
print(feb)
print(march)'''


'''x = ("sunday", "monday", "tuesday")

(a,b,c) = x

print(a)
print(c)
print(a)'''


'''n = int(input("input the number: "))
i=2

if n<2:
  print("Number is not prime")
elif n==2:
  print("Number is the prime number")
else:
  while i<n:
    if n%i==0:
      print("Not a Prime Number")
      break
    i+=1
  else:
    print("Number is Prime")'''


'''Check number is prime or not

what is prime number.
prime numbers are natural numbers ex: 1,2,3,4,5,6.
0 is not a prime number.
1 is not a prime number
prime number is, which can divide by one and itself. They have no other factors.
for example: 11 is prime number.
if put 11 so I just want to check 2 to 10 numbers.
n%i==0 we have to check its divisible or not.

Find the n number of even numbers'''

'''x = int(input("Enter a number: "))
z = 0
y = 0
while z < x:
   y+=1
   if y%2==0:
      print(y)
      z+=1'''


'''x = ["sun","Mon","Tues","wed","Thurs","Friday","Sat"]
for z in x:
  print(z)'''

'''x = "Hello Delhi"
for i in x:
  print(i)'''

'''for i in "Hello Delhi":
  print(i,end=" ")'''


'''days = ["sun","Mon","Tues","wed","Thurs","Friday","Sat"]
for i in days:
  if i == "wed":
    break
  print(i)'''

'''for x in range(10):
  print(x)'''


'''for x in range(1,11):
  print(x)'''

'''for x in range(1,11,2):
  print(x)'''

'''for x in range(2,22,2):
  print(x)'''

'''x = int(input("Enter a number: "))
z = 0
y = 0
while z < x:
   y+=1
   if y%2==0:
      print(y)
      z+=1'''

'''for i in range(10):
  print(i)'''

'''for i in range(2,10):
  print(i)'''

'''for i in range(2,10,2):
  print(i)'''


'''for i in range(2,22,2):
  print(i)'''

'''x = int(input("Enter the number: "))
y=0
for i in range(x):
  y+=1
  if y%2==0:
    print(y)'''

'''x = int(input("Enter the number: "))
y=0
for i in range(x):
  y+=1
  if y%2==0:
    print(y)'''


'''x = int(input("Enter a number: "))
z = 0
y = 0
while z < x:
   y+=1
   if y%2==0:
      print(y)
      z+=1'''


'''days = ["sun","mon","tues","wed"]
months = ["Jan","Feb","March","April","may"]

for i in days:
  for y in months:
    print(i,y)


*
* *
* * *
* * * *
* * * * *'''

'''x = int(input("Enter a number: "))
for i in range(x):
  for y in range(i):
    print("*",end=" ")
  print()

1
1 1
1 1 1
1 1 1 1
1 1 1 1 1
1 1 1 1 1 1


1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6'''



'''i = 1
while i < 10:
  if i == 8:
    break
  print(i)
  i += 1

print counting 1 t0 20 and it should stop on 15.'''



'''i = 1
while i < 11:
  print(i)
  i += 1
else:
  print("1 to ten counting is completed now")'''


'''Find the even number and the sum of n number of even number

x = int(input("Enter a number: "))
z = 0
y = 0
c = 0
while z < x:
   y+=1
   if y%2==0:
      print(y)
      z+=1
      c+=y
print("sum of n even numbers:", c)'''



'''x = ["sun","Mon","Tues","wed","Thurs","Friday","Sat"]
for i in x:
  print(i)'''


'''x = "Hello Delhi"
for i in x:
  print(i)
'''

 
'''for i in "Hello Delhi":
  print(i)
'''


'''for i in "Hello Delhi":
  print(i,end=" ")
'''

'''x = int(input("enter a number: "))
for i in range(x,0,-1):
  #print(i)
  for y in range(i):
    print("*",end=" ")
  print()'''


'''a = """Honesty is the best policy
    we are indians, Now we are learning data 
    analytics course
    from madrid institute"""

print(a)

print this string with the help of for loop and while loop:

x = "Arunachal Predesh"'''


'''x = ["sun","Mon","Tues","wed","Thurs","Friday","Sat"]
for i in x:
  print(i)'''

'''x = "banana"
for i in x:
  print(i)'''

'''for i in "banana":
  print(i,end=" ")'''


'''for i in range(10):
  print(i)'''

'''for i in range(1,11):
  print(i)'''

'''for i in range(1,11,2):
  print(i)'''

'''for i in range(2,22,2):
  print(i)'''

#print 1 to 50 with the help of for loop and then reverse this counting.

'''find 10 even numbers
find 10 odd numbers
Find the factorial of any number:
find the sum of 10 even numbers
find the sum of 10 odd numbers
print a table with the help of user input'''

'''find the sum of n natural numbers
Take user input and print any random number of even number or any random number of odd number
and finally show the sum of these even numbers and odd numbers.'''

'''for i in range(2,22,2):
  print(i)'''

'''x = int(input("Enter a number: "))
z = 0
y = 0
while z < x:
   y+=1
   if y%2==0:
      print(y)
      z+=1
      #print(z)'''


'''x = int(input("Enter a number: "))
for i in range (1,x+1):
  if i%2==0:
    print(i)'''


'''x = int(input("Enter a number: "))
for i in range (1,x*2+1):
  if i%2==0:
    print(i)'''


'''x = int(input("Enter a number: "))
for i in range(0,x*2,2):
  print(i)'''



'''x = "Honesty is the best policy"
print("best" not in x)'''

'''x = "Honesty is the best policy"
if "best" not in x:

  print("Yes, 'best' is present.")

else:
  print("This is not true")'''


#import numpy as np
'''class Parent_1:
  def __init__(self,a,b):
    self.a = a
    self.b = b
    self.z = a+b
class Parent_2:
  def x2(self,m,n):
    self.m = m
    self.n = n
    self.t = m**n
class Child(Parent_1,Parent_2):
  def __init__(self,a,b,m,n,u,v):
    super(). __init__(a,b)
    super(). x2(m,n)
    self.u = u 
    self.v = v
    self.k = u/v 
ob = Child(6,12,3,4,6,3)
print(ob.z)
print(ob.t)
print(ob.k)'''


'''class Parent_1:
  def __init__(self,a,b):
    self.a = a
    self.b = b
    self.z = a+b
class Parent_2:
  def __init__(self,m,n):
    self.m = m
    self.n = n
    self.t = m**n
class Child(Parent_1,Parent_2):
  def __init__(self,a,b,m,n,u,v):
    Parent_1. __init__(self,a,b)
    Parent_2. __init__(self,m,n)
    self.u = u 
    self.v = v
    self.k = u/v 
ob = Child(6,12,3,4,6,3)
print(ob.z)
print(ob.t)
print(ob.k)'''

#import numpy as np

'''x = np.array([[[1,2,3,4,5]]])


print(type(x))
print(x.ndim)   #it represents the length of the array. means numbers of square brackets.
print(x.dtype)
print(x.size)'''


'''x = np.array([[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]]])
#print(type(x))
#print(x.ndim)
#print(x)
#print(x[0][0][1][0])
print(x[0][0][2][1])
#print(x[0][0][0][0])

extract 8, 13,1'''



#create three arrays wtih the help of arange method.

'''x = np.arange(6)
print(x)'''

'''x = np.arange(2,10)
print(x)'''

'''x = np.arange(1,10,2)
print(x)'''

'''y = np.arange(10,20)
print(y)'''

'''x = np.array ([1,2,3,4,5])
print(x)'''

'''x = np.array ([[1,2,3,4,5],[6,7,8,9,10]])
print(x[0])
print(x)'''


'''x= np.zeros(6)
print(x)'''
#print(type(x))

'''x= np.ones(7)
print(x)'''

'''x = np.ones(3)
print(x)
print(type(x))'''


'''x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])

z =  np.concatenate((x,y))
print(z)'''

'''x = np. array ([2,1,5,3,7,8])
y=np.sort(x)
print(y)'''

'''create two arrays with the help of zeros and ones method and concatenate it.

create two arrays with the help of arange method and concatenate it and then do sort
of this array'''

'''x = np.full(5,6)
print(x)'''

'''x = np. array ([2,1,5,4.0])
print(x)


print(x[1].dtype)'''



'''x = np. array ([2,1,5,4.0,8J])
print(x)
print(x[1].dtype)'''

'''x = np. array ([["abc",1,5,4],["xyz",5,6,9]],ndmin=6)
print(x)'''


'''We can increase dimension with the help of this argument ndmin=x

x = np.array ([[1,2,3,4,5],[6,7,8,9,10]],ndmin=7)
print(x)


sum of total rows and columns'''

'''x = np.array([10,6,2])
y = np.array([20,4,3])
z = np.sum([x,y])
print(z)'''


'''x = np.array([10,12,2])
y = np.array([16,15,3])     #axis = 0 add these elements with respect to columns
z = np.sum([x,y], axis=0)
print(z)'''


'''x = np.array([10,12,2])
y = np.array([16,15,3])     #axis = 1 add these elements with respect to rows
z = np.sum([x,y], axis=1)
print(z)'''



x = ["sunday", "monday", "tuesday", "wednesday", "Thursday","Friday","Saturday", "papaya"]
'''print(x)
print(len(x))
print(x[1])
print(x[-6])
print(x[2:5])
print(x[-5:-2])
print(x[:-4])'''


'''return third item 
return fifth item 
return seventh item 
return fifth to eight items
return third fourth and fifth items
return second item to seventh items
return second last to start
return third to eight items'''


x = ["sunday", "monday", "tuesday", "wednesday", "Thursday","Friday","Saturday", "papaya"]

'''for i in x:
  print(i)'''

'''y = 0
while y<(len(x)):
  print(x[y])
  y+=1'''

'''y = 0
z = len(x)-1
while y<=z:
  print(x[z])
  z-=1'''


'''for i in range(len(x)-1,0,-1):
  print(x[i])'''





#First logic

'''x = int(input("Enter a number: "))
y = 1
for i in range(x,1,-1):
  y=i*y
print("This is my factorial",y)

#second logic

x = int(input("Enter a number: "))
y = 1
for i in range(1,x+1):
  y = y*i
print("This is my factorial",y)'''



'''x = {"sunday", "monday", "tuesday","wednesday","thursday"}
y = {1,2,3,4,5}
x=x.union(y)
print(x)'''


'''x = {"sun","mon","tues","jan","feb","march"}
y = {"sun","mon","tues","wed","thurs"}
x.intersection_update(y)
print(x)
'''

'''x = {"sun","mon","tues","jan","feb","march"}
y = {"sun","mon","tues","wed","thurs"}
z=x.intersection(y)
print(z)
'''

'''x = {"sunday", "monday", "tuesday","wednesday","thursday","friday","saturday"}
y =x.pop()
print(y)                #removed item
print(x)'''


'''student = {"Name": "Arun","School": "XYZ","Age": 16,"Roll_no" : 12}
print(student)'''




'''x = {
  "Name": "ABC",

  "School": "xyz",

  "Age": 16,

  "Roll_no": 12
} 
print(x)'''


'''x = {
  "Name": "ABC",
  "School": "xyz",
  "Age": 16,
  "Roll_no": 12
}

x = x["Roll_no"]
print(x)'''


'''class Parrot:
  def fly(self):
    print("Parrot can fly")
  def swim(self):
    print("Parrot can't swim")

class Penguin:
  def fly(self):
    print("Penguin can't fly")
  def swim (self):
    print("Penguin can swim")

def flying_test(self):
  self.fly()
  self.swim()

bird = Parrot()
Peggy = Penguin()

flying_test(bird)
flying_test(Peggy)'''


'''from abc import ABC,abstractmethod
class employee(ABC):
   def A(self):    
      pass
 
class employee_1(employee):
   def B(self,a,b):
      self.a = a 
      self.b = b
      self.c = self.a * self.b
      print(self.c)
class employee_2(employee):
   def C(self,a,b):
      self.a = a 
      self.b = b
      self.c = self.a + self.b
      print(self.c)

emp1 = employee_1()
emp2 = employee_2()
emp1.B(4,5)
emp2.C(7,8)'''


#It should be correct

'''from abc import ABC,abstractmethod

class employee(ABC):
  def A(self):
    pass
class employee_1(employee):
  def B(self,a,b):
    self.a = a
    self.b = b
    self.c = a * b
    #print(self.c)
class employee_2(employee):
  def C(self,a,b):
    self.a = a
    self.b = b
    self.c = a + b
    #print(self.c)

emp1 = employee_1
emp2 = employee_2

emp1.B(4,5)
print(emp1.c)

emp2.C(7.8)

#print(emp2.c)
'''
'''x = np.zeros((1,3))       # Two parameters here, one for row and three for columns.
print(x)'''

'''x = np.zeros((5,5))   # First parameter for row and second parameter for columns.
print(x)'''

'''x = np. array ([1,5,4,6,7,3j,5j],ndmin=5)
print(x)
print(x.dtype)'''


'''x = np.full((12,12),500)    #First parameter for row and second parameter for columns and third parameter
print(x)          #for the matrix
x = x*2
print(x)'''


'''x=np.arange(10,50,5)
#print(x)
x = x*2
#print(x)
x = x+2
print(x)'''

'''x = np.random.randint(1,50,5)  # first parameter for specified the number and second also specified the
                #number and third parameter tell how much number you want.
print(x)'''

'''
x = np.zeros((5,6,5))
print(x)'''
'''x=x+2
print(x)'''

'''x = np.ones((5,4,5))
#print(x)
x = x+5
#print(x)
x = x-1
print(x)'''


'''x = np.zeros((2,6,5))
print(x)
x=x+2
print(x)'''


'''x = np.eye(5)
print(x)'''

'''x = np.eye(5,5)
#print(x)

a = np.diag(x)            #It is fetching the diagonal elements
print(a)
print(a+9)'''

'''x = np.diagflat([[1,2,3,4],[5,6,7,8]])  
print(x)                     # This diagflat() shift these elements in the matrix as diagonal sequence
a = np.diag(x)'''
#print(a)


'''x = ["sun","mon","tues","wed"]
print(x[::-1])
'''

'''y = x.index("tues")
print(y)

'''
'''x = ["sun", "mon", "tues"]
x[2] = "wednesday"
print(x)
'''


#x = ["sunday", "monday",[ "tuesday", "wednesday", "thursday"], "friday","sat","ora"]
#print(x)
#print(x[2][2])
#print(x[3])
#print(x[1:5])

#print(x[2][::-1])


'''x[2].append("wed")
print(x)'''

'''x[2].insert(1,"papaya")
print(x)'''


'''x = {
  "Name"    : "ABC",
  "School"  : "xyz",
  "Age"     : 16,
  "Roll_no" : 12
  }

x.update({"admission date": "01/06/2022"})
#print(x)


for i, y in x.items():
  print(i," : ", y)
'''

'''y = x.copy()
print(y)'''

'''y = dict(x)
print(y)'''





'''x = ["sunday", "monday",["tuesday", "wednesday", "thursday", "friday","sat"],"orange"]

print(x)

Extract the values without method

"monday"
"wednesday"to "friday"

"monday to sat"

in second list replace two values with the one value.

use methods as per ur requirements:

in first list add one item and index should be 3

add one item in last in the second list

print reverse second list

remove last item of the first list.

find the index of wednesday

print an empty list
'''



'''x = "Hello Delhi"
print(x[6])
print(x[-5])
print(x[4])
print(x[-7])

print(x[1:5])
print(x[-10:-6])

print(x[7:10])
print(x[-4:])'''




'''x = "Himachal Pradesh"
print(len(x))
return third item 
return fifth item 
return seventh item 
return fifth to eight items
return third fourth, fifth items
return second item to seventh items
return second last to start
return third to eight items
Return third, fourth, fifth items
Return third to last item
Return fifth to eight item
Return seventh to eight item
Return sixth to fifteen item
Return second last to first item
Return ninth to sixteen items
Return fourteen, fifteen, sixteen.'''


import develop
'''develop.x()

print(develop.y)

print(develop.z)'''

import develop as D



#print(D.y)

#print(D.z)

'''a = "Honesty is the best policy"
print(a.split())'''

'''x= "Good Morning India"
print("Good morning, \nkumod")'''      

'''x= "Good Morning India"
print("Good morning\tIndia")'''

'''x = "Good \bmorning India" 
print(x)  

quantity = 3
item_no = 45
price = 78.45

x = "I want {} pieces of item {} for {} price."
print(x.format(quantity, item_no, price))


Make a program with the help of string formating,'''



'''"My name is abc, I am 20 years old and I passed 12 in 2016, 
I purchase 24 oranges and the price of these orange are 60.50"'''

'''
Looping through a string

x = "Arunachal Pradesh"

print this string with the help of while loop and for loop.

print this string with help of while loop and for loop in reverse order.'''


'''x = np.array([[[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]]]])
#print(x[0][0][2][:-1])
print(type(x))
print(x.ndim)
print(x.shape)'''


'''class Parent():
  def __init__(self,a,b):
    self.a=a
    self.b=b 
    self.c=a*b
class child(Parent):               
  def first(self):
    y=1
    z=2
    while y<=10:
      i=y*z
      print(i)
      y+=1
  def second(self):
    print("All the best for future")

mul=child(10,5)  #para meter pass here , it is __init__ function
#mul.c(10,5)     Its __init__ u should not call and don't pass para meter here
print(mul.c)  
mul.first()
mul.second()'''

#x = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
'''print(x[3])
print(x[-4])
print(x[1:4])
print(x[-6:-3])

print a list with the help of while loop and for loop
print a list in reverse order with the help of for and while loop.'''

'''for i in x:
  print(i,end=" ")'''

'''a = str(input("Enter any string: "))
y = a.split() 
for i in y:
  print(i)'''



'''x = [ ]
n = int(input("Enter number of elements : "))
  
for i in range(0, n):
    y = [str(input()), int(input())]
    x.append(y)
      
print(x)'''






'''x= "Good Morning India"
print("Good morning \nIndia")'''    

# \t  Tab - It returns one tab


'''x= "Good Morning India"
print("Good morning \tIndia")'''


#\b It will return Backspace


'''x = "Good \bmorning India" 
print(x)'''

'''age = 18
x = "My name is ABC, and I am {} years old"
print(x.format(age))'''


'''How do you replace a string with an index in Python?
Replace Character at a given Position in a String using List. First, 
convert the string to a list, then replace the item at the given index with 
a new character, and then join the list items to the string.'''




'''import numpy

import numpy as np
'''

'''x = np.arange(6)
print(x)
print(type(x))

x = np.arange(2,10)
print(x)

x = np.arange(1,10,2)
print(x)'''

'''x= np.zeros(6)
print(x)
print(type(x))'''
#y = np.arange(10,20)

'''x = np.array([10,6,2])
y = np.array([20,4,3])
z = np.sum([x,y])
print(z)'''

#If I want to add these elements with respect to columns and rows


'''x = np.array([10,12,2])
y = np.array([16,15,3])     #axis = 0 add these elements with respect to columns
z = np.sum([x,y], axis=0)
print(z)'''

'''x = np.array([10,12,2])
y = np.array([16,15,3])     #axis = 1 add these elements with respect to rows
z = np.sum([x,y], axis=1)
print(z)'''


'''x = np.zeros((4,3))   # Two parameters here, first for row and second for columns.
print(x)

x = np.ones((3,5))   # Two parameters here, first for row and second for columns.
print(x)


x = np.full((5,4),8)   # three parameters here, one for row and second for columns, and for matrix
print(x)

x = np.full((3, 6),100)
print(x)'''


'''first parameter for specified the number and second also specified the number and 
third parameter tell how much number you want.'''

'''x = np.random.randint(5,10,2)  
print(x)'''

'''x = np.array([1,5,3,100,4,48])
x=np.std(x)
print(x)


mean = 26.833333333333332'''


'''class Parent ():
  def first(self,a,b):
    self.a=a
    self.b=b
    self.c=a+b
  def __init__(self,x,y):
    self.x=x
    self.y=y 
    self.z=x*y
class Child(Parent):
  def second(self,A,B):
    self.A=A 
    #print(self.A)
    self.B=B 
    self.C=A/B
    super().first(a,b)
    super().__init__(x,y)
Mul=Child(5,6)
Mul.first(4,3)
print(Mul.c)
Mul.second(8,9)
print(Mul.C)
print(Mul.z)'''


'''How can we repace any character on specific index.
x = "Arunachal Pradesh"
y=x[4].replace('a','@')
print(y)
print(x)'''



'''x = "Arunachal Pradesh"
y=x.count('z')
print(y)'''

'''age = int(input("Enter age: "))
clas = int(input("Enter class: "))
years = int(input("Enter years: "))
dozons = int(input("Enter dozens: "))
price = float(input("Enter price: "))
x = "My name is priya, I am {} years old and I passed {} in {},I purchase {} oranges and the price of these orange are {}"
print(x.format(age,clas,years,dozons,price))


#You can replace items in dictionary
 
x = {
  "age": 16,
  "class": 12,
  "years": 16,
  "dozens": 12,
  "price" : 76.32
  }


x["class"] = 10
x["age"] = 20         

print(x)'''

'''x = np.arange(16)
#print(x)
a = np.diag(x)            #It is fetching the diagonal elements
#print(a)
print(a+3)'''

'''x = np.eye(5,5)
print(x)
y = np.fliplr(x)
print(y)
'''


'''x = np.eye(5,5)
print(x)
y = np.fliplr(x)
print(y+2)
z = np.diag(y+2)
print(z)'''



'''x = np.zeros((2,6,5))
#print(x)
x=x+2
print(x)'''

# How can we fill an empty dictionary

'''x = {}


x["Name"] = 'ABC'
x["Roll_NO"] = 25
x["Age"] = 18
x["class"] = "11th"
print(x)'''


#How can we fill empty set()

'''x = set()
y = [1,2,3]
x.update(y)
x.add("wed")
print(x)'''

#How can we fill empty list.

'''x = []
y = [3,2,6.4,6j,"monday"]
x.extend(y)
print(x)'''

'''x = []
y = [3,2,6.4,6j,"monday"]
x.extend(y)
x.insert(3,"banana")
print(x)'''


'''x = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
i = 0
while i < len(x):
  print(x[i])
  i+=1'''

'''x = np.array([1, 2, 3])

y = np.array([4, 5, 6])

z = np.concatenate((x, y))

print(z)'''

'''x = np.array([[1, 2], [3, 4]])    

y = np.array([[5, 6], [7, 8]])    #axis = 1 concatenate acording to column wise

z = np.concatenate((x, y), axis=0)

print(z)'''


'''x = np.array([1, 2, 3])

y = np.array([4, 5, 6])

z = np.stack((x, y), axis=1)

print(z)'''

'''x = np.array([1, 2, 3, 4, 10])

y = np.array([6, 7, 8, 9, 11])

z = np.dstack((x, y))

print(z)'''


'''x = np.array([1, 2, 3, 4, 5, 6])

y = np.array_split(x, 8)

print(y)'''


'''x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

y = np.hsplit(x, 3)

print(y)'''


'''x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

y = np.vsplit(x, 3)

print(y)
'''

'''x = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]])

y = np.dsplit(x, 3)

print(y)

'''

'''x = np.array([[1, 2, 3], [4,5,6]])
print(x)
'''

'''x = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(x)
print(x.transpose())
'''

'''x = ("sunday", "monday", "tuesday","wednesday","thursday","friday","saturday","January")
print(x[-2::-1])'''



'''x = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday","dff","ggh")
y = list(x)

y[1:4] = ("January",)
#print(y)
x = tuple(y)
print(x)'''


'''x = ("sunday", "monday", "tuesday")

a,b,c = x

print(a)
print(c)
print(a)
print(b)'''

'''x = ("sunday", "monday", "tuesday","wednesday","thursday","friday","saturday")

(jan,*feb,march) = x

print(jan)
print(feb)
print(march)'''

'''x = np.array([1, 2, 3, 4, 5])
y = x.copy()
x[1] = 18

print(x)
print(y)


x = np.array([1, 2, 3, 4, 5])
y = x.view()
x[0] = 18

print(x)
print(y)'''


'''x = np.array([1, 2, 3, 4, 5])

for i in x:
  print(i)
'''

'''x = np.array([[1, 2, 3], [4, 5, 6]])

for i in x:
  print(i)'''


'''x = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])
for i in x:
  for y in i:
    print(y)'''

'''x = np.array([[[[1, 2, 3], [4, 5, 6],[7,8,9]]]])

for i in np.nditer(x):
  print(i)

for i in x:
  for y in i:
    for z in y:
      for w in z:
        print(w)'''



'''x = np.array([1, 2, 3, 4, 5, 4, 4])

y = np.where(x == 4)

print(y)'''


'''x = np.array([1, 2, 3, 4, 5, 6, 7, 8])

y = np.where(x%2 == 0)

print(y)'''
'''Example

Find the indexes where the values are odd:
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])

y = np.where(x%2 == 1)

print(y)'''

'''def add(a,b):

  print(a+b)

def sub(a,b):

  print(a-b)


add(3,6)
sub(4,8)
add(9,4)



Create functions and pass two arguments and perform all arthmetic operations, 
then call it in shuffling way.

first subtraction
second multiplication
third division
fourth floor divison
fifth exponentiation
six modulus.'''

'''def D():
  a=int(input("Enter first number: "))
  b=int(input("Enter second number: "))
  print(a*b)
  print(a/b)
  print(a-b)
  print(a%b)
  print(a//b)
D()
'''

'''def x(*names):
  print("I am good" , names[0])
  print("Hello world" + " "+ names[7])
  print("Good Morning" , names[2])
  print("I am indian officer" + " "+ names[5])
  print("I am an Army officer" + " "+ names[4])

x("Koyal","XYZ","IBM","GOOGLE","REF","Indian","Microsoft","Amazone")'''


'''def x(Name,Age,Class):
  print("My name is" +" " + Name)
  print("My Class is" , Class)
  print("My Age is" , Age)

x(Name = "ABC", Age = "15", Class = "Xth")'''




'''x = ["apple", "banana",[ "cherry", "orange", "kiwi"], "melon", "mango"]
#print(x)
#print(x[2][0])
#print(x[3])
#print(x[1:4])
print(x[2][0:2])'''

#insert "papaya", and index should be 1 on the second list.

'''x = ["apple", "banana",[ "cherry", "orange", "kiwi"], "melon", "mango"]
x[2].insert(1,"papaya")
print(x)'''

'''x = ["apple", "banana",[ "cherry", "orange", "kiwi"], "melon", "mango"]
x[2].clear()
#print(x)
x[2].extend([1,2,3,3.12,4j,"mango"])
print(x)
'''

'''x = [1,2,["sun","mon",["apple","banana"],"Tues"],5,6]
x[2][2].reverse()
print(x)'''

'''x = [1,2,["sun","mon",["apple","banana","kiwi"],"Tues"],5,6]
x[2][2][::-1]
print(x)'''

'''Reverse this third list
Extract this "sun"
Extract "mon"to "Tues"
extract 5 to 6
add one item in third list
add one item in second list and index should be 2
remove third item in the second list'''

'''x = ['a','b','c','d','e']
print(x[::-1])'''

'''x = ["sun","mon","tues","wed"]
y = x.index("tues")
print(y)'''
#x = ["apple", "banana",[ "cherry", "orange", "kiwi"], "melon", "mango"]

'''x = ["sun","mon","tues","wed","mon","mon","mon","mon","mon"]
#print(x)
y = x.count("mon")
print(y)'''

'''x = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
x.clear()
print(x)'''  

'''x = [1,2,3,3,3,3,4,5,6,3,3]
y=x.count(3)
print(y)'''

'''x = ["sun","mon","tues","wed"]
x.append("thurs")
print(x)'''


'''x = ["sun","mon","tues","wed"]
x.insert(2,"thurs")
print(x)'''



'''x = []
y = [3,2,6.4,6j,"monday"]
x.extend(y)
print(x)
'''

'''Take user input and make list and print it with the help of for loop and while loop
print it in reverse order.'''

'''a = str(input("Enter any string: "))
b = int(input("Enter a number: "))
y = a.split()'''

'''for i in y:
  print(i)'''


'''x = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

y = np.array_split(x, 3)

print(y)'''


'''x = np.eye(2)
print(x)
'''
'''x = np.eye(5,5)
print(x)'''

'''x = np.eye(6,7)     # First parameter for row and second parameter for column.
print(x)'''


'''x = np.arange(16)
print(x)'''
'''a = np.diag(x)            #It is fetching the diagonal elements
print(a)
print(a+3)'''


'''x = np.eye(6,7)     # First parameter for row and second parameter for column.
print(x)
a = np.diag(x)      #It is fetching the diagonal elements
print(a)
print(a+4)
'''


'''x = np.eye(5,5)
#print(x)
y = np.fliplr(x)
print(y)
'''

'''x = np.array([1, 2, 3, 4, 5, 4, 4])

y = np.where(x == 4)

print(y)'''

'''x = np.array([1, 2, 3, 4, 5, 6, 7, 8])

y = np.where(x%2 == 0)

print(y)'''

'''x = ("Arun",)
print(x)
print(type(x))'''

'''x = ("sunday", "monday", "tuesday","wednesday","thursday","friday","saturday","January")
print(x[-2::-1])
'''

'''x = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday","dff","ggh")
y = list(x)

y[1:4] = ("January",)
#print(y)
x = tuple(y)
print(x)'''


#x = ("sunday", "monday", "tuesday","wednesday","thursday","friday","saturday")
'''for i in x:
  print(i)'''

'''for i in range(len(x)):
  print(x[i])
'''

'''y = 0
while y<len(x):
  print(x[y])
  y+=1'''


'''y = 0
z = len(x)-1
while z>=y:
  print(x[z])
  z-=1'''

'''z = len(x)-1
for i in range(z,-1,-1):
  print(x[i])'''


#x = int(input("Enter any number: "))


'''x = ["apple", "banana", ["cherry", "orange", "kiwi"], "melon", "mango"]
#print(x)
print(x[3])'''


'''x = [1,2,["sun","mon",["apple","banana"],"Tues"],5,6]
print(x[2][3])

Extract sun to mon
extract 6
extract "banana"
add "kiwi" in third list
remove "Tues"
add three values in second list

x = ["apple", "banana", ["cherry", "orange", "kiwi"], "melon", "mango"]

Reverse this second list
return banana to mango
return only cherry to orange
remove one item in second list
add two items in first list'''


'''x = ["apple", "banana", ["cherry", "orange", "kiwi"], "melon", "mango"]
#print(x)
#print(x[2][1:])
print(x[3])'''

'''x = [1,2,["sun","mon",["apple","banana"],"Tues"],5,6]
print(x[2][2][0])
print(x[2][3])
print(x[2])'''


'''x = int(input("enter any number: "))
y = []
y.append(x)
print(y)'''

'''x = np. array ([2,1,5,4.2])
print(x)
print(x[1].dtype)

x = np. array (["abc",1,5,4.0])
print(x)
print(x.dtype)

An unsigned integer is a 32-bit datum that encodes a nonnegative integer 
in the range [0 to 4294967295].''' 

#x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

#x1 = x.reshape(4, 3)
#print(x1)

#x1 = x.reshape(3,4)

#x1 = x.reshape(6,2)

'''x1 = x.reshape(2,6)
#print(x1)


x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

x1 = x.reshape(2,3,2)

print(x1)'''

'''x = np.array([[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]]])
print(x.ndim)'''

'''x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#z = x[(x>2) & (x < 11)]
z = (x>2) & (x < 11)
print(z)
'''

'''x = int(input("enter any number: "))
y = []
for i in range(x):
  z = eval(input("enter any number: "))
  y.append(z)
print(y)
'''


'''x = ("hello",)
print(type(x))
print(len(x))
'''

'''x = str(input("Enter any string: "))
y = 0
while y<len(x):
  if 
  x[y]==a or x[y]==e or y==i or y==o or y==u or y == 'A' or y == 'E' or y == 'I' or y == 'O' or y == 'U':
    z+=y
  #y+=1
print(z)'''

#Update tuple with the help of type casting

'''x = ("sunday", "monday", "tuesday","wednesday","thursday")
y = list(x)
y[1:3] = ["january"]
x = tuple(y)
print(x)
'''
'''x = ("sunday", "monday", "tuesday")

a,b,c = x

print(a)
print(c)
print(a)
print(b)
'''

'''x = ("sunday", "monday", "tuesday","wednesday","thursday","friday","saturday")

(*jan,feb,march) = x

print(jan)
print(feb)
print(march)'''


'''a=[11 12 13 14 15 16 17 18 19 20]

unique_values = np.unique(a)
print(unique_values)
'''

'''x = np.array([[2,4,6],[1,3,5]])
print(x)
y = np.cumsum(x)
print(y)'''


'''x = np.array([[2,4,6],[1,3,5]])
print(x)
y = np.cumsum(x,axis=1)
print(y)'''


'''x = np.array([[2,4,6],[1,3,5]])
print(x)
y = np.cumsum(x,axis=0)
print(y)'''


'''x = {"sunday", "monday", "tuesday","wednesday","thursday","friday","saturday"}
y =x.pop()
print(y)                #removed item
print(x)'''


'''x = {"sun","mon","tues","jan","feb","march"}
y = {"sun","mon","tues","wed","thurs"}
x.intersection_update(y)
print(x)'''


'''Given the names and grades for each students in a class of students, store 
them
in a nested list and print the names(s) of any student(s) having the second 
lowest grade.

'''
'''x = int(input("Enter number of students: "))
y = []
  
for i in range(x):
  z = []
  name = str(input("Enter student name: "))
  marks = float(input("Enter student marks: "))
  z.append(name)
  z.append(marks)
  y.append(z)
print(y)
print(argmin(y))'''


'''x = ("sunday", "monday", "tuesday","wednesday","thursday","friday","saturday")
y = 0
while y<len(x):
  print(x[y])
  y+=1
'''

'''x = ("sunday", "monday", "tuesday","wednesday","thursday","friday","saturday")
y = 0
z = len(x)-1
while z>=y:
  print(x[z])
  z-=1'''

'''i = 1
while i < 10:
  if i == 8:
    break
  print(i)
  i += 1'''

'''x = ("sunday", "monday", "tuesday","wednesday","thursday","friday","saturday")
y = 0
while y<len(x):
  #print(x[y])
  if x[y]=="friday":
    break
  print(x[y])
  y+=1
'''
'''i = 0
while i < 10:
  i += 1
  if i == 8:
    continue
  print(i)
'''

'''x = ("sunday", "monday", "tuesday","wednesday","thursday","friday","saturday")
y = -1
z = len(x)-1
while y<z:
  y+=1
  if x[y]=="wednesday":
    continue
  print(x[y])'''

'''for i in x:
  print(i)'''

#print(len(x))


'''Take user input and print any string and find the vowel in this string.

Take user input and print a dynamic list
x = eval(input("enter any value: "))

with the help of for and while loop'''

#change this arrays elements into string

'''x = np. array ([2,1,5,7,0.4,3J,'tt'])
print(x)'''


'''x= np.zeros(6)
print(x)
print(type(x))

x= np.ones(7)
print(x)

x = np.ones(3)
print(x)
print(type(x))

x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])

z =  np.concatenate((x,y))
print(z)

x = np. array ([2,1,5,3,7,8])
y=np.sort(x)
print(y)'''

'''x = np.arange(6)
print(x)

x = np.arange(2,10)
print(x)

x = np.arange(1,10,2)
print(x)'''

'''y = np.arange(10,20)
print(y)'''

'''x = np.array ([1,2,3,4,5])
print(x)'''

'''print(type(x))
print(x.ndim)   #it represents the length of the array.
print(x.shape)
print(x.size)'''


#import numpy 
'''x = numpy.array([1,2,3,4,5])
print(x)
print(type(x))
print(x.size)
'''
#import numpy as np
'''x = np.array([[[23,45,67,32,12],[22,33,44,12,32]]])
#print(x.ndim)
print(x[0][1][1:4])'''

#HOW CAN WE CREATE BASIC ARRAYS

'''x = np.zeros(6)
print(x)
print(x+2)
'''

'''x = np.ones(4)
print(x)
print(x+5)'''

'''x = np.arange(6)
print(x)'''

'''x = np.arange(2,12)
print(x)'''

'''x = np.arange(2,22,2)
print(x)
print(type(x))
print(x.size)'''


'''from abc import ABC,abstractmethod

class employee(ABC):
  def A(self):
    pass
class employee_1(employee):
  def B(self,a,b):
    self.a = a
    self.b = b
    self.c = a * b
    #print(self.c)
class employee_2(employee):
  def C(self,a,b):
    self.a = a
    self.b = b
    self.c = a + b
    #print(self.c)

emp1 = employee_1
emp2 = employee_2

emp1.B(4,5)

emp2.C(7.8)

print(emp1.c)
print(emp2.c)'''


'''x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

#print(x[x < 5])
print(x[x > 12])
#print(x[x >10])
#print(x[x<=5])'''

'''x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

z = x[x%2==0] 
print(z)'''

'''x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
z = x[(x>2) & (x < 11)]
print(z)'''


'''x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#z = x[(x<2) | (x>13)]
#print(z)

#z = x[(x<1) | (x>16)]
#z = (x>5) | (x == 5)
z = (x<5) | (x > 16)    #if we want to get boolean value.
print(z)'''


'''z = np.linspace(4,8,num=4)
print(z)'''

'''z = np.linspace(2,8,num=4)
print(z)'''

'''z = np.linspace(3,10,num=5)
print(z)'''

'''z = np.linspace(3,10,num=5, retstep=True)
print(z)'''

'''z = np.linspace(2.0,3.0,num=5, retstep=True)
print(z)'''

'''z = np.linspace(2,8,num=4, retstep=True)
print(z)'''

'''z = np.linspace(2.0,3.0,num=5, endpoint = False)
print(z)'''

'''z = np.linspace(2,8,num=4, endpoint = False)
print(z)'''


'''x = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday","dff","ggh"]
x[1:3] = ["January", "fabuary"]
print(x)


x = []
y = [3,2,6.4,6j,"monday"]
x.extend(y)
x.insert(3,"banana")
print(x)'''



'''x = []
y = eval(input("enter any element: "))

with the help of append()


Fill an empty list with the help of methods
Fill an empty list with the help of user input and make a dynamic list.


x = str(input(Enter any string: ))

Take user input and iterate this "string" with while loop and for loop. Then
reverse this string.

Take user input and find count the vowels in it.'''


'''def add(a,b):

  print(a+b)

def mul(d,e):
  print(d*e)

def sub(d,e):
  print(d-e)

def exp(d,e):
  print(d**e)

def div(d,e):
  print(d/e)


add(3,6)
div(6,3)
exp(2,3)
sub(6,3)
mul(5,6)
add(4,5)
exp(2,4)'''

'''x = {"sunday", "monday", "tuesday","monday","monday",True,False}
print(x)'''

'''x = {"sunday", "monday", "tuesday"}
y = {1,2,3,4,5,6,0}
x.update(y)
print(x)'''


'''x = {"sunday", "monday", "tuesday","wednesday","thursday","friday","saturday"}
y =x.pop()
print(y)                #removed item
print(x)'''


#import pandas as pd 
'''x = pd.Series([25,23,27,48,19])
print(x)
print(type(x))
print(len(x))'''

'''x = pd.Series([1,2,"a","b",2.13,7j,True,False])
print(x)'''


'''x = pd.Series([1,2,3,4,5])
print(x[4])
'''

'''x = pd.Series([25,23,27,48,19])
print(x[1:4])'''


'''x = pd.Series([1,2,3,4,5], index= ["a","b","c","d","e"])
#print(x)
print(x["a"])'''


'''x = pd.Series([1,2,3,4,5], index= ["one","Two","Three","Four","Five"])
print(x["one":"Four"])
'''
'''x = pd.Series([1,2,3,4,5], index= ["one","Two","Three","Four","Five"])
print(x)
print(x.dtype)
print(x.index)'''

'''x = pd.Series(np.random.randint(5), index=["a", "b", "c", "d", "e"])
print(x)'''

'''x = pd.Series({"a": 10, "b": 20, "c": 30})
print(x)'''

'''student = pd.Series({"Name": "ABC", "Age": 12, "Roll no": 13})
print(student)'''

'''x = pd.Series({"a": 10, "b": 20, "c": 30},index = {"b", "a", "d", "c"})
print(x)'''

'''x = pd.Series((22,33,44,55,66),index = ("a","b","c","d","e"))
print(x)
print(type(x))'''


'''x = pd.Series([34,45,76,23,89,98])
print(x[1:5])'''

#Extracting Elements from back
'''x = pd.Series([34,45,76,23,89,98])
print(x[-3:])
'''

'''x = pd.Series([34,45,76,23,89,98])
print(x[::-1])'''

'''x1 = pd.Series([10,20,30,40,50,60,70])
x2 = pd.Series([23,34,56,78,12,12,23])
z = x1+x2
print(z)'''
'''x1 = pd.Series([10,20,30,40,50,60,70])
x2 = pd.Series([23,34,56,78,12,12,23])
z = x1+x2
print(z)

print(x1+x2)
print(x1*x2)
print(x1/x2)
print(x1//x2)
print(x1-x2)'''

'''x = pd.DataFrame({"Name":["Deepak","Kanika","Samridhi","Hemlata"], "Marks": [78,67,92,87]})
print(x)
print(type(x))
print(len(x))'''

'''Students = {"student 1" :{"Name": "Aryan", "Age": 16}, "student 2" : {"Name": "prerna","Age" : 16},
"student3": {"Name" : "preeti", "Age" : 18 }}
print(Students)'''


'''student_1 = {
  "name" : "Abc",
  "Age"  :  16
}

student_2 = {
  "name" : "xyz",
  "Age"  :  18
}

student_3 = {
  "name" : "RBC",
  "Age"  :  19
}

students = {
  "student_1" : student_1,
  "student_2" : student_2,
  "student_3" : student_3
}

print(students)'''




'''quantity = 3
item_no = 45
price = 78.45

x = "I want {} pieces of item {} for {} price."
print(x.format(quantity, item_no, price))'''


'''x = int(input("Enter a number: "))
y = int(input("Enter second number: "))
z = x/y
u = "I want {} marks"
print(u.format(2f,z))'''

#print("Hello")

'''z = {}
x = int(input ("enter a number: "))
y = 0
while y<x:
  keys = str(input("Enter any key: "))
  values = eval(input("Enter any value: "))
  z[keys] = values
  y+=1
print(z)'''

'''z = {}
x = int(input("Enter a number: "))
for i in range(x):
  keys = str(input("Enter any keys: "))
  values = eval(input("Enter any value: "))
  z[keys] = values
print(z)'''

'''z = []
x = int(input("Enter a number: "))
y = 0
while y < x:
  t=eval(input("Enter any element: "))
  z.append(t)
  y+=1
print(z)
'''
'''z = []
x = int(input("Enter a number: "))
for i in range(x):
  a = eval(input("Enter any element: "))
  z.append(a)
print(z)
'''





'''y = x.loc[1:3,('Fruits','quality')]
print(y)'''

              #first parameter represent the rows, and second parameter represent 
   

'''The difference between .iloc and .loc method is we passed index in the .iloc method and 
we passed the cloumn names in the .loc method and all values are the inclusive.

Use of .iloc[]
How can we extract values from data sets, row wise or column wise.'''


'''x= iris.iloc[0:3,0:2]
print(x)                #first parameter represent the rows, and second parameter represent 
                        #represent column.
x = iris.iloc[5:11,2:]
print(x)'''

'''x = iris.loc[6:10,('SepalWidthCm','PetalLengthCm')]
print(x)'''


'''x = pd.DataFrame({"Fruits":["apple","mango","banana","orange","papaya"], "cost": [78,67,92,87,96], "quality" : ["Good for health","sweet","yummy","tasty","sour"]})
z = x.loc[1:4,('Fruits','cost')]
print(z)'''




'''x = {"sun", "mon", "tues"}
y = {"Jan", "feb", "march"}

z = zip(x, y)
print (set(z))'''


'''x = lambda a : a + 10
print(x(5))
'''

'''x = lambda a, b : a * b
print(x(5, 6))'''


'''x = lambda a, b, c : a + b + c
print(x(5, 6, 2))'''


'''x = lambda a, b, c, d, e, f: a + b * c- d + e / f
print(x(5, 6, 2,6,8,4))
'''


'''x = ("sun", "mon", "tues")
y = ("Jan", "feb", "march")

z = zip(x, y)
print (tuple(z))
'''

'''x = ["sun", "mon", "tues"]
y = ["Jan", "feb", "march"]

z = zip(x, y)
print (list(z))'''


'''x = {"sun", "mon", "tues"}
y = {"Jan", "feb", "march"}

z = zip(x, y)
print (set(z))'''

'''x = {"sun", "mon", "tues"}
y = {"Jan", "feb", "march"}

z = zip(x, y)
print (dict(z))
'''


'''x = ("sun", "mon", "tues")
y = ["Jan", "feb", "march"]

z = zip(x, y)
print (list(z))'''


'''z = []
x = int(input("Enter a number: "))
y = 0
while y<x:
  s = eval(input("Enter any element: "))
  u = []
  if s > 45:
    u.append(s)
  z.append(s)
  y+=1
z.append(u)
print(z)
'''

'''Take two lists one for storing sublist and other one for storing elements of sublist.
Take a loops and start appending the elements onto the list.
Set the sublist to null.
Print the list.
'''

'''x=int(input("enter the size of list"))
y= int(input("enter the size of sublist"))
list1=[]
sublist=[]
for i in range(x):
  for j in range(y):
    sublist.append(input())
  list1.append(sublist)
  sublist=[]
print (list1)'''


'''x=int(input ("enter the size of list"))
stu=[]
record=[]
for i in range(0,x):

    
    stu.append(input())
    stu.append(input())
    record.append(stu)
    stu = []

print(record)
'''

'''z =[]
r=[]
x = int (input("Enter a number: "))
y = 0
while y<x:
  t = eval(input("Enter an element: "))
  s = eval(input("Enter an element: "))
  z.append(t)
  r.append(s)
  y+=1
z.append(r)
print(z)
'''


'''z =[]
x = int (input("Enter a number: "))
y = 0
r=[]
c = []
while y<x:

  t = eval(input("Enter an element: "))
  s = eval(input("Enter an element: "))
  q = eval(input("Enter an element: "))

  z.append(t)
  r.append(s)
  c.append(q)
  y+=1
z.append(r)
r.append(c)
#print(r)
print(z)'''


'''x= int(input("Enter a number: "))
z = []
y = 0
while y<x:
  t=eval(input("Enter any element: "))
  z.append(t)
  y+=1
  e=set(z)
print(e)'''


'''z = open("g4.py", "w")
z.write("write method will overwrite the content")
z = open("g8.py", "r")
print(z.read())'''

import numpy as np
import pandas as pd
'''x = pd.Series(np.random.randint(3), index=["a", "b", "c", "d", "e"])
print(x)
print(x.index)
print(x.dtype)'''

'''student = pd.Series({"Name": "ABC", "Age": 12, "Roll no": 13}, index = {"Age", "class", "Name", "Roll no"})
print(student)
'''

'''x = pd.Series({"a": 10, "b": 20, "c": 30},index = {"b", "a", "d", "c"})
print(x)
'''
'''Create a class and make three methods in this class in first method do exponent, 
in second method print any statement and in third method find the modulus. take 
different arguments for all methods, and use __init__ function in this class.
'''

'''class x:
  def __init__(self,a,b):
    self.a=a
    self.b=b
    self.z=a**b
  def r(self):
    print("I love Delhi")
  def w(self,c,v):
    self.c = c
    self.v=v 
    self.k=(c%v)
x1 = x(2,3)
print(x1.z)
x1.r()
x1.w(6,3)
print(x1.k)'''


'''class x:
  def __init__(self):
    a=int(input("Enter a number: "))
    b=0
    while b<10:
      b+=1
      print(a*b)
      

  def Y(self):
    w=int(input("Enter a number: "))
    e=int(input("Enter a number: "))
    self.s=w*e
x1=x()
x1.Y()
print(x1.s)'''


'''class parent ():
  def __init__(self,a,b):
    self.a=a
    self.b=b
    self.z=a*b
    
class child (parent):
  def __init__(self,a,b,c,d):
    super(). __init__(a,b)
    self.c=c
    self.d=d
    self.w=c+d
    
ob=child(2,3,4,5)
print(ob.z)
print(ob.w)


Create two class and make two methods in each calss in first method do any arithmetic
operation and in second method print any statement, in second class print a list with
the help of while loop and in second method do any calculation. use __init__ constructor 
and super function as per your requirement.'''

'''class x:
  def __init__(self,a,b):
    self.a=a 
    self.b=b 
    self.c=a*b 
  def Y(self):
    print("Delhi is my favourite city")
class z(x):
  def F(self):
    y=["apple","mango","banana","orange","kiwi"]
    u = 0
    while u<len(y):
       print(y[u])
       u+=1
  def __init__(self,m,n,a,b):
    super().__init__(a,b)
    self.m=m
    self.n=n
    self.q=m**n 
E=z(2,3,4,3)
print(E.c)
print(E.q)
E.Y()
E.F()'''

'''y=["apple","mango","banana","orange","kiwi"]
u = 0
while u<len(y):
   print(y[u])
   u+=1'''

'''x = lambda a : a + 10
print(x(5))'''

'''Lambda functions can take any number of arguments:

Multiply argument a with argument b and return the result:'''

'''x = lambda a, b : a * b
print(x(5, 6))'''

#Summarize argument a, b, and c and return the result:

'''x = lambda a, b, c : a + b + c
print(x(5, 6, 2))'''

'''x = lambda a, b, c, d, e, f: a + b * c- d + e / f
print(x(5, 6, 2,6,8,4))'''


'''x = {"sun", "mon", "tues"}
y = {"Jan", "feb", "march"}

z = zip(x, y)
print (tuple(z))'''

'''x = map('a','b','c')
print(x)
'''
'''tables = [lambda x=x: x*10 for x in range(1, 11)]
 
for table in tables:
    print(table())'''

'''x = [lambda y=y: y*10 for y in range(1,11)]
for i in x:
  print(i())'''

#How can we read excel file in my text editor



#x = pd.read_excel('C:/Users/shpoo/Desktop/B1.xlsx')
#print(x)

'''x.iloc[2,1] = 500  #First parameter for row and second parameter for column
print(x)
'''
'''x=pd.read_excel('C:/Users/shpoo/Desktop/B1.xlsx',sheet_name='Sheet2')
print(x)
'''

'''x=pd.read_excel('C:/Users/shpoo/Desktop/B1.xlsx',sheet_name='Sheet3')
print(x)
'''
#NOTE: If I want to check all sheets together

'''x = pd.read_excel('C:/Users/shpoo/Desktop/B1.xlsx',sheet_name=['Sheet1','Sheet2','Sheet3'])  
print(x)
'''

#NOTE: By defalut it will read first sheet.


# Now I want to write something in my excel file.

'''with pd.ExcelWriter('DAone.xlsx')as writer:
  x.to_excel(writer,sheet_name='Sheet1')
  x.to_excel(writer,sheet_name='Sheet2')
  x.to_excel(writer,sheet_name='Sheet3')
  x.to_excel(writer,sheet_name='Sheet4')
  x.to_excel(writer,sheet_name='Sheet5')
  print(x)
'''
'''with pd.ExcelWriter('DAone.xlsx')as writer:
  x = pd.DataFrame({"Name":["Kajal","Koyal","Kiran"], "Marks": [78,67,92]}, 
    index = [1,2,3])
  x.to_excel(writer,sheet_name='Sheet1')
  x = pd.DataFrame({"Fruits":["Apple","Mango","Banana"], "Cost": [89,67,23]}, 
    index = ["a","b","c"])
  x.iloc[0,1]=1000
  x.to_excel(writer,sheet_name='Sheet2')
  x = pd.DataFrame({"Vegetables":["Potato","Tomato","Peas"], "Cost": [34,56,78]}, 
    index = ["A1","B1","C1"])
  x.to_excel(writer,sheet_name='Sheet3')
  x = pd.DataFrame({"Food Products":["sauce","Butter","Jam"], "Cost": [79,39,89]}, 
    index = ["A","B","C"])
  x.to_excel(writer,sheet_name='Sheet4')
  x = pd.DataFrame({"Pickles":["mango_pickles","chilly_pickles","Mix_pickles"], 
    "Cost": [89,90,120]}, index = ["One","Two","Three"])
  x.iloc[1,1]='100'
  x.to_excel(writer,sheet_name='Sheet5')
  print(x)'''



'''PIVOT FUNCTION

The pivot function in pandas is used to reshape the given data frame based on 
specific columns. 
Specified columns act as pivots of the data frame. An important thing to note is 
that the pivot 
function does not support data aggregation. Instead, multiple columns will return 
the data frame, 
becoming multi-indexed.'''


'''x = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two',

                           'two'],

                   'bar': ['A', 'B', 'C', 'A', 'B', 'C'],

                   'baz': [1, 2, 3, 4, 5, 6],

                   'zoo': ['x', 'y', 'z', 'q', 'w', 't']})'''

#print(x)

'''z=x.pivot(index='foo', columns='bar', values='baz')
print(z)
'''
'''z=x.pivot(index='foo', columns='bar')['baz']
print(z)
'''
'''z=x.pivot(index='foo', columns='bar', values=['baz', 'zoo'])
print(z)
'''









#If I want to change in second sheet
'''x=pd.read_excel('C:/Users/shpoo/Desktop/A2.xlsx',sheet_name='Sheet2')
x.iloc[1,0]='Rose'
print(x)'''






'''x=pd.read_excel('C:/Users/shpoo/Desktop/Datasets/ONE/Aone.xlsx',sheet_name='Sheet1')
print(x)
'''
'''x=pd.read_excel('C:/Users/shpoo/Desktop/Datasets/ONE/Aone.xlsx',sheet_name='Sheet2')
print(x)
'''

'''x=pd.read_excel('C:/Users/shpoo/Desktop/Datasets/ONE/Aone.xlsx',sheet_name='Sheet3')
print(x)
'''


'''x.to_excel('C:/Users/shpoo/Desktop/Datasets/ONE/Aone.xlsx',sheet_name='Sheet2')  # It shows only sheet number 2.
x.iloc[(1,2)] = 600
print(x)'''




'''x=pd.read_excel('C:/Users/shpoo/Desktop/Datasets/ONE/Aone.xlsx',sheet_name='Sheet2')    #by default it will read first sheet
x.iloc[1,1] = 6000
print(x)


x=pd.read_excel('C:/Users/shpoo/Desktop/Datasets/ONE/Aone.xlsx')    #by default it will read first sheet
x.iloc[1,1] = 6000
print(x)
'''






#by default it will read first sheet

'''pihu.to_excel('pihu1.xlsx',sheet_name='Sheet2')    
pihu.iloc[1,1] = 600
print(pihu)'''

#x = pd.read_excel('C:/Users/shpoo/Desktop/A2.xlsx')


#Now I want to check all sheets.

'''x1 = x.copy()
with pd.ExcelWriter('C:/Users/shpoo/Desktop/Datasets/ONE/Aone.xlsx')as writer:
  x.to_excel(writer,sheet_name='Sheet1')
  x.to_excel(writer,sheet_name='Sheet2')
  #print(x)
  print(x1)'''
  
# Now I want to write something in my excel file.
'''x = pd.read_csv('C:/Users/shpoo/Desktop/IRIS.csv')
#print(x)

with pd.ExcelWriter('B2.xlsx')as writer:
    x.to_excel(writer,sheet_name='Sheet1')
    x.to_excel(writer,sheet_name='Sheet2')
    x.to_excel(writer,sheet_name='Sheet3')
    print(x)'''
    


'''with pd.ExcelWriter('New_1.xlsx')as writer:
  x = pd.DataFrame({"Name":["Kajal","Koyal","Kiran"], "Marks": [78,67,92]}, index = [1,2,3])
  x.to_excel(writer,sheet_name='Sheet1')
  x = pd.DataFrame({"Fruits":["Apple","Mango","Banana"], "Cost": [89,67,23]}, index = ["a","b","c"])
  x.to_excel(writer,sheet_name='Sheet2')
  x = pd.DataFrame({"Vegetables":["Potato","Tomato","Peas"], "Cost": [34,56,78]}, index = ["A","B","C"])
  x.to_excel(writer,sheet_name='Sheet3')
  print(x)'''







'''with pd.ExcelWriter('output.xlsx')as writer:
  pihu = pd.DataFrame({"Name":["Kajal","Koyal","Kiran"], "Marks": [78,67,92]}, index = [1,2,3])
  pihu.to_excel(writer,sheet_name='Sheet1')
  pihu = pd.DataFrame({"Fruits":["Apple","Mango","Banana"], "Cost": [89,67,23]}, index = ["a","b","c"])
  pihu.iloc[0,1] = 900
  pihu.to_excel(writer,sheet_name='Sheet2')
  pihu = pd.DataFrame({"Vegetables":["Potato","Tomato","Peas"], "Cost": [34,56,78]}, index = ["A","B","C"])
  pihu.to_excel(writer,sheet_name='Sheet3')
  print(pihu)'''


#"26-05-06" Task

#By default it will read first sheet.


#x = pd.read_excel('abc.xlsx')
#print(x)



# Now I will change something in first sheet.

'''x = pd.read_excel('abc1.xlsx')
x.iloc[1,1] = 600
print(x)'''


'''x.to_excel('abc1.xlsx',sheet_name='Sheet2')    
x.iloc[1,0] = 600
print(x)'''


#Now I am reading sheets one by one

'''x = pd.read_excel('abc.xlsx',sheet_name='Sheet1')
print(x)'''
'''x = pd.read_excel('abc.xlsx',sheet_name='Sheet2')
print(x)'''
'''x = pd.read_excel('abc.xlsx',sheet_name='Sheet3')
print(x)'''

#Now I will read all sheets together

'''x = pd.read_excel('abc.xlsx',sheet_name=['Sheet1','Sheet2','Sheet3'])  
print(x)'''

#Now I want to write something in my excel sheet

'''NOTE: Through this pattern I can change only one sheet, but this pattern will remove all the 
sheets of this file except and return sheet2'''




#Now I want to change something in all the sheets together.

'''x = pd.read_excel('abc.xlsx')
with pd.ExcelWriter('Aone.xlsx')as writer:
  x = pd.DataFrame({"Name":["Kajal","Koyal","Kiran"], "Marks": [78,67,92]}, index = [1,2,3])
  x.to_excel(writer,sheet_name='Sheet1')
  x = pd.DataFrame({"Fruits":["Apple","Mango","Banana"], "Cost": [89,67,23]}, index = ["a","b","c"])
  x.to_excel(writer,sheet_name='Sheet2')
  x.iloc[0,1] = 900
  x = pd.DataFrame({"Vegetables":["Potato","Tomato","Peas"], "Cost": [34,56,78]}, index = ["A","B","C"])
  x.to_excel(writer,sheet_name='Sheet3')
  print(x)'''


'''with pd.ExcelWriter('Aone.xlsx')as writer:
  x = pd.DataFrame({"Name":["Kajal","Koyal","Kiran"], "Marks": [78,67,92]}, index = [1,2,3])
  x.to_excel(writer,sheet_name='Sheet1')
  x = pd.DataFrame({"Fruits":["Apple","Mango","Banana"], "Cost": [89,67,23]}, index = ["a","b","c"])
  x.iloc[0,1] = 9000
  x.to_excel(writer,sheet_name='Sheet2')
  x = pd.DataFrame({"Vegetables":["Potato","Tomato","Peas"], "Cost": [34,56,78]}, index = ["A","B","C"])
  x.to_excel(writer,sheet_name='Sheet3')
  print(x)'''




'''x = pd.DataFrame({"Name":["Deepak","Kanika","Samridhi","Hemlata"], "Marks": [78,67,92,87]})
print(x)
print(type(x))
print(len(x))'''



'''x = pd.DataFrame({"Fruits":["apple","mango","banana"], "cost": [78,67,92], "quality" : 
    ["Good for health","sweet","yummy"]},index = ["a","b","c"])
print(x)
'''
'''x = pd.DataFrame({"Fruits":["apple","mango","banana"], "cost": [78,67,92], "quality" : 
    ["Good for health","sweet","yummy"]},index = ["a","b","c"], 
    columns=["quality", "Fruits", "cost"])
print(x)
'''
'''x = pd.DataFrame({"Name":["Tejesvi","koyal","Kiran"], "Marks": [78,67,92]}, index = [1,2,3])
y = pd.DataFrame({"Name":["Ashok","Alok","Riya"], "Marks": [56,34,89]}, index = [4,5,6])
z = pd.DataFrame({"Name":["Deepak","Kanika","Samridhi"], "Marks": [78,67,92]},
index =[7,8,9])

r=(x,y,z)
w = pd.concat(r)
print(w)
'''

'''x = pd.DataFrame({"Name":["Tejesvi","koyal","Kiran"], "Marks": [78,67,92]}, index = [1,2,3])
y = pd.DataFrame({"Name":["Ashok","Alok","Riya"], "Marks": [56,34,89]}, index = [4,5,6])
z = pd.DataFrame({"Name":["Deepak","Kanika","Samridhi"], "Marks": [78,67,92]},
t=x.append(y)
a=t.append(z)
print(a)'''

'''z = {}
x = int(input("Enter a number: "))
for i in range(x):
  keys = str(input("Enter any keys: "))
  values = eval(input("Enter any value: "))
  z[keys] = values
print(z)'''



'''import numpy

x = numpy.array ([1,2,3,4,5])
print(x)

print(type(x))
print(x.size)
'''
import numpy as np

'''x = np.array([1,45,67,88,7.9])
print(x)
'''
'''x = np.array([[[[[[1,2,3,4,5]]]]]])


print(type(x))
print(x.ndim)   #it represents the length of the array. means numbers of square brackets.
print(x.size)
'''

'''x = np.array([[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]]])
print(type(x))
print(x.ndim)
print(x.shape)
print(x.size)

print(x[0][0][1][1:4])
'''

'''x = np.array([[[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]]]])

find the type, dimenstion,print this array, size of this array, and extract these values
of this array.

extract theses values:

return 7, 12, 18, 1, 20, 3 
return 7 to 10
return 12 to 13
reverse this array [16,17,18,19,20]
return 6 to 10 
return 2 to 3
print each array seprately'''

#MERGE OF DATAFRAME

'''x = pd.DataFrame({'Name_1':['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'],
  'Eng':[99,78,98,87,97,67]})
#print(x)


y = pd.DataFrame({'Name_2':['Ritesh','Ashish','Tajesvi','Omkar','Nikhil','Rahul','Abhishek','Ranjeet'],
  'Math':[99,78,98,87,97,67,75,98]})
#print(y)



z=pd.merge(left=x, right=y, how='inner', left_on='Name_1',right_on='Name_2')
#print(z)

z=pd.merge(left=x, right=y, how='inner', left_on='Name_1',right_on='Name_2', indicator = True)
#print(z)
'''

#OUTER MERGE


'''z=pd.merge(left=x, right=y, how='outer', left_on='Name_1',right_on='Name_2', indicator = True)
print(z)

#LEFT MERGE

z=pd.merge(left=x, right=y, how='left', left_on='Name_1',right_on='Name_2', indicator = True)
print(z)
'''

#RIGHT MERGE

'''z=pd.merge(left=x, right=y, how='right', left_on='Name_1',right_on='Name_2', indicator = True)
print(z)
'''

'''x = pd.Series(['Ashish',   'Arvind',   'Sahil',   'Deepak','Nikhil','Abhishek'])
print(x.str.split())
'''

'''x = [lambda y=y: y*5 for y in range(1,11)]
for i in x:
  print(i())
'''

'''create a program with the help of multilevel inheritance and make three classes and create
two methods in each class in first class first method take user input and find the 
factorial and in second method print any statement. in second class first method take
two variable and perform any arithmetic operarations and in second method print any 
statement in third method print the sum of any random number with the help of user input,
in second method take two arguments and perform any arithmetic operations.
'''

'''class x:
  def A(self):
    s = int(input("enter a number: "))
    y = 1
    while s>0:
      y=y*s
      s-=1
    print("Factorial is: ", y)
  def B(self):
    print("Delhi is my favourite place")

class x1(x):
  def C(self,h,i):
    self.h=h 
    self.i=i 
    self.z=(h**i)
  def D(self):
    print("I am the honest person")
class x2(x1):
  def E(self):
    w=int(input("Enter a number: "))
    y = 0
    k = 0
    while y<w:
      y+=1
      print(y)
      k+=y
    print("This the sum of all countings", k)
  def F(self,m,n):
    self.m=m 
    self.n=n 
    self.v=m*n
R = x2()
R.A()
R.B()
R.C(2,3)
print(R.z)
R.D()
R.E()
R.F(8,6)
print("This is the multiplication:", R.v)
'''

'''def E():
  w = int(input("enter"))
  y = 0
  k = 0
  while y < w:
    y+=1
    print(y)
    k+=y
  print(k)
E()'''

'''class first():
  def __init__(self,a,b):
    a=int(input("enter the number: "))
    b=1
    while a>0:
      b*=a
      a-=1
    print ("factorial:", b )
  
  def text(self):
    print("Anmol is a good girl")
'''
'''class second(first):
  def __init__(self,a,b):
    super().__init__(a,b)
    self.a=a
    self.b=b
    self.c=a*b
    #print(c)
  def text2(self):
    print("Hello")

class third(second):
  def __init__(self,a,b):
    super().__init__(a,b)
    a= int(input("enter the number: "))
    b= int(input("enter the number :"))
    self.k= a+b
    #print(k)

  def eng(self,a,b):
    self.a=a
    self.b=b
    self.c=a**b
  #print(c)\7

ob= third(5,6)
print(ob.k)
ob.text()
ob.text2()
ob.eng(3,4)
print(ob.c)'''



'''Fetch a dataset from keggle, and find 10 rows and all columns from start of data set, 
find seven rows from end of the dataset.
find any three rows and two columns from this data set.'''



'''Create three classes with the help of multiple inheritance and make two methods in each class
and use init function in each class and use super function as per your requirement. 
In first class first method take two argments and perform any arithmetic operation, and in second method
print a list with the help of while loop. In second class, in first method take two arguments
and perform any arithmetic operation and in second method print a dictionary keys with the help
of loop. In third class, in first method take two aregument and perform any arithmetic operation
and in second method take user input and print a table of any random number'''


'''a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])  
b = np.array([2,4,6,8,10,12,14])  
c = a+b  
print(c)'''


'''x = np.array([1, 2, 3, 4, 5, 6])

y = np.array_split(x, 7)

print(y)
'''
'''x = np.array([1, 2, 3, 4, 5, 6])

y = np.array_split(x, 3)
print(y)

print(y[1])
print(y[0])
print(y[2])
'''

'''x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

y = np.array_split(x, 3)

print(y)
'''

'''x = np.array([1, 2, 3])

y = np.array([4, 5, 6])

z = np.concatenate((x, y))

print(z)
'''

'''Example

Join two 2-D arrays along rows and columns:
import numpy as np'''


#x = pd.read_csv('Boston.csv')

'''x =pd.read_csv('IRIS.csv')
#print(x)

y=x.loc[6:10,('sepal_length','petal_length','petal_width')]
print(y)
'''

#print(y)
#print(x.shape)
#print(x.head(15))
#print(x.tail(8))
'''y = x.iloc[5:11,3]
print(y)'''

'''y = x.iloc[8:21,2:4]
print(y)'''

'''import pandas as pd 
x=pd.read_csv('iris.csv')
print(x)'''
#print(x.shape)
'''y = x.iloc[8:21,2:4]
print(y)
'''

import matplotlib
from matplotlib import pyplot as plt 
import numpy as np
import pandas as pd


#How can se create a line plot

'''x = np.arange(1,11)
y = 2*x
print(x)
print(y)
plt.plot(x,y)
plt.show()
'''
'''x = np.arange(1,11)
y = 2*x
print(x)
print(y)
plt.plot(x,y)
plt.title("SimpleLine Plot")
plt.xlabel("data on x-axis")
plt.ylabel("data on y-axis")
plt.show()
'''

'''x = np.arange(1,11)
y = 2*x
print(x)
print(y)
plt.plot(x,y,color='red',linestyle = ':', linewidth = 5)
plt.title("SimpleLine Plot")
plt.xlabel("data on x-axis")
plt.ylabel("data on y-axis")
plt.show()
'''
'''x = np.arange(1,11)
y1 = 2*x
y2 = 3*x
print(y1)
print(y2)
plt.plot(x,y1,color='orange',linestyle = ':', linewidth = 5)
plt.plot(x,y2,color='g',linestyle = '-.', linewidth = 5)
plt.title("Two Lines in one Plot")
plt.xlabel("range")
plt.ylabel("two lines")
plt.grid(True)
plt.show()
'''

'''x = np.arange(1,11)
y1=2*x
y2=3*x
print(y1)
print(y2)

plt.subplot(1,2,1)  # first parameter for row and second for columns and third parameter shows this is first sub plot.

plt.plot(x,y1,color='green',linestyle=':',linewidth=2)

plt.subplot(1,2,2)  # first parameter for row and second for columns and third parameter shows this is second sub plot.

plt.plot(x,y2,color='brown',linestyle=':',linewidth=5)

plt.show()'''


'''x = np.array([3, 8, 1, 10])

plt.plot(x, marker = 'o')
plt.show()
'''
'''x = np.array([3, 8, 1, 10])

plt.plot(x, marker = '*')
plt.show()
'''
'''x = np.array([3, 8, 1, 10])

plt.plot(x, marker = '_')
plt.show()
'''

'''x = np.array([3, 8, 1, 10])

plt.plot(x, marker = 'D')
plt.show()
'''

'''x = np.array([3, 8, 1, 10])

plt.plot(x, 'o:r')
plt.show()
'''
'''x = np.array([3,8,1,10])
plt.plot(x,'--')
plt.show()'''

'''x = np.array([3,8,1,10])
plt.plot(x, marker = 'o', ms = 20, mec = 'r')
plt.show()'''


'''x =np.array([3,8,1,10])
plt.plot(x, marker = 'o', ms = 20, mfc = 'r')
plt.show()'''

'''x = np.array([3,8,1,10])
plt.plot(x,marker = 'o', ms = 20, mec = 'r', mfc = 'y')
plt.show()'''

'''x = np.array([3,8,1,10])
plt.plot(x,marker = 'o', ms = 20, mec = 'r', mfc = 'hotpink')
plt.show()'''

'''x= iris.iloc[0:3,0:2]
print(x)                #first parameter represent the rows, and second parameter represent 
                        #represent column.
x = iris.iloc[5:11,2:]
print(x)'''

'''x = iris.loc[6:10,('SepalWidthCm','PetalLengthCm')]
print(x)'''


#x = pd.read_csv('iris.csv')
#print(x)
#print(x.shape)
#print(x.head(10))
#print(x.tail(10))
'''z=x.loc[6:10,('sepal_length')]
print(z)'''

import pandas as pd 

'''x = pd.Series([25,23,27,48,19])
print(x)
print(type(x))
print(len(x))
'''
'''x = pd.Series([1,2,"a","b",2.13,7j,True,False])
print(x)
'''

#x = pd.Series(["a","b","c","d","e"])
#print(x)
#print(x[1:4])

'''x = pd.Series([1,2,3,4,5], index= ["a","b","c","d","e"])
print(x['b':'d'])
'''

'''x = pd.Series([1,2,3,4,5], index= ["one","Two","Three","Four","Five"])
print(x)
print(x.dtype)
print(x.index)
'''

'''x = pd.Series(np.random.randint(100,1000,5), index=["a", "b", "c", "d", "e"])
print(x)
'''

'''x = pd.Series(np.random.randint(5), index=["a", "b", "c", "d", "e"])
print(x)
print(x.index)
print(x.dtype)
'''

'''x = pd.Series({"a": 10, "b": 20, "c": 30})
print(x)
'''
'''student = pd.Series({"Name": "ABC", "Age": 12, "Roll no": 13})
print(student)
'''

'''x = pd.Series({"a": 10, "b": 20, "c": 30},index = {"b", "a", "d", "c"})
print(x)
'''
'''student = pd.Series({"Name": "ABC", "Age": 12, "Roll no": 13}, index = {"Age", "Name", "Roll no"})
print(student)
'''

'''x = pd.Series([34,45,76,23,89,98])
#print(x[2])
#print(x[3:5])
print(x[1:])

'''
'''Extract values
76
23 to 89
45 to 98
34
'''
'''x1 = pd.Series([10,20,30,40,50,60,70])
x2 = pd.Series([23,34,56,78,12,12,23])
z = x1+x2
#print(z)

#print(x1+x2)
print(x1*x2)
print(x1/x2)
print(x1//x2)
print(x1-x2)'''

'''x1 = pd.Series([10,20,30,40,50,60,70])
print(x1 + 5)

'''

'''x = pd.DataFrame({"Name":["Deepak","Kanika","Samridhi","Hemlata"], "Marks": [78,67,92,87]})
print(x)
print(type(x))
print(len(x))
'''

'''x = pd.DataFrame({"Fruits":["apple","mango","banana"], "cost": [78,67,92], "quality" : 
    ["Good for health","sweet","yummy"]})
'''
'''x = pd.DataFrame({"Fruits":["apple","mango","banana"], "cost": [78,67,92], "quality" : 
    ["Good for health","sweet","yummy"]},index = ["a","b","c"])

'''
'''x = pd.DataFrame({"Fruits":["apple","mango","banana"], "cost": [78,67,92], "quality" : 
    ["Good for health","sweet","yummy"]},index = ["a","b","c"], 
    columns=["quality", "Fruits", "cost"])


print(x)'''

'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])
#print(x)
print(x.str.lower())
'''
'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])

print (x.str.cat(sep=',,'))
'''


'''student = {"kajal":87, "Arun": 56, "kiran":27}
a = list(student.keys())
b = list(student.values())
print(a)
print(b)
plt.bar(a,b)
plt.grid(True)
plt.show()
'''

'''Vegetables_basket = {"Brinjal":100, "Potatos": 145, "Tomatoes": 123}
Vegetables_names=list(Vegetables_basket.keys())
Vegetables_cost=list(Vegetables_basket.values())
plt.bar(Vegetables_names,Vegetables_cost)
plt.title("Bar Plot")
plt.xlabel("Vegetables_names")
plt.ylabel("Vegetables_cost")
plt.grid(True)
plt.show()
'''
'''Vegetables_basket = {"Brinjal":100, "Potatos": 145, "Tomatoes": 123}
Vegetables_names=list(Vegetables_basket.keys())
Vegetables_cost=list(Vegetables_basket.values())
plt.barh(Vegetables_names,Vegetables_cost,color = 'orange')
plt.title("Bar Plot")
plt.xlabel("Vegetables_cost")
plt.ylabel("Vegetables_names")
plt.grid()
plt.show()'''

'''x=[10,20,30,40,50,60,70,80,90]
y=[8,1,7,2,0,3,7,3,2]
plt.scatter(x,y)
plt.show()
'''
'''x = [4,5,1,6,2,3,7,8]
y = [80,10,40,50,34,20,80,30]
plt.scatter(x,y,color='g')
plt.title('scatter plot')
plt.xlabel('Years from starting of entity')
plt.ylabel('Revenue Growth in Percent(%)')
plt.grid(True)
plt.show()
'''
'''x = [4,5,1,6,3,5,8]
y = [8,1,4,5,2,8,3]
plt.scatter(x,y,marker="*",color='g',s=400)
plt.title('scatter plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()
plt.show()
'''

'''x = [10,20,30,40,50,60,70,80,90]
a = [8,1,7,2,0,3,7,3,2]
b = [7,2,5,6,9,1,4,5,3]
plt.scatter(x,a,marker="*",color='g',s=150)
plt.scatter(x,b,marker=".",color='orange',s=300)
plt.title('scatter plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()'''


'''x = [10,20,30,40,50,60,70,80,90]
a = [10,23,70,20,9,30,46,33,28]
b = [80,20,52,67,92,13,42,56,36]
plt.subplot(1,2,1)
plt.scatter(x,a,marker="*",color='g',s=150)
plt.title('Company Green')
plt.xlabel('Years from entity origin')
plt.ylabel('Revenue growth in percentage(%)')
plt.grid(True)
plt.subplot(1,2,2)
plt.scatter(x,b,marker=".",color='red',s=300)
plt.title('Company Red')
plt.xlabel('Years from entity origin')
plt.ylabel('Revenue growth in percentage(%)')
plt.grid(True)
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=0.4,hspace=0.4)
plt.show()'''

'''x = [10,20,30,40,50,60,70,80,90]
a = [8,1,7,2,0,3,7,3,2]
b = [7,2,5,6,9,1,4,5,3]
plt.subplot(2,1,1 )
plt.scatter(x,a,marker="*",color='red',s=150)
plt.title('scatter sub plots')
plt.xlabel('Years from entity origin')
plt.ylabel('Revenue growth in percentage')
plt.subplot(2,1,2)
plt.scatter(x,b,marker=".",color='blue',s=300)
plt.xlabel('Years from entity origin')
plt.ylabel('Revenue growth in percentage')
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=0.5,hspace=0.5)
plt.show()'''

#program for row wise elements addition in tuple matrix.
'''x = [[("Gfg",3)],[("Best",1)]]
y = [1,2]'''


'''x = np.arange(6)
print(x)

x = np.arange(2,10)
print(x)

x = np.arange(1,10,2)
print(x)
'''

'''x= np.zeros(6)
print(x)
print(type(x))

x= np.ones(7)
print(x)
'''
'''x = np.ones(3)
print(x)
print(type(x))
'''
'''x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])

z =  np.concatenate((x,y))
print(z)
'''
'''y = np.array([6,7,8,9,10], ndmin=6)
print(y)
'''
'''x = np.eye(2)
print(x)
'''

'''x = np.array([[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]]])
y=x.ndim
print(y)
'''
# Check size of an array
'''x = np.array([[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]]])
print(x.size)'''

#Check the shape of an array
'''x = np.array([[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]]])
print(x.shape)
print(x[0][0][1][2])
'''
# How can we insert dimension of an array

'''x = np. array ([1,5,4,6,7,3,5],ndmin=5)
print(x)
print(x.dtype)'''

#import numpy

#import numpy as np

'''x = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#print(x)
print(x.transpose())
'''
'''x = np.array([[11,23,56,78], [45,34,56,78]])
print(x.transpose())
print(x)'''

'''x = np.array([[11,23,56,78], [45,34,56,78]])
print(x.T)
'''

x = np.eye(2)
#print(x)


x = np.eye(5,5)
#print(x)

x = np.eye(6,7)     # First parameter for row and second parameter for column.
#print(x)
'''a = np.diag(x)      #It is fetching the diagonal elements
print(a)
print(a+4)
'''

'''x = np.arange(16)
print(x)
a = np.diag(x)            #It is fetching the diagonal elements
print(a)
print(a+3)
'''

'''x = np.diagflat([[1,2,3,4],[5,6,7,8]])  
print(x)  
a = np.diag(x)
print(a)
'''


'''x = np.arange(16)
#print(x)
a = np.diag(x)            #It is fetching the diagonal elements
#print(a)
#print(a+3)


x = np.arange(16).reshape(4,4)
#print(x)
a = np.diag(x)            #It is fetching the diagonal elements
#print(a)
print(a+3)
'''

'''z = open("New.py","a")

z.write(" \n Honesty is the best policy")

z = open("New.py","r")                    #open and read the file after the appending:
print(z.read())'''

#z.write(" \n python is important for machine learning")

'''import os
os.rmdir("aaaa")
'''

'''x = pd.read_csv('matches.csv')
#print(x.head(5))

x['player_of_match'].value_counts()
print(x)

plt.figure(figsize=(8,5))
plt.bar(list(x['player_of_match'].value_counts()[0:5].keys()),list(x['player_of_match'].value_counts()[0:5]),color='r')
plt.show()'''


'''x=pd.read_csv('matches.csv')
#print(x.head())
z=x.drop([1:3],axis=0)
print(z)'''

'''x= iris.iloc[0:3,0:2]
  print(x)                #first parameter represent the rows, and second parameter represent 
  '''  

'''x = pd.read_csv('matches.csv')
print(x)'''


'''z = np.linspace(4,8,num=4)
print(z)
'''
'''z = np.linspace(2,8,num=4)
print(z)

z = np.linspace(3,10,num=5)
print(z)
'''
'''z = np.linspace(3,10,num=5, retstep=True)
print(z)
'''
'''z = np.linspace(2.0,3.0,num=5, retstep=True)
#print(z)

z = np.linspace(2,8,num=4, retstep=True)
print(z)'''

'''z = np.linspace(2.0,3.0,num=5, endpoint = False)
print(z)

z = np.linspace(2,8,num=4, endpoint = 0)
print(z)
'''


'''x = np.empty([4,5],dtype=int)
#print(x)

x = np.empty([2,4])
print(x)'''

'''x = np.empty([3,2],dtype=int)
print(x)'''

'''x = np.empty([3,4],dtype=int)
print(x)'''

'''x = np.array([[5, 6], [7, 8]])
  
y = x.flatten()
  
print( y )
'''
'''x = np.array([[[5, 6, 8, 9], [17,18,19,20], [34,56,23,12]]])
  
y= x.flatten()
  
print( y )'''


'''x = np.array([1, 2, 3])

y = np.array([4, 5, 6])

z = np.concatenate((x, y))

print(z)
'''

'''x = np.array([[1, 2], [3, 4]])

y = np.array([[5, 6], [7, 8]])

z = np.concatenate((x, y), axis=0)
print(z)'''


'''x = np.array([1, 2, 3])

y = np.array([4, 5, 6])

z = np.stack((x, y))

print(z) '''

'''x = np.array([1, 2, 3])

y = np.array([4, 5, 6])

z = np.hstack((x, y))'''

#print(z)
'''Stacking Along Columns

NumPy provides a helper function: vstack()  to stack along columns.
Example
import numpy as np'''

'''x = np.array([1, 2, 3])

y = np.array([4, 5, 6])

z = np.vstack((x, y))

print(z)'''

'''import datetime

x = datetime.datetime.now()
print(x)'''

'''import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A")) # It will return week day name full version

print(x.strftime("%B")) # It will return Month name full version

print(x.strftime("%a")) # it will return day name in short version
print(x.strftime("%b")) # it will return month name in short version.
print(x.strftime("%C")) # It will return centuary.
print(x.strftime("%Y")) # It will return full version of year
print(x.strftime("%y")) # It will return shor version of year.
print(x.strftime("%X")) # Local version of time
print(x.strftime("%x")) # Local version of date'''

'''import calendar
   
year = 2022
month = 12
   
print(calendar.month(year, month))

#import calendar
   
print ("The calendar of year 2022 is : ")
print (calendar.calendar(2022))'''

'''a = ~8
print(a)
b = a+4
print(b)
'''
#print (calendar.calendar(2018, 2, 1, 6))

'''import matplotlib
from matplotlib import pyplot as plt 
import numpy as np
import pandas as pd

euro12=pd.read_csv('pan/Euro_2012_stats_TEAM.csv')
'''#print(euro12)

'''x = pd.Series([25,23,27,48,19])
print(x)
print(type(x))
print(len(x))
'''


'''x = pd.Series([1,2,3,4,5], index= ["one","Two","Three","Four","Five"])
print(x)
#print(x.dtype)
print(x.index)
'''
'''x = pd.Series(np.random.randint(5), index=["a", "b", "c", "d", "e"])
print(x)
print(x.index)
'''
x = pd.Series([34,45,76,23,89,98])
#print(x[1])

#Extracting Elements from back
'''x = pd.Series([34,45,76,23,89,98])
print(x[2:5])


x1 = pd.Series([10,20,30,40,50,60,70])
x2 = pd.Series([23,34,56,78,12,12,23])
z = x1+x2
print(z)

#print(x1+x2)
print(x1*x2)
print(x1/x2)
print(x1//x2)
print(x1-x2)'''

'''x = pd.DataFrame({"Name":["Deepak","Kanika","Samridhi","Hemlata"], "Marks": [78,67,92,87]})
print(x)
print(type(x))
print(len(x))
'''


'''x = pd.DataFrame({"Fruits":["apple","mango","banana"], "cost": [78,67,92], "quality" : 
    ["Good for health","sweet","yummy"]},index = ["a","b","c"])
print(x)


x = pd.DataFrame({"Fruits":["apple","mango","banana"], "cost": [78,67,92], "quality" : 
    ["Good for health","sweet","yummy"]},index = ["a","b","c"], 
    columns=["quality", "Fruits", "cost"])
print(x)
'''

'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])
print(x)
print(x.str.lower())
print(x.str.upper())
'''
'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])
print(x.str.len())
print(len(x))
'''
'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])
print(x.str.split())
'''
'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])

print (x.str.cat(sep='**'))
'''
'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek','Aryan'])
print (x.str.contains('ee'))
'''

'''x = pd.Series(['Ashish','Arvind','@Sahil','Deepak','Nikhil','Abhishek'])

#print (x.str.replace('@','**'))
print (x.str.replace('A','B'))
'''


'''x = pd.Series(['Ashish ','Arvind ','Sahil ','Deepak','Nikhil','Abhishek'])
print(x.str.repeat(3))
'''

'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])
print(x.str.count('e'))
#print(x.str.count('A'))
'''
'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])
print(x)
print(x.str.startswith ('A'))
'''
'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])
print(x.str.endswith ('l'))
'''
'''data = [1,1,1,3,3,3,3,4,4,4,2,2]
plt.hist(data)'''
#plt.show()


'''z = [1,1,2,2,2,3,3,3,3,4]
plt.hist(z,color="g")
plt.show()
'''
'''z = [1,1,2,2,2,3,3,3,3,4]
plt.hist(z,color='r',bins=4)

plt.show()
'''

'''Vegetables = ["Potato","Tomato","Brinjal","chilly"]
Cost= [64,34,100,56]
plt.pie(Cost,labels=Vegetables)
plt.show()
'''

'''Vegetables = ["Potato","Tomato","Brinjal","chilly","carrot"]
Cost= [64,34,100,56,78]
plt.pie(Cost,labels=Vegetables,autopct='%0.2f%%',colors=['yellow','grey','green','red','teal'])
plt.show()
'''

'''Vegetables = ["Potato","Tomato","Brinjal","chilly","carrot"]
Cost= [64,34,100,56,78]
#plt.pie(Cost,labels=Vegetables,radius=1)
plt.pie(Cost,labels=Vegetables,autopct='%0.1f%%',colors=['yellow','grey','green','red','blue'])
plt.pie([1],colors=['white'],radius=0.4)
plt.show()'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/iris.csv')
z=x.head(20)
print(z)
plt.hist(z['sepal_length'],color='g')
plt.show()
'''
#iris = pd.read_csv('iris.csv')
#print(iris.head())

'''plt.hist(x['petal_length'],color='r')
plt.show()
'''

'''class Parrot:
  def fly(self):
    print("Parrot can fly")
  def swim(self):
    print("Parrot can't swim")

class Penguin:
  def fly(self):
    print("Penguin can't fly")
  def swim (self):
    print("Penguin can swim")

def flying_test(self):
  self.fly()
  self.swim()

bird = Parrot()
Peggy = Penguin()

flying_test(bird)
flying_test(Peggy)'''


'''from abc import ABC,abstractmethod
class employee(ABC):
  def emp_id(self,id,name,age,salary):    
    pass
 
class employee1(employee):
  def emp_id(self,id):
    print("emp_id is",id)
 
emp1 = employee1()
emp1.emp_id(8)'''


'''x = np.array([1, 2, 3, 4, 5])
y = x.view()
x[1] = 18

print(x)
print(y)
'''



#print('hello')


# This is my addition program

'''a = 4 
b = 6 
z= a+b 
print(z)'''


'''a = 8 
b = 4 
c = a-b
print(c)

'''


import numpy as np 
'''x =  np.array([1,2,3,4,5])
    print(x)
    print(type(x))
    print(x.size)
    '''    


import numpy as np 

'''x = np.array([[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]]])
#print(type(x))
#print(x.ndim)
print(x[0][0][2][1:4])
'''


'''x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

print(x[x < 5])
'''
'''x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#z = (x>5) | (x == 5)
z = (x>5) & (x <16)'''






#z = (x<5) | (x > 16)    #if we want to get boolean value.
#z = (x<1) | (x > 16)





#z = x[(x>2) & (x < 11)]
#z = x[(x>1) & (x<16)]
#print(z)


x = np.array([[2,4,6],[1,3,5]])
#print(x)
'''y = np.cumsum(x)
print(y)
'''

'''x = np.array([[2,4,6],[1,3,5]])
print(x)
y = np.cumsum(x,axis=1)
print(y)
'''

'''x = np.array([[2,4,6],[1,3,5]])
#print(x)
y = np.cumsum(x,axis=0)
print(y)
'''

'''x = np.array([1, 2, 3, 4])
y = np.array([2, 3, 4, 2])
print(x*y)
'''


'''a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])  
b = np.array([2,4,6,8,10,12,14])  
c = a*b  
print(c)
'''


'''x = np.arange(6)
print(x)

x = np.arange(2,10)
print(x)

x = np.arange(1,10,2)
print(x)
'''


'''x= np.zeros(6)
print(x)
print(type(x))

x= np.ones(7)
print(x)

x = np.ones(3)
print(x)
print(type(x))
'''


'''x = np. array ([1,5,4,6,7,3j,5j],ndmin=3)
print(x)
'''

'''x = np.array([[[[[1,2,3,4,5]]]]])
print(type(x))
print(x.ndim)
'''

'''x = np.array([[[1,2,3,4,5],[6,7,8,9,10]]])
print(x)
print(x.shape)
'''


'''x = np.arange(6)
print(x)
y = x+2
print(y)
z = y*5
print(z)
'''

'''x = np.eye(2)
print(x)
'''

'''x = np.eye(5)
#print(x)

x = np.eye(6,8)
print(x)'''


'''x=20

if x < 50:
  print("True")

else:
  print("This is false")'''


#How can we take user input
 
'''x = int(input("Enter a number: "))
if x < 100:
  print("This is true")
elif x == 100:
  print("This is equal")
else:
  print("Nothing is true")'''


'''x = np.array([[[[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]]]]])
y=x.ndim
print(y)
'''
# Check size of an array
'''x = np.array([[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]]])
print(x.size)
'''
#Check the shape of an array
'''x = np.array([[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]]])
print(x.shape)
'''
# How can we insert dimension of an array

'''x = np. array ([1,5,4,6,7,3,5],ndmin=6)
print(x)
'''#print(x.dtype)


'''x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(x.shape)
print(x)
'''
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

#x1 = x.reshape(4, 3) #First parameter for row and second parameter for column
#print(x1)

#x1 = x.reshape(3,4)

#x1 = x.reshape(6,2)

#x1 = x.reshape(2,6)

'''x1=x.reshape(2,3,2)
print(x1)'''


x = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#print(x)
#print(x.transpose())
#print(x.T)


'''x = np.array([1, 2, 3, 4])
y = np.array([2, 3, 4, 2])
print(x*y)
'''
'''x = np.array([2,3,4,2])
y = 3
print(x*y)
'''
'''a = np.array([1,2,3,4,5,6,7])  
b = np.array([2,4,6,8,10,12,14])  
c = a*b  
print(c)
'''

'''a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])  
b = np.array([2,4,6,8,10,12,14])  
c = a*b  
print(c)
'''

'''x = np.array([[[2,3,4,2],[6,7,8,9],[10,11,12,13]]])
y = np.array([4,3,2,3])
z = x+y
print(z)
'''

'''x = np.array([10,6,2])
y = np.array([20,4,3])
z = np.sum([x,y])
print(z)
'''
#If I want to add these elements with respect to columns


'''x = np.array([10,12,2])
y = np.array([16,15,3])     #axis = 0 add these elements with respect to columns
z = np.sum([x,y], axis=0)
print(z)

'''
'''x = np.array([10,12,2])
y = np.array([16,15,3])     #axis = 1 add these elements with respect to rows
z = np.sum([x,y], axis=1)
print(z)
'''

'''x = np.array([12,13,14,15])
x = x+4
print(x)
'''

'''x = np.zeros((1,3))   # Two parameters here, one for row and three for columns.
#print(x)

x = np.ones((5,5)) # First parameter for row and second parameter for columns.
#print(x)


x = np.zeros((5,5))
#print(x)
x = x+2
#print(x)
x = x*3
print(x)'''


'''x = np. array ([1,5,4,6,7,3j,5j],ndmin=5)
print(x)
print(x.dtype)
'''


'''x = np.ones((1,3))
print(x)
'''
'''x = np.ones((5,5))
#print(x)
x = x+3
print(x)
'''

'''x = np.full((3,3),8)  #First parameter for row and second parameter for columns and third parameter
#print(x)        #for the matrix
x = x*2
print(x)
'''


'''x = np.zeros((2,6,5))
#print(x)
x=x+2
print(x)
'''


'''x = np.full((4,6),9)  # Two parameters are here, first is for row and second is for column
x=x*2
print(x)
'''

'''x = np.full((4,3,2),8)  # Three parameters are here first(4) is for matrix, second(3) is for 
              #row and 2 is for columns, fourth parameter the integer of the matrix.
#x = x+2
print(x)
'''

'''x = np.eye(5,5)
#print(x)

a = np.diag(x)            #It is fetching the diagonal elements
#print(a)
z=a+9
#print(z)
x = np.diagflat(z)
print(x)
'''
'''x = np.diagflat([[1,2,3,4],[5,6,7,8]])  
print(x)                     # This diagflat() shift these elements in the matrix as diagonal sequence
'''



'''x = np.diagflat([[1,2,3,4],[5,6,7,8]])  
print(x)                     # This diagflat() shift these elements in the matrix as diagonal sequence
'''


'''x = pd.Series(['Ashish','Arvind','SAhil','Deepak','NiAhil','Abhishek'])
print(x.str.swapcase())
'''
'''x = pd.Series(['Ashish','ARVIND','SAhil','DEEPAK','NiAhil','Abhishek'])
print(x.str.isupper())
'''


'''x = pd.DataFrame({"Fruits":["apple","mango","banana","papaya","apple","mango"],
 "cost": [78,67,92,87,78,67]})

#print(x)
x = x.drop_duplicates()
print(x)
'''

x = pd.read_csv('IRIS.csv')
#print(x)
#print(x.shape)
#print(x.head())
#print(x.tail())
#print(x.head(12))
#print(x.tail(10))
#print(x.describe())


'''x = pd.read_csv('IRIS.csv')
             y= x.iloc[2:11,2:5]
             print(y)                #first parameter represent the rows, and second parameter represent 
             '''             






                        #represent column.
'''y = x.iloc[5:11,2:]
print(y)

'''

'''x = open("q1.py", "r")
print(x.read())
'''
'''x = open("q1.py","rt")
print(x.read())
'''

'''z = np.linspace(4,8,num=4)
print(z)
'''
'''z = np.linspace(2,8,num=4)
print(z)
'''
'''z = np.linspace(3,10,num=5)
print(z)
'''
#retstep tells us what will be the space between the elements of an array.

'''z = np.linspace(3,10,num=5, retstep=True)
print(z)
'''
'''z = np.linspace(2.0,3.0,num=5, retstep=True)
print(z)
'''
'''z = np.linspace(2,8,num=4, retstep=True)
print(z)'''

# endpoint argument skip the last value.

'''z = np.linspace(2.0,3.0,num=5, endpoint = False)
print(z)
'''
'''z = np.linspace(2,8,num=4, endpoint = False)
print(z)'''

'''x = np.array([56,23,46,67,3,0])
a=x.argsort()
print(a)
'''
'''x = np.array([[5, 6], [7, 8]])
  
y = x.flatten()
  
print( y )
'''

'''x = np.array([1, 2, 3])

y = np.array([4, 5, 6])

z = np.concatenate((x, y))

print(z)
'''
#Join two 2-D arrays :

'''x = np.array([[1, 2], [3, 4]])    

y = np.array([[5, 6], [7, 8]])    #axis = 1 concatenate acording to column wise

z = np.concatenate((x, y), axis=1)

print(z)
'''
'''x = np.array([[1, 2], [3, 4]])

y = np.array([[5, 6], [7, 8]])    #axis = 0 concatenate acording to row wise

z = np.concatenate((x, y), axis=0)

print(z)'''


'''x = int(input("Enter a number: "))
y = 0
z = 0
while y < x:
   y+=1
   if y%2==0:
      print(y)
      z+=y
print(z)
'''

'''x = int(input("Enter a number: "))
z = 0
y = 0
while z < x:
   y+=1
   if y%2==0:
      print(y)
      z+=1
'''

'''x = int(input("Enter a number: "))
y = 0 
while y< 10:
  y+=1
  print(y*x)'''





'''Create a story and show the profit by region, show the sales by country, show the total percentage
  of the sales by bar graph, make a dashboard in this story.
  '''



'''x = np.array([1, 2, 3, 4, 5, 6])

y = np.array_split(x, 8)

print(y)
'''

'''x = np.array([1, 2, 3, 4, 5, 6])

y = np.array_split(x, 3)

print(y[2])
print(y[1])
print(y[0])
'''
x = np.array([[2,4,6],[1,3,5]])
#print(x)
'''y = np.cumsum(x)
print(y)
'''

'''x = np.array([[2,4,6],[1,3,5]])
#print(x)
y = np.cumsum(x,axis=1)
print(y)
'''

'''x = np.array([[2,4,6],[1,3,5]])
#print(x)
y = np.cumsum(x,axis=0)
print(y)
'''


'''x = np.array([1, 2, 3, 4, 5])

for i in x:
  print(i)
'''
#x = np.array([[[[[1, 2, 3], [4, 5, 6]]]]])

'''for i in x:
  for y in i:
    for z in y:
      for s in z:
        for t in s:

            print(t)'''


'''x = np.array([[[[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]]]])

for i in np.nditer(x):
  print(i)
'''

'''x = np.array([1, 2, 3, 4, 5])
y = x.copy()
x[1] = 18

print(x)
print(y)
'''
'''VIEW:

Make a view, change the original array, and display both arrays:

The view SHOULD be affected by the changes made to the original array.'''

'''x = np.array([1, 2, 3, 4, 5])
y = x.view()
y[1] = 18

print(x)
print(y)
'''

'''x = np.array([1, 2, 3, 4, 5, 4, 4])

y = np.where(x == 4)

print(y)
'''


'''x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

print(x[x < 5])
'''

#Find the number which is divisible by 2
'''x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

z = x[x%2==0] 
print("Number is divisible by 2: ", z)
'''


'''x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#z = x[(x>2) & (x < 11)]
z = x[(x>1) & (x<16)]
print(z)
'''

x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#z = x[(x<2) | (x>16)]
#z = x[(x<1) | (x>16)]
#print(z)

#z = (x>5) | (x == 5)
'''z = (x<5) | (x > 16)    #if we want to get boolean value.
z = (x<1) | (x > 16)
z = x[(x<1) | (x > 16)]
'''


'''x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#z = (x>5) | (x == 5)
z = (x<5) | (x > 16)
print(z)
'''

'''Create a matrix with the help of eye function (5) and add two with these digonal values and then
find the exponent of these values. ** should be 3.
'''
'''Create an array with the help of arange function range should be (16) and make a matrix with 4,4 
and then multiply 2 with this matrix, and then reshape this matrix and find the digonal values 
and 
then subtract 1 with these digonal values. 
'''


'''x = pd.DataFrame({'Name_1':['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'],'Eng':[99,78,98,87,97,67]})
#print(x)

y = pd.DataFrame({'Name_2':['Ashish','Tajesvi','Omkar','Nikhil','Abhishek','Rahul','Ranjeet'],'Math':[99,98,87,97,67,75,98]})
#print(y)

z=pd.merge(left=x, right=y, how='outer', left_on='Name_1',right_on='Name_2',indicator=True)
print(z)
'''

'''x = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two',

                           'two'],

                   'bar': ['A', 'B', 'C', 'A', 'B', 'C'],

                   'baz': [1, 2, 3, 4, 5, 6],

                   'zoo': ['x', 'y', 'z', 'q', 'w', 't']})

#print(x)
z=x.pivot(index='foo', columns='bar', values='baz')
print(z)
'''
'''z=x.pivot(index='foo', columns='bar')['baz']
print(z)
'''
#z=x.pivot(index='foo', columns='bar', values=['baz', 'zoo'])
#print(z)



'''z = open("g2.py","x")

z.write("  Honesty is the best policy********")
#z.write(" \n python is important for machine learning")
z = open("g2.py","r")                    #open and read the file after the appending:
print(z.read())
'''
'''import os
os.remove("koyal.py")
'''
'''import os
os.rmdir("C:/Users/shpoo/downloads/pooja")
'''

'''x = np.ones(5,6)  #First parameter for row and second parameter for columns and third parameter
print(x)        #for the matrix
x = x*2
print(x)
'''

#x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

#print(x[x < 5])
#print(x[x > 12])
#print(x[x >10])
#print(x[x<=5])

'''x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

z = x[x%2!=0] 
print("Number is divisible by 2: ", z)
'''
'''x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#z = x[(x>2) & (x < 11)]
z = (x>1) & (x<16)
print(z)
'''

'''x = pd.Series([25,23,27,48,19])
print(x)
print(type(x))
print(len(x))
'''

#x = pd.Series(["a","b","c","d","e"])
#print(x[4])
#print(x[1:4])

'''x = pd.Series([1,2,3,4,5], index= ["a","b","c","d","e"])
print(x)
'''

#x = pd.Series([1,2,3,4,5], index= ["a","b","c","d","e"])
#print(x)
#print(x["c"])
#print(x["b":"d"])



'''Extract 3
extract 2 to 4
'''

'''x = pd.Series(np.random.randint(100,1000,5), index=["a", "b", "c", "d", "e"])
print(x)
'''

'''student = pd.Series({"Name": "ABC", "Age": 12, "Roll no": 13})
print(student)
'''

'''x = pd.DataFrame({'Name_1':['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'],'Eng':[99,78,98,87,97,67]})
#print(x)

y = pd.DataFrame({'Name_2':['Ashish','Tajesvi','Omkar','Nikhil','Abhishek','Rahul','Ranjeet'],'Math':[99,98,87,97,67,75,98]})
#print(y)

z=pd.merge(left=x, right=y, how='outer', left_on='Name_1',right_on='Name_2',indicator=True)
print(z)'''


'''x=pd.DataFrame({'company':["google","google","yahoo","yahoo","Amazone","Amazone"],
  'person':['Akash','kajal','kiran','koyal','Anjali','Aman'],'sales_in_India'
  :[100,140,540,670,240,551]})

#print(x)
#print(type(x.groupby('company')))
z = (x.groupby('company'))


#print(z.std())
#print(z.min())
#print(z.mean())
#print(z.sum()) 
#print(z.count())
#print(z.describe())
#print(z.describe().transpose())  # It will change the position of data frame, row become column and column become row.
print(z.describe().transpose()['Amazone'])

'''

x = pd.read_csv('C:/Users/shpoo/Desktop/IRIS.csv')
#print(x)
#print(x.shape)
#print(x.head())
#print(x.tail())


#How can we extract the rows and columns from the data sets:
#use of .iloc[] method

'''y = x.iloc[20:41,0:]
print(y)


#use of .loc[] method

y = x.loc[4:12,('sepal_width','sepal_length')]
print(y)'''

#Aggregate functions:

#x = pd.read_csv('C:/Users/shpoo/Desktop/IRIS.csv')
#print(x)
#print(x.sum())
#print(x.min())
#print(x.max())
#print(x.count())
#print(x.std())
#print(x.mean())
#print(x.describe())


'''x = pd.DataFrame({"Fruits":["apple","mango","banana"], "cost": [78,67,92], "quality" : ["Good for health","sweet","yummy"]},index = [1,2,3], columns=["quality", "Fruits", "cost"])
x.to_csv('pppp.csv')
'''


'''x = pd.Series(["a","b","c","d","e"],index=[1,2,3,4,5])
print(x)
'''

'''x = pd.DataFrame({"Name":["Deepak","Kanika","Samridhi","Hemlata"], "Marks": [78,67,92,87]},index=["a","b","c","d"])
print(x)
print(type(x))
print(len(x))
'''

'''x = pd.DataFrame({"Fruits":["apple","mango","banana"], "cost": [78,67,92], "quality" : 
["Good for health","sweet","yummy"]},index = [1,2,3])
print(x)
'''


'''x = pd.DataFrame({"Fruits":["apple","mango","banana"], "cost": [78,67,92], "quality" : 
["Good for health","sweet","yummy"]},index = [1,2,3], columns=["quality", "Fruits", "cost"])
print(x)
'''

'''x = pd.DataFrame({"Fruits":["apple","mango","banana"], "cost": [78,67,92], "quality" : 
["Good for health","sweet","yummy"]},index = [1,2,3], row=["mango", "apple", "banana"])
print(x)
'''

'''x = pd.DataFrame({"Name":["kajal","Ritu","Priya"], "Marks": [78,67,92]}, index = [1,2,3])
y = pd.DataFrame({"Name":["Shivam","Sheenu","koyal"], "Marks": [56,34,89]}, index = [4,5,6])
z = (x,y)
w = pd.concat(z)
print(w)
'''
'''
x = pd.DataFrame({'Name_1':['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'],'Eng':[99,78,98,87,97,67]})
#print(x)

y = pd.DataFrame({'Name_2':['Ashish','Tajesvi','Omkar','Nikhil','Abhishek','Rahul','Ranjeet'],'Math':[99,98,87,97,67,75,98]})
#print(y)

z=pd.merge(left=x, right=y, how='outer', left_on='Name_1',right_on='Name_2',indicator=True)
print(z)
'''


#x = pd.read_csv('dataone.csv')
#print(x)

'''x.dropna(inplace=True)
print(x)'''

'''z=x.dropna()
print(z)
'''

'''x.fillna('abhishek', inplace = True)
print(x)
'''
# z is new dataframe

'''z=x.fillna(240)
print(z)
'''
'''x["Calories"].fillna(240000, inplace = True)
print(x)
'''
# It will not work here, it has no nan data

'''z=x["Calories"].fillna(240)
print(z)
'''
'''z=x.loc[7,'Duration'] = 45
print(z)
'''

'''x.dropna(inplace=True)
x['Date'] = pd.to_datetime(x['Date'])
print(x)
'''
#z=x.dropna()
#z['Date'] = pd.to_datetime(z['Date'])
#print(z)

#z=x.dropna()
#z['Date'] = pd.to_datetime(z['Date'])

'''z.loc[7,'Duration'] = 45
print(z)
'''

'''z=x.dropna()
z.loc[:,'date'] = pd.to_datetime(z.loc[:,'date'])
print(z)
'''

#x = pd.read_csv('dataone.csv')

#x = pd.read_csv('IRIS.csv')
#print(x)
'''z = x['species'].value_counts()
print(z)
'''
'''x = pd.read_csv('dataone.csv')
z = x['Duration'].count()
print(z)'''


'''x= pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/diamonds.csv')
y=x.head()
#print(y)
sns.distplot(x['price'],color="purple")
#sns.histplot(x['price'],color="b")'''




'''import pandas as ps
import seaborn as sns
x = pd.read_csv('weight-height.csv')
#print(x)
#print(x.head())
#print(x.shape)
#print(x.describe())
sns.histplot(x['Height'],kde=True)
#plt.show()
mean = x.Height.mean()
#print(mean)
std_deviation = x.Height.std()
#print(std_deviation)
z=mean - 3*std_deviation
#print(z)
y=mean + 3*std_deviation
#print(y)
w=x[(x.Height<54.82)]
#print(w)
#These are the outliers
w=x[(x.Height<54.82)|(x.Height>77.91)]
#print(w)

no_outlier = x [(x.Height<77) & (x.Height>54.82)]
#print(no_outlier)
print(no_outlier.shape)

'''

#Z Score: How many standard deviation away a datapoint is from mean.

#x = pd.read_csv('weight-height.csv')
#print(x)
#z=x.loc[0:,'Height']
#print(z)
#print(z.mean())

'''x=6.2+5.7+4.6+5.4+5.9+4.3+5.1+5.2+4.9
print(x.sum())
'''


#Manual Data Set:
'''Name  Height
Kajal 6.2
Koyal 5.7
Kiran 4.6
prem  5.4
Sheenu  5.9
Pihu  4.3
Tarun 5.1
Bharat  5.2
Veenu 4.9'''




'''x = pd.read_csv('pooja.csv')
#print(x)
z=x.loc[0:,'Height']
#print(z)
print(z.mean())
print(z.std())
'''
# Average = 5.25

#Standard Deviation = 0.61

#Z score  :  (6.2-5.25)/0.61=1.53


'''x = pd.read_csv('dataone.csv')
#print(x)
y = x.dropna()
#print(y)
y['Date'] = pd.to_datetime(y['Date'])
#print(y)

y.loc[7,'Duration'] = 45
print(y)
'''
'''x = pd.read_csv('dataone.csv')
#print(x)
y = x.fillna(240)
#print(y)
y.loc[7,'Duration'] = 45
#print(y)
'''
'''x = pd.DataFrame({"Fruits":["apple","mango","banana"], "cost": [78,67,92], "quality" : 
    ["Good for health","sweet","yummy"]},index = ["a","b","c"])
#print(x)

x.to_csv('rrr.csv')'''

'''x = pd.DataFrame({"Fruits":["apple","mango","banana"], "cost": [78,67,92], "quality" : 
    ["Good for health","sweet","yummy"]})'''
#print(x)

#x.to_csv('www.csv',index=False)



'''x = pd.DataFrame({"Fruits":["apple","mango","banana"], "cost": [78,67,92], "quality" : 
    ["Good for health","sweet","yummy"]})
#print(x)

x = pd.DataFrame()
'''
'''#x.to_excel('ATHREE.xlsx',index = False)

x = pd.read_excel('ATHREE.xlsx')
#print(x)

with pd.ExcelWriter('ATHREE.xlsx')as writer:

      x = pd.DataFrame({"Fruits":["apple","mango","banana","orange"], "cost": [78,67,92,45], "quality" : 
      ["Good for health","sweet","yummy","sour"]})
      x.to_excel(writer,sheet_name='Fruits_name in first sheet')

      x = pd.DataFrame({"Vegetables":["potatoes","Tomatoes","chilly","Brinjal"], "cost": [78,67,92,67], "quality" : 
      ["Good for health","sweet","yummy","tasty"]})
      x.to_excel(writer,sheet_name='Vegetables in second sheet')

      x = pd.DataFrame({"Name":["Kajal","Koyal","Kiran"], "Marks": [78,67,92]}, index = [1,2,3])
      x.to_excel(writer,sheet_name='Students marks in third sheet')


'''

'''x = pd.DataFrame()
      
#x.to_excel('gggggggg.xlsx')

x = pd.read_excel('gggggggg.xlsx')
#print(x)

with pd.ExcelWriter('gggggggg.xlsx')as writer:
      x = pd.DataFrame({"Fruits":["apple","mango","banana","orange"], "cost": [78,67,92,45], "quality" : 
      ["Good for health","sweet","yummy","sour"]})

      x.to_excel(writer,sheet_name='Fruits_name in first sheet')
      
      x = pd.DataFrame({"Vegetables":["potatoes","Tomatoes","chilly","Brinjal"], "cost": [78,67,92,67], "quality" : 
      ["Good for health","sweet","yummy","tasty"]})
      
      x.to_excel(writer,sheet_name='Vegetables in second sheet')

'''

'''x=pd.DataFrame({'company':["google","google","yahoo","yahoo","Amazone","Amazone"],
  'person':['Akash','kajal','kiran','koyal','Anjali','Aman'],'sales_in_India'
  :[100,140,540,670,240,551]})

print(x)

print(x.groupby('company'))
'''#print(type(x.groupby('company')))
#z = (x.groupby('company'))


#print(z.std())
#print(z.min())
#print(z.mean())
#print(z.sum()) 
#print(z.count())
#print(z.describe())
#print(z.describe().transpose())  # It will change the position of data frame, row become column and column become row.
#print(z.describe().transpose()['Amazone'])'''




'''x = pd.read_csv('matches.csv')
#print(x)

#print(x.groupby('city'))
z=x.groupby('city')
#print(z.sum())
print(z.max())
#print(z.describe())
'''

#x.to_excel('Book2.xlsx')



'''Drop any four rows from the data set.

Return 3 rows from the bottom.
Return 6 rows from the head.
Return any 15 rows from the mid 
find the mean,count,min,max from this dataset.


count the values of any two columns.
Take some data as you want and make a bar graph on this data.
Find the mean any specific column.

Drop any two colmns.
find two columns and six rows from the mid.

Show the number of rows and columns in the data set

Getting the frequency of most of the match awards

Getting the top 10 players with the most man of the match awards.
 
Finding out the number of toss wins w.r.t each team

Extracting the records where a team won batting first.

Make a bar plot for the top 5 players with most man of the match awards.

Making a pie chart for distribution of most wins after batting second.

Looking at the number of matches played each season.'''

#x=pd.read_csv('matches.csv')
#print(x)
#y = x.drop([4,5,6,8],axis=0)
#print(y)

#print(x.tail(3))
#print(x.head(6))
#y = x.iloc[300:315,0:]
#print(y)



'''x=iris.drop([4,5,6],axis=0)
print(x)'''


'''x=pd.DataFrame({'company':["google","google","yahoo","yahoo","Amazone","Amazone"],
  'person':['Akash','kajal','kiran','koyal','Anjali','Aman'],'sales_in_India'
  :[100,140,540,670,240,551]})

#print(x)

print(x.groupby('company'))
#print(type(x.groupby('company')))
z = (x.groupby('company'))


#print(z.std())
#print(z.min())
#print(z.mean())
e=z.sum()
e.to_csv('rrrr.csv')'''


'''import numpy

x = numpy.array ([1,2,3,4,5])
print(x)

print(type(x))
print(x.size)
'''

#print(len(x))'''

import numpy as np 

'''x = np.array((1,2,3,4,5,6,7,8))
print(x)
print(type(x))
print(x.size)
'''
'''x = np.array([1,2,3,4,5,6])
print(x)
print(type(x))
print(x.size)   

x = np.array({1,2,3,4,5})
print(x)
print(type(x))
print(x.size)'''

'''x = np.array({"name":"abc","Roll_no": 16, "school":"xyz"})
print(x)
print(type(x))
print(x.size)
'''

#DATA CLEANING:

#x = pd.read_csv("dataone.csv")
#print(x)

#Remove all rows with NULL values:

#inplace = True it means change into original data set
#Change into original dataset

'''x.dropna(inplace=True)
print(x)'''

#Its duplicate data set of original data set.

'''z=x.dropna()
print(z)'''

#x = pd.read_csv('dataone.csv')
#print(x)

'''Another way of dealing with empty cells is to insert a new value instead.

This way you do not have to delete entire rows just because of some empty cells.

The fillna() method allows us to replace empty cells with a value:

#replaces all empty cells in the whole Data Frame.'''

'''The fillna() method allows us to replace empty cells with a value:
Example'''

# x is original dataframe

'''x.fillna(240, inplace = True)
print(x)'''

# z is new dataframe
'''x = pd.read_csv('dataone.csv')

z=x.fillna(240)
print(z)'''

#x = pd.read_csv('dataone.csv')
#print(x)

# If you want to change in a specific column.

'''x["Calories"].fillna('apple,banana', inplace = True)
print(x)

# It will not work here, it has no nan data

z=x["Calories"].fillna('apple')
print(z)


Data of Wrong Format

Cells with data of wrong format can make it difficult, or even impossible, to analyze 
data.

To fix it, you have two options: remove the rows, or convert all cells in the columns 
into the same format.'''

#x = pd.read_csv('dataone.csv')

'''x.dropna(inplace=True)
x['Date'] = pd.to_datetime(x['Date'])
#print(x)

z=x.dropna()
z['Date'] = pd.to_datetime(z['Date'])
#print(z)

x.loc[7,'Duration'] = 45
print(x)

'''

'''x = pd.read_csv('dataone.csv')
#print(x)
y = x.dropna()
#print(y)
y['Date'] = pd.to_datetime(y['Date'])
#print(y)

y.loc[7,'Duration'] = 45
print(y)
'''

#x = pd.read_csv('matches.csv')
#print(x)
'''z=['winner'],value_counts()
print(z)'''

'''z=Season['result'],value_counts()
print(z)'''

'''y=x.loc(['player_of_match'],value_counts())
print(y)'''

'''y=x.value_counts('player_of_match')
print(y)
'''
'''z = x.value_counts('toss_winner')
print(z)'''

'''x = np.array([[[1,2,3,4,5]]])
print(type(x))
print(x.ndim)  #it represents the length of the array. means numbers of square brackets.
print(x.size)
'''
#x = pd.read_csv('matches.csv')
#print(x)
#print(x.head())

#Random sampling is one of the easiest forms of collecting data from the total population. Under random 
#sampling, each member of the population carries an equal opportunity of being chosen as a part of the 
#sampling process.
#Random sampling
#print(x.sample(200))

#Systemetic Sampling

'''Systematic Sampling

Systematic sampling is a probability sampling method where elements from a target population are chosen by selecting a random starting point and selecting sample members after a fixed ‘sampling interval.’ This is implemented easily by selecting each ‘N’th element. Systematic sampling ensures that the full population is represented fairly.

Here, we do systematic sampling, choosing every 10th element.'''

'''z=x.iloc[0:,5:16]
print(z)
'''

'''import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

#%matplotlib notebook

female_heights = np.random.normal(loc = 151.9, scale = 6, size = 16000)
male_heights = np.random.normal(loc = 164.9, scale = 7, size = 4000)

all_heights = np.append(female_heights, male_heights)
all_genders = ['F'] * 16000 + ['M'] * 4000

df = pd.DataFrame({'Gender': all_genders, 'Height': all_heights})
print(df.head())

plt.figure()
sns.distplot(pd.Series(female_heights, name = "Height(cm)"), hist = False, label = "Females",
             color='red', kde_kws={'linestyle': 'dotted'})
sns.distplot(pd.Series(male_heights, name = "Height(cm)"), hist = False, label = "Males", 
             color = 'blue', kde_kws={'linestyle': 'dotted'})
sns.distplot(all_heights, hist = False, label = "All", 
             color = 'green')

plt.gca().set_ylabel('Density(scaled)')
plt.gca().set_title('Distribution of heights - with sampling bias')
plt.legend()
plt.show()
'''


'''Take a data set and read this data set
find the first five rows
find last five rows
find the 23 rows from the mid of this data set
drop any two columns of this data set
drop 12, 34,45, 50 rows from this data set
find a one column and 14 row of this data set

find the sum, mean, std, count, min, max, and caluculate the all values.


create an excel sheet from this text editor and create six sheets on this excel sheet
on first sheet show the mean of this data set, on second sheet show the sum of this data set,
on third sheet show min value, fourth sheet show maximum value, fifth sheet perform all
aggregate functions. and on the sixth sheet sort this sheet according to a column.'''

'''x = pd.read_csv('iris.csv')
#print(x)
#print(x.shape)
y = x.drop([12,34,45,50],axis=0)
print(y)
print(y.shape)'''


#x = pd.read_csv('iris.csv')
#print(x)
#print(x.shape)

#print(x.head())
#print(x.head(12))
#print(x.tail())
#print(x.tail(10))

#z = x.iloc[0:6,2:4]
#print(z)

'''z = x.iloc[2, 2]
print(z)'''

'''z = x.loc[2:9,'sepal_width']
print(z)'''

'''z = x.loc[2:10,('petal_width','sepal_length')]
print(z)'''

'''z = x.drop([3,6,2],axis=0)
print(z)
'''
'''z = x.drop(['petal_length','sepal_length'],axis=1)
print(z)'''

#These are aggrigate functions

#print(x.sum())
#print(x.mean())
#print(x.min())
#print(x.max())
#print(x.count())
#print(x.std())
'''z = x.value_counts('sepal_length')
print(z)
'''
'''z = x.value_counts('species')
print(z)
'''

'''z = x.sort_values(by = 'petal_length')
#print(z)

z.to_csv('uuuuuuu.csv')
'''

'''y = x.sort_values(by='sepal_length')
print(y)
'''


#x = pd.read_csv('dataone.csv')
#print(x)

#It will change original datset

#x.dropna(inplace=True)
#print(x)


# It will change the duplicate data set
#z=x.dropna()
#print(z)


#x.fillna('satender', inplace=True)
#print(x)


'''z = x.fillna('satender')
print(z)
'''

# Change into specific column

'''x['Calories'].fillna(3000000, inplace=True)
print(x)
'''

'''z = x['Calories'].fillna(4000000)
print(z)
'''

'''x.dropna(inplace=True)
x['Date'] = pd.to_datetime(x['Date'])
'''#print(x)



'''z=x.dropna()
z['Date'] = pd.to_datetime(z['Date'])
print(z)
'''

'''x.dropna(inplace=True)
x['Date'] = pd.to_datetime(x['Date'])
x.loc[7,'Duration'] = 45
print(x)
'''


'''z=x.dropna()
z['Date'] = pd.to_datetime(z['Date'])
z = x.loc[7,'Duration'] =45
print(z)'''



'''x["Calories"].fillna(240000, inplace = True)
print(x)

# It will not work here, it has no nan data

z=x["Calories"].fillna(240)
print(z)'''




'''x.dropna(inplace=True)
print(x)

z=x.dropna()
print(z)
'''

'''iris.csv data set



Create three sheets on the excel and extract first to 15 row from this data set and show on first sheet
extract 20 row from mid and show in second sheet, extract two column and 30 row and show it 
on third sheet.'''

'''x= pd.read_csv('iris.csv')
#print(x)
z = x.head(15)
#print(z)

with pd.ExcelWriter('y9.xlsx')as writer:
  x = z
  x.to_excel(writer,sheet_name='15 rows from head')
  
  x.to_excel(writer,sheet_name='15 rows from head')

'''


#x = pd.DataFrame()

'''#x.to_excel('ATHREE.xlsx',index = False)



from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns'''


'''x = random.normal(loc=1, scale=2, size=(2, 3))

print(x) 


sns.distplot(random.normal(size=1000), hist=False)

plt.show() 
'''



'''x = random.binomial(n=10, p=0.5, size=10)

print(x)

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

plt.show() 
'''

'''x = pd.DataFrame({"Fruits":["apple","mango","banana"], "cost": [78,67,92], "quality" : 
    ["Good for health","sweet","yummy"]},index = ["a","b","c"])
print(x)

y = pd.DataFrame()
'''


'''x = pd.DataFrame({"Name":["Ashish","Arun","Anurag"], "Marks": [78,67,92],"Roll_no":[11,12,13]})
print(x)

y=pd.DataFrame(x)
y.insert(1,'School',['School_A','School_B','School_C'])

print(y)
'''

'''x = pd.DataFrame({"Name":["Ashish","Arun","Anurag"], "Marks": [78,67,92],"Roll_no":[11,12,13]})
print(x)
y=x.pop()
print(y)
'''


#Add a column in to the last of this DataFrame

'''x = pd.DataFrame({"Name":["Ashish","Arun","Anurag"], "Marks": [78,67,92]})
y = pd.DataFrame(x)

School = ['School_A','School_B','School_C']
y['School'] = School
print(y)
'''


# Add a column on the specific index.

'''x = pd.DataFrame({"Name":["Ashish","Arun","Anurag"], "Marks": [78,67,92],"Roll_no":[11,12,13]})
#print(x)

y=pd.DataFrame(x)
y.insert(2,'School',['School_A','School_B','School_C'])

print(y)
'''

#x = pd.read_csv('C:/Users/shpoo/Downloads/DS-EX3/DS-EX3/US_Crime_Rates_1960_2014.csv')
#print(x)
#print(x.head())

'''y = x.resample('year')
print(y)'''

'''z=x.groupby(pd.Year(freq = '10Y')).mean()
print(z)'''


'''a={"Name":["prince","priya","priyanshu"],"Year":[2020,2022,2021],"Rating":[9.2,8.5,7.7]}
x=pd.DataFrame(a)
#print(x)

x["Rating_Rank"]=x["Rating"].rank()
x=x.set_index["Rating_Rank"]
print(x)'''


'''x=pd.DataFrame({'company':["google","google","yahoo","yahoo","Amazone","Amazone"],
  'person':['Akash','kajal','kiran','koyal','Anjali','Aman'],'sales_in_India'
  :[100,140,540,670,240,551]})

#print(x)

#print(x.groupby('company'))
#print(type(x.groupby('company')))
z = (x.groupby('company'))
'''

#print(z.std())
#print(z.min())
#print(z.mean())
#print(z.sum()) 
#print(z.count())
#print(z.describe())
#print(z.describe().transpose())  # It will change the position of data frame, row become column and column become row.
'''s=z.describe().transpose()['Amazone']
d=z.describe().transpose()['google']
r=z.describe().transpose()['yahoo']



x.to_excel('aaaaa.xlsx')
x = pd.read_excel('aaaaa.xlsx')
#print(x)
with pd.ExcelWriter('aaaaa.xlsx')as writer:
  x = s
  x.to_excel(writer,sheet_name='Fruits_name in first sheet')
  x = d
  x.to_excel(writer,sheet_name='Fruits_name in first sheet')
  x = r
  x.to_excel(writer,sheet_name='Fruits_name in first sheet')
                                                                        
'''

      


'''with pd.ExcelWriter('output.xlsx')as writer:
  pihu.to_excel(writer,sheet_name='Sheet1')
  pihu.to_excel(writer,sheet_name='Sheet2')
  pihu.to_excel(writer,sheet_name='Sheet3')
  print(pihu)
  #print(pihu)'''

'''a={"Name":["prince","priya","priyanshu"],"Year":[2020,2022,2021],"Rating":[9.2,8.5,7.7]}
x=pd.DataFrame(a)
#print(x)

x["Rating_Rank"]=x["Rating"].rank()
x=x.set_index["Rating_Rank"]
print(x)'''


'''PIVOT FUNCTION

The pivot function in pandas is used to reshape the given data frame based on specific columns. 
Specified columns act as pivots of the data frame. An important thing to note is that the pivot 
function does not support data aggregation. Instead, multiple columns will return the data frame, 
becoming multi-indexed.


x = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two',

                           'two'],

                   'bar': ['A', 'B', 'C', 'A', 'B', 'C'],

                   'baz': [1, 2, 3, 4, 5, 6],

                   'zoo': ['x', 'y', 'z', 'q', 'w', 't']})

#print(x)

z=x.pivot(index='foo', columns='bar', values='baz')
#print(z)

z=x.pivot(index='foo', columns='bar')['baz']
#print(z)

z=x.pivot(index='foo', columns='bar', values=['baz', 'zoo'])
print(z)'''


'''from scipy.stats import kurtosis

x = [55, 78, 65, 98, 97, 60, 67, 65, 83, 65]

print(kurtosis(x))'''


'''import numpy.random as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


population_size = 1000000
population = np.rand(1000000)


number_of_samples = 10000
sample_means = np.rand(number_of_samples)
sample_size = 1

x = np.rand(number_of_samples)
for i in range(0,number_of_samples):
    x=np.randint(1,population_size,sample_size)
    sample_means[i] = population[x].mean()


plt.subplot(1,2,1)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
sns.distplot(sample_means,bins=int(180/5),hist = True,kde = False)
plt.title('Histogram of Sample mean')
plt.xlabel('Sample mean')
plt.ylabel('Count',fontsize=20)
plt.subplot(1,2,2)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
sns.distplot(sample_means,hist = False,kde = True)
plt.title('Density of Sample mean')
plt.xlabel('Sample mean')
plt.ylabel('Density',fontsize=20)
#plt.subplots_adjust(bottom=0.1, right=2, top=0.9)
plt.subplots_adjust(bottom=0.1, right=0.9, top=0.9)

plt.show()


x = [10,20,30,40,50,60,70,80,90]
a = [10,23,70,20,9,30,46,33,28]
b = [80,20,52,67,92,13,42,56,36]
plt.subplot(1,2,1)
plt.scatter(x,a,marker="*",color='g',s=150)
plt.title('Company Green')
plt.xlabel('Years from entity origin')
plt.ylabel('Revenue growth in percentage(%)')
plt.grid(True)
plt.subplot(1,2,2)
plt.scatter(x,b,marker=".",color='red',s=300)
plt.title('Company Red')
plt.xlabel('Years from entity origin')
plt.ylabel('Revenue growth in percentage(%)')
plt.grid(True)
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=0.4,hspace=0.4)
plt.show()'''




'''x = pd.DataFrame()
x.to_excel('U9.xlsx')

with pd.ExcelWriter('U9.xlsx')as writer:
  x = pd.DataFrame({"Name":["Kajal","Koyal","Kiran"], "Marks": [78,67,92]}, index = [1,2,3])
  x.to_excel(writer,sheet_name='Sheet1')
  x = pd.DataFrame({"Fruits":["Apple","Mango","Banana"], "Cost": [89,67,23]}, index = ["a","b","c"])
  x.iloc[0,1] = 900 # You can change in ur existing sheet like this.
  x.to_excel(writer,sheet_name='Sheet2')
  x = pd.DataFrame({"Vegetables":["Potato","Tomato","Peas"], "Cost": [34,56,78]}, index = ["A","B","C"])
  x.to_excel(writer,sheet_name='Sheet3')
  
'''
# Apply Loc or iloc [] method u can change in ur existing sheet.



#x = pd.DataFrame({"Name":["Ashish","Arun","Anurag"], "Marks": [78,67,92],"Roll_no":[11,12,13]})





#Create an excel sheet and perform these programs in different sheets
#Data set should be iris.csv
# find five row from top 
#find 10 rows from bottom.
#find 30 row from mid of this data set
#Apply describe method on 30 rows and perform it on different sheet.


'''x = pd.read_csv('iris.csv')
  #print(x)
  #print(x.head())
  z=x.head()
  y=x.tail(10)
  s = x.iloc[40:71,0:]
  w=s.describe()
  x.to_excel('ppppppp.xlsx')
  with pd.ExcelWriter('ppppppp.xlsx')as writer:
    x = z
    x.to_excel(writer,sheet_name='First Five Rows')
    x = y  
    x.to_excel(writer,sheet_name='Last Ten Rows ')
    x = s
    x.to_excel(writer,sheet_name='Mid Thirty Rows')
    x = w
    x.to_excel(writer,sheet_name='Show all aggregate functions')'''
    
      

'''x = pd.read_csv('iris.csv')
#print(x)
#print(x.head())
z=x.head()
y=x.tail(10)
s = x.iloc[40:71,0:]
w=s.describe()
x.to_excel('bbbbb.xlsx')
with pd.ExcelWriter('bbbbb.xlsx')as writer:
  z=x.head()
  x.to_excel(writer,sheet_name='First Five Rows')
  y=x.tail(10)  
  x.to_excel(writer,sheet_name='Last Ten Rows ')
  s=x.iloc[40:71,0:]
  x.to_excel(writer,sheet_name='Mid Thirty Rows')
  w=x.describe()
  x.to_excel(writer,sheet_name='Show all aggregate functions')

x = pd.read_excel('bbbbb.xlsx',sheet_name='First Five Rows')
print(x)
x = pd.read_excel('bbbbb.xlsx',sheet_name='Last')
print(x)
'''



#Now I am reading sheets one by one

'''x = pd.read_excel('abc.xlsx',sheet_name='Sheet1')
print(x)'''
'''x = pd.read_excel('abc.xlsx',sheet_name='Sheet2')
print(x)'''
'''x = pd.read_excel('abc.xlsx',sheet_name='Sheet3')
print(x)'''

#Now I will read all sheets together

'''x = pd.read_excel('abc.xlsx',sheet_name=['Sheet1','Sheet2','Sheet3'])  
print(x)'''


'''x = pd.DataFrame({"Name":["Ashish","Arun","Anurag"], "Marks": [78,67,92]})
#print(x)
y = pd.DataFrame(x)

School = ['School_A','School_B','School_C']
y['School'] = School
print(y)
'''

'''x = pd.DataFrame({"Name":["Ashish","Arun","Anurag"], "Marks": [78,67,92],"Roll_no":[11,12,13]})
#print(x)
y=pd.DataFrame(x)
y.insert(2,"School",['School_A','School_B','School_C'])
print(y)
'''

import numpy as np

'''x = 7,   8,   8,   9,   9,   9,   10,  11,  14,  14,  15,

y = np.mean(x)
print(y)
'''

'''x = 7,   8,   8,   9,   9,   9,   10,  11,  14,  14,  15,

y = np.median(x)
print(y)
'''

'''import scipy

x = 7,   8,   8,   9,   9,   9,   10,  11,  14,  14,  15,

y = stats.mod(x)

print(y)
'''


#check the dimensions of an array.

x = np.array([[[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]]]])
y=x.ndim
#print(y)



# Check size of an array
'''x = np.array([[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]]])
print(x.size)
'''
#Check the shape of an array
'''x = np.array([[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]]])
print(x.shape)'''


# How can we insert dimension of an array

'''x = np. array ([1,5,4,6,7,3,5],ndmin=5)
print(x)'''



#print(x.dtype)

'''x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(x.shape)
print(x)
'''
#This is two D dimensions

'''x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

x1 = x.reshape(4, 3) #First parameter for row and second parameter for column
#print(x1)

#x1 = x.reshape(3,4)

#x1 = x.reshape(6,2)

x1 = x.reshape(2,6)
#print(x1)


x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

x1 = x.reshape(2,3,2)

print(x1)'''


'''x = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#print(x)
#print(x.transpose())

x = np.array([[10,20,30,40],[50,60,70,80]])
#print(x)
print(x.T)'''

'''x = np.array([2,3,4,5,6])
y = np.array([2,7,8,9,10])
#print(x*y)
z = x*y
print(z)
'''
'''x = np.array([2,3,4,5,6])
y = 2
#print(x+y)
z = x+y 
print(z)'''


'''x = np.array([[2,3,4,5,6],[4,5,3,2,1]])
y = np.array([2,3,4,5,3])
print(x+y)'''


'''x = np.array([[2,3,4,5,6],[7,8,9,10,11]])
y = np.array([[6,5,4,3,2],[10,11,9,8,7]])
print(x+y)
'''
'''x = np.array([[2,3,4,5,6],[7,8,9,10,11]])
y = 8
print(x*y)'''

'''x = np.array([2,3,4,5,6])
y=np.array([4,3])
print(x*y)'''

'''x = np.array([10,11,12,13])
y = np.array([11,12,13,14])
z =np.sum([x,y])
print(z)
'''

'''x = np.array([10,12,2])
y = np.array([16,15,3])     #axis = 1 add these elements with respect to rows
z = np.sum([x,y], axis=1)
print(z)
'''

'''x = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two',

                           'two'],

                   'bar': ['A', 'B', 'C', 'A', 'B', 'C'],

                   'baz': [1, 2, 3, 4, 5, 6],

                   'zoo': ['x', 'y', 'z', 'q', 'w', 't']})

#print(x)

z=x.pivot(index='foo', columns='bar', values='baz')
#print(z)

z=x.pivot(index='foo', columns='bar')['baz']
#print(z)

z=x.pivot(index='foo', columns='bar', values=['baz', 'zoo'])
print(z)'''




'''x = pd.DataFrame({'Name': ["Akash","Akash","Akash","Bhanu","Bhanu","Bhanu","Rahul","Rahul","Rahul"],
  'Subjects':['Python','Maths','Science','Python','Maths','Science','Python','Maths','Science'],
  'Marks' :[65,79,89,55,78,90,112,82,77]})
#print(x)
z=x.pivot(index = 'Name', columns = 'Subjects', values='Marks')
print(z)'''


'''x = pd.DataFrame({'Name': ["Akash","Bhanu","Rahul","Akash","Bhanu","Rahul","Akash","Bhanu","Rahul"],'Subjects':['Python','Maths','Science','Python','Maths','Science','Python','Maths','Science'],'Marks' :[65,79,89,78,89,100,39,44,58]})
#print(x)
z=x.pivot(index = 'Subjects', columns = 'Name', values='Marks')
print(z)'''



'''import libraries as per ur requirement.
Take any one data set 
find top 20 rows from data set
Extract bottom 10 row from data set
Extract any two column from data set
Extract 20 rows from the mid of data set'''


'''import pandas as pd
from numpy.random import randint
  
dict = {'Name':['Martha', 'Tim', 'Rob', 'Georgia'],
        'Maths':[87, 91, 97, 95],
        'Science':[83, 99, 84, 76]
       }
  
df = pd.DataFrame(dict)
  
#print(df)
  
df.loc[len(df.index)] = ['Amy', 89, 93] 
  
print(df)'''

#x =np.zeros((5,5))
#print(x)

'''x = np.ones((4,3))
z=x+4
y=z*2
print(y)
'''

'''x = np.full((4,5),8)
print(x*4)'''


'''x = np.random.randint(100,1000,5)
print(x)'''


'''x =np.full((5,5,),100)
print(x)'''

'''x= np.eye(4,4)
#print(x)

a=np.diag(x)
print(a+7)'''

'''x = np.diagflat([[1,2,3,4],[5,6,7,8]])  
#print(x)                     # This diagflat() shift these elements in the matrix as diagonal sequence
a = np.diag(x)
print(a)
'''

'''x = np.eye(5,4)
#print(x)
y = np.fliplr(x)
print(y)'''



'''x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])
z = np.concatenate((x,y))
print(z)'''


'''x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
z = np.concatenate((x,y),axis=0)
print(z)'''


'''x = np.array([1,2,3,4])
y =np.array([5,6,7,8])
z =np.stack((x,y),axis=0)
print(z)
'''

'''x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
z = np.hstack((x,y))
#print(z)

x = np.array([10,20,30,40])
y = np.array([50,60,70,80])
z = np.vstack((x,y))
print(z)'''


'''x = pd.DataFrame({"Name":['Anu','Ashu','Aniket'],"Marks":[34,56,78],"Roll_no":[1,2,3]})
#print(x)

x.loc[len(x.index)] = ['Kirti',99,4]
print(x)'''


'''import pandas as pd
from numpy.random import randint
  
dict = {'Name':['Martha', 'Tim', 'Rob', 'Georgia'],
        'Maths':[87, 91, 97, 95],
        'Science':[83, 99, 84, 76]
       }
  
df = pd.DataFrame(dict)
  
#print(df)
  
df.loc[len(df.index)] = ['Amy', 89, 93] 
  
print(df)'''


#How can we replace a row.

'''x = pd.DataFrame({"Name":['Anu','Ashu','Aniket','Shreya'],"Marks":[34,56,78,88],"Roll_no":[1,2,3,4]})
#print(x)
x .loc[1]=['koyal',87,2]
#x.loc[len(x.index)] =['koyal',66,2]
print(x)'''



#How Can We insert a row in a specific index.

import warnings
warnings.filterwarnings('ignore')

'''x = pd.DataFrame({"Name":['Anu','Ashu','Aniket','Shreya'],"Marks":[34,56,78,88],"Roll_no":[1,3,4,5]})
#print(x)

#y = x[0:1]
#y.loc[1]=['koyal',87,2]
#print(y)'''
'''z=x.loc[1:]
#print(z)
A = pd.concat([y,z],ignore_index=True)
A.reset_index()
print(A)'''

'''y = x.iloc[0:1]
#print(y)
y.loc[1]=['Koyal',87,2]
#print(y)
z =x.loc[1:]
#print(z)
A=pd.concat([y,z],ignore_index = True)
A.reset_index()
print(A)'''


'''x = pd.DataFrame({"Name":['Anu','Ashu','Aniket','Shreya'],"Marks":[34,56,78,88],"Roll_no":[1,3,4,5]})
#print(x)

y = x.iloc[0:1]
#print(y)
y.loc[1]=['Koyal',87,2]
#print(y)
z =x.loc[1:]
#print(z)
A=pd.concat([y,z],ignore_index = True)
A.reset_index()
print(A)'''


import matplotlib
from matplotlib import pyplot as plt 
import numpy as np
import pandas as pd

#How can se create a line plot

'''x = np.arange(1,11)
y = 2*x
print(x)
print(y)
plt.plot(x,y)
plt.show()
'''


'''x = np.arange(1,11)
y = 2*x
print(x)
print(y)
plt.plot(x,y)
plt.title("SimpleLine Plot")
plt.xlabel("data on x-axis")
plt.ylabel("data on y-axis")
plt.show()
'''


'''x = np.arange(1,11)
y = 2*x
print(x)
print(y)
plt.plot(x,y,color='red',linestyle = ':', linewidth = 5)
plt.title("SimpleLine Plot")
plt.xlabel("data on x-axis")
plt.ylabel("data on y-axis")
plt.show()
'''

'''x = np.arange(1,11)
y1 = 2*x
y2 = 3*x
print(y1)
print(y2)
plt.plot(x,y1,color='orange',linestyle = ':', linewidth = 5)
plt.plot(x,y2,color='g',linestyle = '-.', linewidth = 5)
plt.title("Two Lines in one Plot")
plt.xlabel("range")
plt.ylabel("two lines")
plt.grid(True)
plt.show()
'''



'''x = np.arange(1,11)
y1=2*x
y2=3*x
print(y1)
print(y2)

# first parameter for row and second for columns and third parameter shows this is first sub plot.


plt.subplot(1,2,1)  # first parameter for row and second for columns and third parameter shows this is first sub plot.

plt.plot(x,y1,color='green',linestyle=':',linewidth=2)

plt.subplot(1,2,2)  # first parameter for row and second for columns and third parameter shows this is second sub plot.

plt.plot(x,y2,color='brown',linestyle=':',linewidth=5)

plt.show()
'''


'''x = pd.DataFrame({"Name":["Ashish","Arun","Anurag"], "Marks": [78,67,92]})
#print(x)
y = pd.DataFrame(x)

School = ['School_A','School_B','School_C']
y['School'] = School
print(y)
'''

'''x = pd.DataFrame({"Name":["Ashish","Arun","Anurag"], "Marks": [78,67,92],"Roll_no":[11,12,13]})
#print(x)
y=pd.DataFrame(x)
y.insert(2,"School",['School_A','School_B','School_C'])
print(y)
'''

#How can we add new row in an existing DataFrame.

'''x = pd.DataFrame({"Name":['Anu','Ashu','Aniket','Shreya'],"Marks":[34,56,78,88],
  "Roll_no":[1,2,3,4]})
#print(x)
x .loc[4]=['koyal',87,5]
print(x)
'''

#How can we replace a row in an existing DataFrame.

'''x = pd.DataFrame({"Name":['Anu','Ashu','Aniket','Shreya'],"Marks":[34,56,78,88],
  "Roll_no":[1,2,3,4]})
#print(x)
x .loc[2]=['koyal',87,5]
print(x)
'''


'''x = pd.DataFrame({"Name":['Anu','Ashu','Aniket','Shreya'],"Marks":[34,56,78,88],
  "Roll_no":[1,3,4,5]})
#print(x)

y = x.iloc[0:1]
#print(y)
y.loc[1]=['Koyal',87,2]
#print(y)
z =x.loc[1:]
#print(z)
A=pd.concat([y,z],ignore_index = True)
A.reset_index()
print(A)
'''

'''x=pd.DataFrame({'company':["google","google","yahoo","yahoo","Amazone","Amazone"],
  'person':['Akash','kajal','kiran','koyal','Anjali','Aman'],'sales_in_India'
  :[100,140,540,670,240,551]})

print(x)

print(x.groupby('company'))
#print(type(x.groupby('company')))
z = (x.groupby('company'))


#print(z.std())
#print(z.min())
#print(z.mean())
#print(z.sum()) 
#print(z.count())
#print(z.describe())
#print(z.describe().transpose())  # It will change the position of data frame, row become column and column become row.
print(z.describe().transpose()['Amazone'])'''


'''x=pd.DataFrame({'School':["School_A","School_A","School_B","School_B","School_C","School_C"],
  'Students':['Akash','kajal','kiran','koyal','Anjali','Aman'],'Marks'
  :[100,140,540,670,240,551]})'''

#print(x)

#print(x.groupby('School'))
#print(type(x.groupby('School')))
#z = (x.groupby('School'))


#print(z.std())
#print(z.min())
#print(z.mean())
#print(z.sum()) 
#print(z.count())
#print(z.describe())
#print(z.describe().transpose())  # It will change the position of data frame, row become column and column become row.
'''a=z.describe().transpose()['School_A']
b=z.describe().transpose()['School_B']
c=z.describe().transpose()['School_C']
#print(a)

x.to_excel('Performance.xlsx')
 
with pd.ExcelWriter('Performance.xlsx')as writer:
  x=a
  x.to_excel(writer,sheet_name='School_A Performance')
  x=b 
  x.to_excel(writer,sheet_name='School_B Performance ')
  x=c
  x.to_excel(writer,sheet_name='School_C Performance')'''
 

#Take a data set and



'''Create a program and make a data frame for students performance, 4 school should be 
there
and take student as per your requirement. and present the performace of school. Do 
Group by this 
data frame according to school and make some sheets on the excel and perform all 
aggregate functions on each sheet.'''

'''x = pd.read_csv('iris.csv')
#print(x)
#print(x.head())
z=x.head()
y=x.tail(10)
s = x.iloc[40:71,0:]
w=s.describe()
x.to_excel('bbbbb.xlsx')
with pd.ExcelWriter('bbbbb.xlsx')as writer:
  z=x.head()
  x.to_excel(writer,sheet_name='First Five Rows')
  y=x.tail(10)  
  x.to_excel(writer,sheet_name='Last Ten Rows ')
  x.iloc[2,3]='Khushi'
  x.to_excel(writer,sheet_name='Mid Thirty Rows')
  w=x.describe()
  x.to_excel(writer,sheet_name='Show all aggregate functions')'''


'''student = {"kajal":87, "Arun": 56, "kiran":27}
a = list(student.keys())
b = list(student.values())
print(a)
print(b)
plt.bar(a,b)
plt.show()
'''

'''x = [4,5,1,6,2,3,7,8]
y = [80,10,40,50,34,20,80,30]
plt.scatter(x,y,color='g')
plt.title('scatter plot')
plt.xlabel('Years from starting of entity')
plt.ylabel('Revenue Growth in Percent(%)')
plt.grid(True)
plt.show()
'''
'''x = [4,5,1,6,3,5,8]
y = [8,1,4,5,2,8,3]
plt.scatter(x,y,marker="*",color='g',s=150)
plt.title('scatter plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()
plt.show()'''

'''x = [10,20,30,40,50,60,70,80,90]
a = [8,1,7,2,0,3,7,3,2]
b = [7,2,5,6,9,1,4,5,3]
plt.scatter(x,a,marker="*",color='g',s=150)
plt.scatter(x,b,marker=".",color='orange',s=200)
plt.title('scatter plot')
plt.show()'''



'''x = [10,20,30,40,50,60,70,80,90]
a = [10,23,70,20,9,30,46,33,28]
b = [80,20,52,67,92,13,42,56,36]
plt.subplot(1,2,1)
plt.scatter(x,a,marker="*",color='g',s=150)
plt.title('Company Green')
plt.xlabel('Years from entity origin')
plt.ylabel('Revenue growth in percentage(%)')
plt.grid(True)
plt.subplot(1,2,2)
plt.scatter(x,b,marker=".",color='red',s=300)
plt.title('Company Red')
plt.xlabel('Years from entity origin')
plt.ylabel('Revenue growth in percentage(%)')
plt.grid(True)
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=0.4,hspace=0.4)
plt.show()
'''

'''z = [1,1,2,2,2,3,3,3,3,4]
plt.hist(z,color="g")
plt.show()
'''


'''iris = pd.read_csv('iris.csv')
#print(iris)
#print(iris.head())

plt.hist(iris['sepal_length'],bins=30,color='g')
plt.show()'''


'''x = pd.Series(["a","b","c","d","e"])
y=x.iloc[-4]
print(y)
'''


#Now I am reading sheets one by one

'''x = pd.read_excel('abc.xlsx',sheet_name='Sheet1')
print(x)
'''
'''x = pd.read_excel('abc.xlsx',sheet_name='Sheet2')
print(x)'''
'''x = pd.read_excel('abc.xlsx',sheet_name='Sheet3')
print(x)'''

#HOW CAN I READ EXCEL SHEET ONE BY ONE, AND HOW CAN I READ ALL EXCEL SHEETS TOGETHER.


'''x = pd.read_csv('iris.csv')
#print(x)
z=x.head()
y=x.tail()
w=x.iloc[1:30,2:4]
x.to_excel('aaaaaaaaaaa.xlsx')
with pd.ExcelWriter('aaaaaaaaaaa.xlsx')as writer:
  x=z
  x.to_excel(writer,sheet_name='First Five Rows')
  x=y 
  x.to_excel(writer,sheet_name='Bottom five Rows')
  x=w 
  x.to_excel(writer,sheet_name='Two columns')

x = pd.read_excel('aaaaaaaaaaa.xlsx',sheet_name='First Five Rows')
print(x)

x = pd.read_excel('aaaaaaaaaaa.xlsx',sheet_name='Bottom five Rows')
#print(x)

x = pd.read_excel('aaaaaaaaaaa.xlsx',sheet_name='Two columns')
#print(x)

#Now I will read all sheets together

x = pd.read_excel('aaaaaaaaaaa.xlsx',sheet_name=['First Five Rows','Bottom five Rows','Two columns'])  
#print(x)'''


'''Vegetables = ["Potato","Tomato","Brinjal","chilly"]
Cost= [64,34,100,56]
plt.pie(Cost,labels=Vegetables)
plt.show()'''

'''Vegetables = ["Potato","Tomato","Brinjal","chilly","carrot"]
Cost= [64,34,100,56,78]
plt.pie(Cost,labels=Vegetables,autopct='%0.2f%%',colors=['yellow','grey','green','red','blue'])
plt.show()
'''


'''Vegetables = ["Potato","Tomato","Brinjal","chilly","carrot"]
Cost= [64,34,100,56,78]
plt.pie(Cost,labels=Vegetables,radius=1)
plt.pie(Cost,labels=Vegetables,autopct='%0.1f%%',colors=['yellow','grey','green','red','blue'])
plt.pie([1],colors=['w'],radius=0.4)
plt.show()
'''
import seaborn as sns

'''x = sns.load_dataset("fmri")
y=x.head()
print(y)
sns.lineplot(x="timepoint",y = "signal",data=x)
plt.show()
'''

'''x = sns.load_dataset("fmri")
#y=x.head(40)
print(x)
sns.lineplot(x="timepoint",y = "signal",data=x,hue="event")
plt.show()
'''

'''x = pd.read_csv('iris.csv')
#print(x)
z=x.head()
y=x.tail()
w=x.iloc[1:30,2:4]

x.to_excel('Akansha.xlsx')
#print(x)

with pd.ExcelWriter('Akansha.xlsx')as writer:
  x=z
  x.to_excel(writer,sheet_name='First Five Rows')
  x=y 
  x.iloc[4,2]='APPLE'
  x.to_excel(writer,sheet_name='Bottom five Rows')
  x=w 
  x.to_excel(writer,sheet_name='Two columns')

x = pd.read_excel('Akansha.xlsx',sheet_name='First Five Rows')
#print(x)

x = pd.read_excel('Akansha.xlsx',sheet_name='Bottom five Rows')
#print(x)

x = pd.read_excel('Akansha.xlsx',sheet_name='Two columns')
#print(x)

#Now I will read all sheets together

x = pd.read_excel('Akansha.xlsx',sheet_name=['First Five Rows','Bottom five Rows',
  'Two columns'])  
print(x)'''


'''x = np.arange(1,11)
y = 2*x
print(x)
print(y)
plt.plot(x,y)
plt.show()
'''
'''x = np.arange(1,11)
y = 2*x
print(x)
print(y)
plt.plot(x,y)
plt.title("SimpleLine Plot")
plt.xlabel("data on x-axis")
plt.ylabel("data on y-axis")
plt.show()
'''

'''x = np.arange(1,11)
y1 = 2*x
y2 = 3*x
print(y1)
print(y2)
plt.plot(x,y1,color='orange',linestyle = ':', linewidth = 5)
plt.plot(x,y2,color='g',linestyle = '-.', linewidth = 5)
plt.title("Two Lines in one Plot")
plt.xlabel("range")
plt.ylabel("two lines")
plt.grid(True)
plt.show()
'''
import seaborn as sns
'''x = sns.load_dataset("C:/Users/shpoo/Desktop/Datasets/ONE/Boston")
print(x)
'''#y=x.head()



x = sns.load_dataset("fmri")
'''y=x.head()
#print(y)
sns.lineplot(x="timepoint",y = "signal",data=x)
plt.show()
'''

'''sns.lineplot(x="timepoint",y = "signal",hue="event",style="event",markers=True,data=x)
plt.show()
'''

'''x=pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/pokemon.csv')
y=x.head()
#print(y)
sns.set(style = "whitekgrid")
sns.barplot(x="Legendary",y="Speed",data=x)
plt.show()
'''


'''x=pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/pokemon.csv')
print(x)
sns.set(style = "whitegrid")
sns.barplot(x="Legendary",y="Speed",hue = "Generation",data=x)
plt.show()
'''

'''x=pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/pokemon.csv')
y=x.head()
#print(y)
sns.set(style = "whitegrid")
sns.barplot(x="Legendary",y="Speed",data=x, color='orange')
plt.show()
'''

'''x = pd.read_csv('iris.csv')
y=x.head()
print(y)
sns.scatterplot(x = 'sepal_length',y = 'petal_length',data=x,hue='species',style='species')
plt.show()
'''

'''x = pd.read_csv('iris.csv')
y=x.head()
#print(y)
sns.scatterplot(x = 'sepal_length',y = 'petal_length',data=x,hue="petal_length",style="species")
plt.show()
'''

'''x = ['apple','mango','pineapple',56,56,45,89]
#print(x)
y =x.index(56)
print(y)'''


#I want to stack both sub plots row swise

'''x = np.arange(1,11)
y1=2*x
y2=3*x
print(y1)
print(y2)

# first parameter for row and second for columns and third parameter shows this is first sub plot.


plt.subplot(1,2,1)  # first parameter for row and second for columns and third parameter shows this is first sub plot.

plt.plot(x,y1,color='green',linestyle=':',linewidth=2)

plt.subplot(1,2,2)  # first parameter for row and second for columns and third parameter shows this is second sub plot.

plt.plot(x,y2,color='brown',linestyle=':',linewidth=5)

plt.show()
'''
'''x = np.arange(1,11)
y1=2*x
y2=3*x

plt.subplot(2,1,1)  # first parameter for row and second for columns and third parameter shows this is first sub plot.
plt.plot(x,y1,color='red',linestyle=':',linewidth=2)

plt.subplot(2,1,2)  # first parameter for row and second for columns and third parameter shows this is second sub plot
plt.plot(x,y2,color='brown',linestyle=':',linewidth=2)

plt.show()
'''

'''student = {"kajal":87, "Arun": 56, "kiran":27}
a = list(student.keys())
b = list(student.values())
print(a)
print(b)
plt.bar(a,b)
plt.show()
'''
'''Vegetables_basket = {"Brinjal":100, "Potatos": 145, "Tomatoes": 123}
Vegetables_names=list(Vegetables_basket.keys())
Vegetables_cost=list(Vegetables_basket.values())
plt.barh(Vegetables_names,Vegetables_cost,color = 'teal')
plt.title("Bar Plot")
plt.xlabel("Vegetables_cost")
plt.ylabel("Vegetables_names")
#plt.grid()
plt.show()
'''


'''x=[10,20,30,40,50,60,70,80,90]
y=[8,1,7,2,0,3,7,3,2]
plt.scatter(x,y)
plt.show()
'''

'''x = [4,5,1,6,3,5,8]
  y = [8,1,4,5,2,8,3]
  plt.scatter(x,y,marker="*",color='g',s=500)
  plt.title('scatter plot')
  plt.xlabel('x-axis')
  plt.ylabel('y-axis')
  plt.grid()
  plt.show()'''

'''x = [10,20,30,40,50,60,70,80,90]
a = [8,1,7,2,0,3,7,3,2]
b = [7,2,5,6,9,1,4,5,3]
plt.scatter(x,a,marker="*",color='g',s=500)
plt.scatter(x,b,marker=".",color='orange',s=150)
plt.title('scatter plot')
plt.show()
'''

#How can we calculate T-test sample one



import scipy.stats as stats
import pandas as pd

'''x = pd.Series([1000,1500, 2300, 3540, 4120, 4560, 5490, 3460, 4750, 2300, 9000, 8600, 7100])

m =x.mean()
#print(m)

x.to_csv("area.csv")
x=pd.read_csv('area.csv')
#print(y)'''
#x = pd.Series([1000,1500, 2300, 3540, 4120, 4560, 5490, 3460, 4750, 2300, 9000, 8600, 7100])
#print(x)
#m = np.mean(x)
#print(m)
'''t_statistic, p_value = stats.ttest_1samp(a=x,popmean=m)
print(t_statistic,p_value)
'''

'''NOTE: 
As the p_value for the given problem is more than 0.05 which is the alpha value, 
we accept the null hypothesis and the alternative hypothesis is rejected.
'''


 
# There is two groups of school students and we find that x group student height is 
#the same height of group y. So let me apply t-test sample two.

'''x = np.array([14, 15, 15, 16, 13, 8, 14,17, 16, 14, 19, 20, 21, 15,
              15, 16, 16, 13, 14, 12])
 
y = np.array([15, 17, 14, 17, 14, 8, 12, 19, 19, 14, 17, 22, 24, 16,
              13, 16, 13, 18, 15, 13])
 

z = stats.ttest_ind(a=x, b=y, equal_var=True)
print(z)'''


'''Analyzing the result:

Two sample t-test has the following hypothesis:

    H0 => µ1 = µ2 (population mean of dataset x is equal to dataset y)

    HA => µ1 ≠µ2 (population mean of dataset x is different from dataset y)

Here, since the p-value (0.53004) is greater than alpha = 0.05 so we cannot 
reject the null hypothesis of the test. We do not have sufficient evidence to say 
that the mean height of students between the two data groups is different.'''




'''x = [88, 82, 84, 93, 75, 78, 84, 87,
       95, 91, 83, 89, 77, 68, 91]
  
y = [91, 84, 88, 90, 79, 80, 88, 90, 
        90, 96, 88, 89, 81, 74, 92]


z=stats.ttest_rel(x, y)
print(z)'''

'''The test statistic comes out to be equal to 2.9732 and the corresponding two-sided 
p-value is 0.010.

Analyzing the output.

The paired samples t-test follows the null and alternative hypotheses:

    H0: It signifies that the mean pre-test and post-test scores are equal
    HA: It signifies that the mean pre-test and post-test scores are not equal

As the p-value comes out to be equal to 0.010 which is less than 0.05 hence we reject 
the null hypothesis. So, we have enough proof to claim that the true mean test score 
is different for cars before and after applying the different engine oil.
'''

'''t=np.var(x)
print(t)
s=np.var(y)
print(s)
'''#The var. equal argument indicates whether or not to assume equal variances when 
#performing a two-sample t-test.
# Perform the two sample t-test with equal variances


  
# loading the csv file
'''data = pd.read_csv('areas.csv')
  
# perform one sample t-test
t_statistic, p_value = stats.ttest_1samp(a=data, popmean=5000)
print(t_statistic , p_value)
'''

'''1000
1500
2300
3540
4120
4560
5490
3460
4750
2300
9000
8600
7100'''


'''x = [32, 36, 46, 47, 56, 69, 75, 79, 79, 88, 89, 91, 92, 93, 96, 97, 
          101, 105, 112, 116]
    
  # First quartile (Q1)
  a = np.median(x[:10])
  #print(a)
  
  # Third quartile (Q3)
  b = np.median(x[10:])
  #print(b)
    
  # Interquartile range (IQR)
  IQR = b-a
  print(IQR)
  '''  







#print(IQR)'''


'''data = [32, 36, 46, 47, 56, 69, 75, 79, 79, 88, 89, 91, 92, 93, 96, 97, 
        101, 105, 112, 116]
  
# First quartile (Q1)
Q1 = np.percentile(data, 25, interpolation = 'midpoint')
print(Q1)
  
# Third quartile (Q3)
Q3 = np.percentile(data, 75, interpolation = 'midpoint')
print(Q3)'''
  
# Interquaritle range (IQR)
'''IQR = Q3 - Q1
  
print(IQR)
'''

from scipy import stats
  
'''x = [32, 36, 46, 47, 56, 69, 75, 79, 79, 88, 89, 91, 92, 93, 96, 97, 
        101, 105, 112, 116]
  
# Interquartile range (IQR)
IQR = stats.iqr(x, interpolation = 'midpoint')
  
print(IQR)
'''
'''x = [32, 36, 46, 47, 56, 69, 75, 79, 79, 88, 89, 91, 92, 93, 96, 97, 
        101, 105, 112, 116]

y = np.std(x)
#print(y)

y = np.var(x)
#print(y)

#How can we find percentile

a = np.percentile(x, 25, interpolation = 'midpoint')
print(a)
'''
'''b = np.percentile(x, 75, interpolation = 'midpoint')
print(b)

'''


'''x = np.array([[2,4,6],[1,3,5]])
#print(x)
y = np.cumsum(x)
#print(y)

x = np.array([[2,4,6],[1,3,5]])
#print(x)
y = np.cumsum(x,axis=1)
#print(y)


x = np.array([[2,4,6],[1,3,5]])
print(x)
y = np.cumsum(x,axis=0)
print(y)
'''

#USE OF LINSPACE METHOD()

z = np.linspace(4,8,num=4)
#print(z)

z = np.linspace(2,8,num=4)
#print(z)

z = np.linspace(3,10,num=5)
#print(z)

#retstep tells us what will be the space between the elements of an array.

z = np.linspace(3,10,num=5, retstep=True)
#print(z)

'''z = np.linspace(2.0,3.0,num=5, retstep=True)
#print(z)

z = np.linspace(2,8,num=4, retstep=True)
print(z)'''

# endpoint argument skip the last value.

z = np.linspace(2.0,3.0,num=5, endpoint = False)
#print(z)

'''z = np.linspace(2,8,num=4, endpoint = False)
print(z)'''

'''x = np.array([34,52,23,74,45,96])
a=x.argmax()
#print(a)

x = np.array([22,34,56,78,100])
a =x.argmin()
#print(a)

x = np.array([100,34,56,77,11,23])
a=x.argsort()
print(a)

x = np.array([23,45,66,77,89,100])
a=x.min()
print(a)
'''

'''x = np.array([[5, 6], [7, 8]])
  
y = x.flatten()
  
print( y )
'''

'''x = np.empty([4,5],dtype=int)
#print(x)

#How to create an empty matrix

x = np.empty([4,5],dtype=int)
#print(x)

x = np.empty([4])
print(x)
'''
'''x = np.empty([3,2],dtype=int)
print(x)'''

'''x = np.empty([3,4],dtype=int)
print(x)'''

#How can we add a row in specific index.

'''x = pd.DataFrame({"Name":['Anu','Ashu','Aniket','Shreya'],"Marks":[34,56,78,88],"Roll_no":[1,3,4,5]})
#print(x)

y = x.iloc[0:1]
#print(y)
y.loc[1]=['Koyal',87,2]
#print(y)
z =x.loc[1:]
#print(z)
A=pd.concat([y,z],ignore_index = True)
A.reset_index()
print(A)
'''

'''x = pd.read_csv('iris.csv')
#print(x)
z=x.head()
y=x.tail()
w=x.iloc[1:30,2:4]
x.to_excel('output.xlsx')
with pd.ExcelWriter('output.xlsx')as writer:
  x=z
  x.to_excel(writer,sheet_name='First Five Rows')
  x=y 
  x.to_excel(writer,sheet_name='Bottom five Rows')
  x=w 
  x.to_excel(writer,sheet_name='Two columns')

x = pd.read_excel('output.xlsx',sheet_name='First Five Rows')
#print(x)

x = pd.read_excel('output.xlsx',sheet_name='Bottom five Rows')
#print(x)

x = pd.read_excel('output.xlsx',sheet_name='Two columns')
#print(x)

x = pd.read_excel('output.xlsx',sheet_name=['First Five Rows','Bottom five Rows','Two columns'])  
print(x)
'''


'''x = np.arange(1,11)
y = 2*x
print(x)
print(y)
plt.plot(x,y,color='y',linestyle = ':', linewidth = 10)
plt.title("SimpleLine Plot")
plt.xlabel("data on x-axis")
plt.ylabel("data on y-axis")
plt.show()
'''

'''x = np.arange(1,11)
y1 = 2*x
y2 = 3*x
print(y1)
print(y2)
plt.plot(x,y1,color='orange',linestyle = ':', linewidth = 5)
plt.plot(x,y2,color='g',linestyle = '-.', linewidth = 5)
plt.title("Two Lines in one Plot")
plt.xlabel("range")
plt.ylabel("two lines")
plt.grid()
plt.show()
'''

'''x = np.arange(1,11)
y1=2*x
y2=3*x
print(y1)
print(y2)

# first parameter for row and second for columns and third parameter shows this is first sub plot.


plt.subplot(1,2,1)  # first parameter for row and second for columns and third parameter shows this is first sub plot.

plt.plot(x,y1,color='green',linestyle=':',linewidth=8)

plt.subplot(1,2,2)  # first parameter for row and second for columns and third parameter shows this is second sub plot.

plt.plot(x,y2,color='brown',linestyle=':',linewidth=5)

plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/diamonds.csv')
y=x.head()
print(y)
sns.distplot(x['price'])
plt.show()
'''
'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/diamonds.csv')
y=x.head()
print(y)
#sns.displot(x['price'])
sns.histplot(x['price'])
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/diamonds.csv')
y=x.head()
#print(y)
sns.distplot(x['price'],rug=True)
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/diamonds.csv')
y=x.head()
#print(y)
sns.distplot(x['price'],color="purple")
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/diamonds.csv')
y=x.head()
#print(y)
sns.histplot(x['price'],color="g",kde=False)
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/diamonds.csv')
y=x.head()
#print(y)
sns.distplot(x['price'],color="b",hist=False)
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
print(y)
sns.boxplot(x='Churn',y='tenure',data=x)
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
#print(y)
sns.boxplot(x='InternetService',y='MonthlyCharges',data=x)
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
#print(y)
sns.boxplot(x='InternetService',y='MonthlyCharges',data=x)
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
#print(y)
sns.boxplot(x='InternetService',y='tenure',data=x,linewidth=3)
plt.show()
'''
'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
#print(y)
sns.boxplot(x='Contract',y='tenure',data=x,color="green",linewidth=3)
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
#print(y)
sns.boxplot(x='Contract',y='tenure',data=x,order=["Two year","Month-to-month","One year"])
plt.show()'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
print(y)
sns.boxplot(x='Contract',y='tenure',data=x,hue="PaymentMethod")
plt.show()
'''

'''x = sns.load_dataset("iris")
y=x.head()
print(y)
sns.pairplot(x, hue="species")
plt.show()
'''

'''x = [10,20,30,40,50,60,70,80,90]
a = [10,23,70,20,9,30,46,33,28]
b = [80,20,52,67,92,13,42,56,36]
plt.subplot(1,2,1)
plt.scatter(x,a,marker="*",color='g',s=150)
plt.title('Company Green')
plt.xlabel('Years from entity origin')
plt.ylabel('Revenue growth in percentage(%)')
plt.grid(True)
plt.subplot(1,2,2)
plt.scatter(x,b,marker=".",color='red',s=300)
plt.title('Company Red')
plt.xlabel('Years from entity origin')
plt.ylabel('Revenue growth in percentage(%)')
plt.grid(True)
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=0.4,hspace=0.4)
plt.show()
'''

'''z = [1,1,2,2,2,3,3,3,3,4]
plt.hist(z,color="g")
plt.show()
'''

'''z = [1,1,2,2,2,3,3,3,3,4]
plt.hist(z,color='r',bins=4)

plt.show()
'''

'''z = [2,2,2,5,6,1,7,8,3,6,6,9,2,4,5,6]
plt.hist(z)
plt.show()
'''
# If I want to add bins and color

'''z = [2,2,2,5,6,1,7,8,3,6,6,9,2,4,5,6]
plt.hist(z,color='r',bins=8)
plt.show()
'''

'''iris = pd.read_csv('iris.csv')
#print(iris)
print(iris.head())

plt.hist(iris['sepal_length'])
plt.show()'''


'''Vegetables = ["Potato","Tomato","Brinjal","chilly"]
Cost= [64,34,100,56]
plt.pie(Cost,labels=Vegetables)
plt.show()


Vegetables = ["Potato","Tomato","Brinjal","chilly","carrot"]
Cost= [64,34,100,56,78]
plt.pie(Cost,labels=Vegetables,autopct='%0.1f%%',colors=['yellow','grey','green','red','blue'])
plt.show()
'''

'''Vegetables = ["Potato","Tomato","Brinjal","chilly","carrot"]
Cost= [64,34,100,56,78]
plt.pie(Cost,labels=Vegetables,radius=1)
plt.pie(Cost,labels=Vegetables,autopct='%0.1f%%',colors=['yellow','grey','green','red','blue'])
plt.pie([1],colors=['w'],radius=0.4)
plt.show()
'''

'''Vegetables = ["Potato","Tomato","Brinjal","chilly","carrot"]
Cost= [64,34,100,56,78]
plt.pie(Cost,labels=Vegetables,radius=1)
#plt.pie(Cost,labels=Vegetables,autopct='%0.1f%%',colors=['yellow','grey','green','red','blue'])
plt.pie(Cost,labels=Vegetables,Cost=[64,34,100,56,78],colors=['yellow','grey','green','red','blue'])
plt.pie([1],colors=['w'],radius=0.4)
plt.show()
'''
'''y = pd.Series([1000,1500, 2300, 3540, 4120, 4560, 5490, 3460, 4750, 2300, 9000, 8600, 7100])
#print(x)
x = np.mean(y)
print(x)
t_statistic, p_value = stats.ttest_1samp(a=y,popmean=x)

print("This is one sample value",t_statistic)
print("This is p value",p_value)
'''


'''from scipy.stats import chisquare

x = [16, 18, 16, 14, 12, 12]

y = chisquare(x)
print(y)
'''

#from scipy.stats import 
'''import statsmodels.api as sm
from statsmodels.formula.api import ols

x = [32, 36, 46, 47, 56, 69, 75, 79, 79, 88, 89, 91, 92, 93, 96, 97, 
        101, 105, 112, 116]


#perform two-way ANOVA
model = ols(data=x).fit()
sm.stats.anova_lm(model, typ=2)

'''
'''import statsmodels.api as sm
from statsmodels.formula.api import ols

#perform two-way ANOVA
model = ols('height ~ C(water) + C(sun) + C(water):C(sun)', data=df).fit()
sm.stats.anova_lm(model, typ=2)'''


'''import numpy as np
import pandas as pd

#create data
df = pd.DataFrame({'water': np.repeat(['daily', 'weekly'],15),
                   'sun': np.tile(np.repeat(['low', 'med', 'high'], 5), 2),
                   'height': [6, 6, 6, 5, 6, 5, 5, 6, 4, 5,
                              6, 6, 7, 8, 7, 3, 4, 4, 4, 5,
                              4, 4, 4, 4, 4, 5, 6, 6, 7, 8]})
print(df[:10])'''

'''import statsmodels.api as sm
from statsmodels.formula.api import ols

#perform two-way ANOVA
model = ols('height ~ C(water) + C(sun) + C(water):C(sun)', data=df).fit()
d=sm.stats.anova_lm(model, typ=2)
print(d)
'''


#Two way Anova test

'''import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np
import pandas as pd
  
# Create a dataframe
x = pd.DataFrame({'Fertilizer': np.repeat(['daily', 'weekly'], 15),
                          'Watering': np.repeat(['daily', 'weekly'], 15),
                          'height': [14, 16, 15, 15, 16, 13, 12, 11, 14, 
                                     15, 16, 16, 17, 18, 14, 13, 14, 14, 
                                     14, 15, 16, 16, 17, 18, 14, 13, 14, 
                                     14, 14, 15]})'''
#print(x)

#z = ols('height ~ C(Fertilizer) + C(Watering) +\
#C(Fertilizer):C(Watering)',
#           data=x).fit()

'''z = ols('height ~ C(Fertilizer) + C(Watering) +\
C(Fertilizer):C(Watering)',
            data=x).fit()

y = sm.stats.anova_lm(z, type=2)
  
# Print the result
print(y)'''


'''Interpreting the result:

Following are the p-values for each of the factors in the output:

    The fertilizer p-value is equal to 0.913305
    The Watering p-value is equal to 0.990865
    The Fertilizer * Watering: p-value is equal to 0.904053

The p-values for water and sun turn out to be less than 0.05 which implies that the means of 
both the factors possess a statistically significant effect on plant height. The p-value for 
the interaction effect (0.904053) is greater than 0.05 which depicts that there is no 
significant interaction effect between fertilizer frequency and watering frequency.'''



'''x = pd.read_csv('C:/Users/shpoo/Desktop/IRIS.csv')
print(x)
print(x.head())
plt.hist(x['petal_length'],color="r")
plt.show()
'''

'''one = [1,2,3,4,5,6,7,8,9]
two = [1,2,3,4,5,4,3,2,1]
three = [6,7,8,9,8,7,6,5,4]

x = list([one,two,three])

plt.boxplot(x)
plt.show()
'''
#VIOLIN PLOT

'''one = [1,2,3,4,5,6,7,8,9]
two = [1,2,3,4,5,4,3,2,1]
three = [6,7,8,9,8,7,6,5,4]

x = list([one,two,three])

plt.violinplot(x)
plt.show()'''

'''one = [1,2,3,4,5,6,7,8,9]
two = [1,2,3,4,5,4,3,2,1]
three = [6,7,8,9,8,7,6,5,4]

x = list([one,two,three])

plt.violinplot(x,showmedians=True)
plt.show()'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/IRIS.csv')
#print(x)
print(x.head())
plt.hist(x['sepal_length'],color="g")
plt.show()
'''

'''Create a data set of student name and show the subjects and students % of marks with the
help of any plot, visualization looks, meaningful and understandable.

Choose any data set and show the visualization with the help of bar graph.

Choose any data set and show the visualization with the help of scatter plot, and line plot.'''

#x = pd.DataFrame({"Name":["Abc","xyz","Awd"], "Marks": [78,67,92]}, index = [1,2,3])

'''x = sns.load_dataset("fmri")
#print(x)
y=x.head()
print(y)
sns.lineplot(x="timepoint",y = "signal",data=x, hue= 'event',style='event')
plt.show()
'''

'''x = sns.load_dataset("fmri")
y=x.head()
print(y)
sns.lineplot(x="timepoint",y = "signal",hue="event",style="event",markers=True,data=x)
plt.show()
'''

'''x=pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/pokemon.csv')
print(x)
#y=x.head()
#print(y)
sns.set(style = "whitegrid")
sns.barplot(x="Legendary",y="Speed",data=x)
plt.show()'''



'''x=pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/pokemon.csv')
#print(x)
sns.set(style = "whitegrid")
sns.barplot(x="Legendary",y="Speed",hue = "Generation",data=x)
plt.show()'''


'''import scipy.stats as stats


#perform the Mann-Whitney U test

group1 = [20, 23, 21, 25, 18, 17, 18, 24, 20, 24, 23, 19]
group2 = [24, 25, 21, 22, 23, 18, 17, 28, 24, 27, 21, 23]
print(stats.mannwhitneyu(group1, group2, alternative='two-sided'))'''




'''x = [7, 9, 12, 15, 21]
y = [5, 8, 14, 13, 25]
z = [6, 8, 8, 9, 5]
  
# Conduct the Kruskal-Wallis Test 
g = stats.kruskal(x, y, z)
  
# Print the result
print(g)'''

'''group1 = [20, 23, 21, 25, 18, 17, 18, 24, 20, 24, 23, 19]
group2 = [24, 25, 21, 22, 23, 18, 17, 28, 24, 27, 21, 23]

print(stats.mannwhitneyu(group1, group2, alternative='two-sided'))
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
print(y)
sns.boxplot(x='Churn',y='tenure',data=x)
plt.show()'''


'''a = sns.load_dataset('titanic')
#print(a)
sns.barplot(x ='who',y = 'fare',hue='class',data = a, palette = 'Blues')
plt.show()'''


'''x=pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/pokemon.csv')
#y=x.head()
print(x)
sns.set(style = "whitegrid")
sns.barplot(x="Legendary",y="Speed",data=x,palette = "Blues_d")
plt.show()
'''

'''x=pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/pokemon.csv')
print(x)
sns.set(style = "whitegrid")
sns.barplot(x="Legendary",y="Speed",hue = "Generation",data=x)
plt.show()
'''
'''x=pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/pokemon.csv')
y=x.head()
#print(y)
sns.set(style = "whitegrid")
sns.barplot(x="Legendary",y="Speed",data=x,color = 'green')#palette = "rocket")
plt.show()
'''

'''x = pd.read_csv('iris.csv')
y=x.head()
print(y)
sns.scatterplot(x = 'sepal_length',y = 'petal_length',data=x,hue = 'species', style = 'species')
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/diamonds.csv')
y=x.head()
print(y)
sns.displot(x['price'], rug = True)
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/diamonds.csv')
y=x.head()
#print(y)
sns.distplot(x['price'],color="g",kde=False)
plt.show()
'''


'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
print(y)
sns.boxplot(x='Churn',y='tenure',data=x)
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
#print(y)
sns.boxplot(x='InternetService',y='MonthlyCharges',data=x, color ='orange', linewidth = 4)
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
#print(y)
sns.boxplot(x='InternetService',y='tenure',data=x,linewidth=3)
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
#print(y)
sns.boxplot(x='Contract',y='tenure',data=x,order=["Two year","Month-to-month","One year"])
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
print(y)
sns.boxplot(x='Contract',y='tenure',data=x,hue="PaymentMethod")
plt.show()
'''

#Import libraries
'''from scipy import stats
  
# Defining data groups
x = [7, 9, 12, 15, 21]
y = [5, 8, 14, 13, 25]
z = [6, 8, 8, 9, 5]
  
# Conduct the Kruskal-Wallis Test 
g = stats.kruskal(x, y, z)
  
# Print the result
print(g)'''

'''from scipy.stats import chisquare

x = [16, 18, 16, 14, 12, 12]

y = chisquare(x)
print(y)
'''

from numpy import random

'''x = random.normal(loc=1, scale=2, size=(2, 3))

print(x) 


import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000), hist=False)

plt.show() 
'''


'''x = random.binomial(n=10, p=0.5, size=10)

print(x)
#Visualization of Binomial Distribution
#Example
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

plt.show() 
'''

'''from numpy import random

x = random.poisson(lam=2, size=10)

print(x)
#Visualization of Poisson Distribution
#Example
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.poisson(lam=2, size=1000), kde=False)

plt.show()
'''

'''x = [10,20,30,40,50,60,70,80,90]
a = [8,1,7,2,0,3,7,3,2]
b = [7,2,5,6,9,1,4,5,3]
plt.scatter(x,a,marker="*",color='g',s=500)
plt.scatter(x,b,marker=".",color='orange',s=500)
plt.title('scatter plot')
plt.show()
'''

'''x = [10,20,30,40,50,60,70,80,90]
a = [10,23,70,20,9,30,46,33,28]
b = [80,20,52,67,92,13,42,56,36]
plt.subplot(1,2,1)
plt.scatter(x,a,marker="*",color='g',s=150)
plt.title('Company Green')
plt.xlabel('Years from entity origin')
plt.ylabel('Revenue growth in percentage(%)')
plt.grid(True)
plt.subplot(1,2,2)
plt.scatter(x,b,marker=".",color='red',s=300)
plt.title('Company Red')
plt.xlabel('Years from entity origin')
plt.ylabel('Revenue growth in percentage(%)')
plt.grid(True)
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=0.4,hspace=0.4)
plt.show()
'''

'''x = [10,20,30,40,50,60,70,80,90]
a = [8,1,7,2,0,3,7,3,2]
b = [7,2,5,6,9,1,4,5,3]
plt.subplot(2,1,1 )
plt.scatter(x,a,marker="*",color='red',s=150)
plt.title('scatter sub plots')
plt.xlabel('Years from entity origin')
plt.ylabel('Revenue growth in percentage')
plt.subplot(2,1,2)
plt.scatter(x,b,marker=".",color='blue',s=300)
plt.xlabel('Years from entity origin')
plt.ylabel('Revenue growth in percentage')
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=0.5,hspace=0.5)
plt.show()
'''


'''z = [1,1,2,2,2,3,3,3,3,4]
plt.hist(z,color="g")
#plt.show()

z = [1,1,2,2,2,3,3,3,3,4]
plt.hist(z,color='r',bins=4)

plt.show()

'''

'''Vegetables = ["Potato","Tomato","Brinjal","chilly"]
Cost= [64,34,100,56]
plt.pie(Cost,labels=Vegetables)
plt.show()
'''

'''Vegetables = ["Potato","Tomato","Brinjal","chilly","carrot"]
Cost= [64,34,100,56,78]
plt.pie(Cost,labels=Vegetables,autopct='%0.1f%%',colors=['yellow','grey','green','red','blue'])
plt.show()
'''

'''Vegetables = ["Potato","Tomato","Brinjal","chilly","carrot"]
Cost= [64,34,100,56,78]
plt.pie(Cost,labels=Vegetables,radius=1)
plt.pie(Cost,labels=Vegetables,autopct='%0.1f%%',colors=['yellow','grey','green','red','blue'])
plt.pie([1],colors=['w'],radius=0.4)
plt.show()
'''

'''from numpy import random

x = random.normal(loc=1, scale=2, size=(2, 3))

print(x) 


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000), hist=False)

plt.show() 
'''

'''from numpy import random

x = random.binomial(n=10, p=0.5, size=10)

print(x)
#Visualization of Binomial Distribution
#Example
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=True)

plt.show() 
'''


'''from numpy import random

x = random.poisson(lam=2, size=10)

print(x)
#Visualization of Poisson Distribution
#Example
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.poisson(lam=2, size=1000), kde=False)

plt.show()'''

#print('hello')

'''x = 4 
y = 7 
z = x+y 
print(z)
print(x)'''

#import pandas as pd 

#x = pd.Series([25,23,27,48,19])
#print(x)
#print(type(x))
#print(len(x))
#print(x[1:4])

'''x = pd.Series([34,22,"as",7.8,5j], index=['one','Two','Three','Four','Five'])
#print(x)

student = pd.Series({"Name": "ABC", "Age": 12, "Roll no": 13},index = {'Name','Age','Roll no'})
print(student)
'''

'''Apply all basic arithmetic operations:

x1 = pd.Series([10,20,30,40,50,60,70])
x2 = pd.Series([23,34,56,78,12,12,23])
z = x1+x2
print(z)'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/IRIS.csv')
print(x.value_counts('species'))'''


'''two = [1,2,3,4,5,4,3,2,1]
three = [6,7,8,9,8,7,6,5,4]
one = [1,2,3,4,5,6,7,8,9]

x = list([one,two,three])

plt.boxplot(x)
plt.show()

#VIOLIN PLOT

one = [1,2,3,4,5,6,7,8,9]
two = [1,2,3,4,5,4,3,2,1]
three = [6,7,8,9,8,7,6,5,4]

x = list([one,two,three])

plt.violinplot(x)
plt.show()
'''
'''one = [1,2,3,4,5,6,7,8,9]
two = [1,2,3,4,5,4,3,2,1]
three = [6,7,8,9,8,7,6,5,4]

x = list([one,two,three])

plt.violinplot(x,showmedians=True)
plt.show()'''


'''x = sns.load_dataset("iris")
y=x.head()
print(y)
sns.pairplot(x, hue="species")
plt.show()
'''


'''Use matplotlib and sea born both.
Create a line plot with the help of sea born on this iris data set.
(Take two columns, sepal_length, sepal_width)

Create a bar plot on titanic data set

Create a histogram and frequency curve on the titanic and iris data set.

Create a scatter plot on these data sets.'''

'''x = pd.read_csv('iris.csv')
#print(x)
y = x.loc[0:,'sepal_length']
#print(y)
z = x.loc[0:,'sepal_width']
#print(z)
sns.lineplot(y,z)
plt.show()'''


'''x = np.arange(1,11)
y = 2*x
print(x)
print(y)
plt.plot(x,y,color='red',linestyle = ':', linewidth = 5)
plt.title("SimpleLine Plot")
plt.xlabel("data on x-axis")
plt.ylabel("data on y-axis")
plt.show()
'''

'''x = pd.read_csv('iris.csv')
#print(x)
y = x.loc[0:,'sepal_length']
#a=y.head()
z = x.loc[0:,'petal_length']
#b=z.head()
#plt.plot(b,a,color='red',linewidth = 6)
plt.plot(z,y,color='red',linewidth = 6)

plt.title('Line_plot')
plt.xlabel("data on x-axis")
plt.xlabel("data on y-axis")
plt.show()
'''

'''x= pd.read_csv('matches.csv')
#print(x)
y=x['Season'].value_counts()
print(y)'''


'''online_rt = pd.read_csv('C:/Users/shpoo/Downloads/Pandas case studies/DS-Ex5(2)/DS-Ex5/Online_Retail.csv')
print(online_rt)
'''
'''import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
df=pd.read_csv("iris.csv")
print(df)
d=df.head(10)

plt.plot(d["sepal_length"],d["SepalWidthCm"],marker="o",markeredgecolor="g",markeredgewidth=15,color="r")
plt.xlabel("SepalLengthCm",fontweight="bold",size=15,backgroundcolor="g",style="italic")
plt.ylabel("SepalWidthCm",fontweight="bold",backgroundcolor="g",size=15,style="italic")
plt.title("Chart")
plt.minorticks_on() 
plt.grid(which="minor",color="g")
plt.tight_layout()
plt.show()'''

import pandas as pd 



'''x = pd.read_csv('iris.csv')
print(x)'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Data set for ML/GOOG.csv')
print(x)'''

'''x = np.array([6,7,7,12,13,13,15,16,19,22])
y=stats.zscore(x)
print(y)'''











'''x = sns.load_dataset("fmri")
#print(x)
y=x.head()
#print(y)
sns.lineplot(x="timepoint",y = "signal",data=x,hue='event',style = 'event',markers=True)
plt.show()
'''

'''x=pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/pokemon.csv')
y=x.head()
#print(y)
sns.set(style = "whitegrid")
sns.barplot(x="Legendary",y="Speed", hue = 'Generation',data=x,palette = "Blues_d")
plt.show()
'''

'''x1=pd.Series([3,4,5,6])
x2 = pd.Series([5,6,7,8])
print(x1+x2)
z=(x1+x2)
'''#print(z)

'''x1 = pd.Series([3,4,5,6])
x2 = 5 
print(x1*x2)'''



#x = pd.DataFrame({"Name":['Arun','Lisa','Kishan','Arvind'], "Marks": [ 45,66,77,98]})
#print(x)
#print(type(x))
#print(len(x))

x = pd.DataFrame({"Fruits":["Apple","Mango","Orange"], "Cost": [ 67,89,85]},
  index = ["one","Two","Three"])
#print(x)
#print(x.index)

x = pd.DataFrame({'Name':['ABC','XYZ','QQR'],'Marks':[3,6.7,5j]})
#print(x)

#How can we change the sequence of columns:

'''x = pd.DataFrame({"Veg_Names":['Potatoes',"Brinjal","Radish","Tomatoes"],"Cost":
  [36,78,99,89],"Quality":["Yummy","Tasty","Good","Bitter"]},index=['a','b','c','d'],
  columns=['Quality','Cost','Vegetables_Names'])
print(x)'''


'''x = pd.read_csv('iris.csv')
print(x)'''

x = pd.read_csv('C:/Users/shpoo/Desktop/iris.csv')
#print(x)
#print(x.head())
#print(x.head(12))
#print(x.tail())
#print(x.tail(12))

#Use of iloc[] method

'''y = x.iloc[30:71,2:5]
print(y)'''


# USe of loc[]method
'''y=x.loc[10:30,('petal_length')]
#print(y)

y = x.loc[30:50,('petal_width','sepal_length')]
print(y)'''

'''x = pd.read_csv('iris.csv')
y=x.head()
#print(y)
sns.scatterplot(x = 'sepal_length',y = 'petal_length',hue = 'species', style = 'species',data=x)
plt.show()
'''


'''a=pd.read_csv('iris.csv')
z=a.head()
#print(z)
sns.scatterplot(x='sepal_length',y='petal_length',data=a)
plt.show()
'''
#x = pd.read_csv('C:/Users/shpoo/Desktop/titanic.csv')
#print(x)

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/diamonds.csv')
y=x.head()
print(y)
sns.distplot(x['price'])
plt.show()
'''
#import pandas as pd
# = pd.read_csv('C:/Users/shpoo/Desktop/iris.csv')
#print(x)
#print(x.shape)
#print(x.head(8))
#print(x.tail(12))

#use of iloc [] method

'''y = x.iloc[43:63,0:]
print(y)'''

'''y = x.iloc[60:71, 2:4]
print(y)'''


#use of loc[] method

'''y = x.loc[45:67,'sepal_width']
print(y)'''

#y = x.loc[56:76,('petal_width','sepal_width')]
#print(y)

'''y = x.min()
#print(y)

y = x.max()
#print(y)

y = x.count()
#print(y)

y = x.value_counts('species')
#print(y)

y = x.median()
#print(y)

y = x.mean()
#print(y)

y = x.mode()
print(y)

y = x.describe()
#print(y)

y = x.std()
#print(y)

y = x.var()
#print(y)'''

#How can we delete and columns

'''y = x.drop([1,5], axis=0)
print(y)'''

#DROP COLUMNS

'''y = x.drop(['petal_length','species'],axis=1)
#print(y)

y = x.sort_values(by='petal_length')
#print(y)

y = x.sum()
#print(y)

#Extract any column and apply all methods


#y = x.loc[20:70,'petal_length']
#print(y)
#print(y.sum())
#print(y.value_counts())
#print(y.count())
#print(y.sort_values())
#print(y.drop ([69,67,45],axis=0))

x = pd.read_csv('C:/Users/shpoo/Downloads/Pandas case studies/DS-Ex5(2)/DS-Ex5/Online_Retail.csv')
print(x)
'''


#euro12 = pd.read_csv('C:/Users/shpoo/Downloads/Pandas case studies/DS-EX2(1)/DS-EX2/Euro_2012_stats_Team.csv')
#print(euro12)

#Step 11. Select the teams that start with G

'''y=euro12[euro12.Team.str.startswith('G')]
print(y)'''


#Step 4. What is the type of the columns?
#crime = pd.read_csv('C:/Users/shpoo/Downloads/Pandas case studies/DS-EX3/US_Crime_Rates_1960_2014.csv')
#print(crime.head())

#What is the type of the column
#z=crime.info()
#print(z)

#Convert the type of the column year to datetime64
#pd.to_datetime(crime)
#a=crime.Year = pd.to_datetime(crime.Year, format ='%Y')
#a.info()
#print(a)
#print(crime)
#z=crime.info()
#print(z)


'''x=pd.DataFrame({'company':["google","google","yahoo","yahoo","Amazone","Amazone"],
  'person':['Akash','kajal','kiran','koyal','Anjali','Aman'],'sales_in_India'
  :[100,140,540,670,240,551]})

print(x)

print(x.groupby('company'))
#print(type(x.groupby('company')))
#z = (x.groupby('company'))


#print(z.std())
#print(z.min())
#print(z.mean())
#print(z.sum()) 
#print(z.count())
#print(z.describe())
#print(z.describe().transpose())  # It will change the position of data frame, row become column and column become row.
print(z.describe().transpose()['Amazone'])
'''



'''plt.cla() clears an axis, i.e. the currently active axis in the current figure. 
It leaves the 
other axes untouched.
plt.clf() clears the entire current figure with all its axes, but leaves the window 
opened, 
such that it may be reused for other plots.
plt.close() closes a window, which will be the current window, if not specified otherwise.

Which functions suits you best depends thus on your use-case.

The close() function furthermore allows one to specify which window should be closed. The argument 
can either be a number or name given to a window when it was created using figure(number_or_name) 
or it can be a figure instance fig obtained, i.e., usingfig = figure(). If no argument is given to 
close(), the currently active window will be closed. Furthermore, there is the syntax close('all'), 
which closes all figures.'''

'''x = [10,20,30,40,50,60,70,80,90]
a = [8,1,7,2,0,3,7,3,2]
b = [7,2,5,6,9,1,4,5,3]
plt.subplot(2,1,1 )
plt.scatter(x,a,marker="*",color='red',s=150)
plt.title('scatter sub plots')
plt.xlabel('Years from entity origin')
plt.ylabel('Revenue growth in percentage')
plt.subplot(2,1,2)
plt.scatter(x,b,marker=".",color='blue',s=300)
plt.xlabel('Years from entity origin')
plt.ylabel('Revenue growth in percentage')
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=0.5,hspace=0.5)
plt.clf()
plt.cla()
plt.show()
plt.close()
'''

'''x = [10,20,30,40,50,60,70,80,90]
a = [8,1,7,2,0,3,7,3,2]
b = [7,2,5,6,9,1,4,5,3]
plt.scatter(x,a,marker="*",color='g',s=150)
plt.scatter(x,b,marker=".",color='orange',s=300)
plt.title('scatter plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
plt.cla()'''


#USE OF cla(), clf() and close() Methods in Matplotlib

'''x = np.arange(1,11)
y = 2*x
print(x)
print(y)
plt.plot(x,y)
#plt.clf()
#plt.cla()
plt.title("SimpleLine Plot")
plt.xlabel("data on x-axis")
plt.ylabel("data on y-axis")
plt.show()
plt.close()
'''
'''student = {"kajal":87, "Arun": 56, "kiran":27}
a = list(student.keys())
b = list(student.values())
print(a)
print(b)
plt.bar(a,b)
#plt.cla() #clear the current Axes state without closing it.
#plt.clf() # clear the current Figure’s state without closing it.
plt.show()
plt.close()
'''
'''Vegetables_basket = {"Brinjal":100, "Potatos": 145, "Tomatoes": 123}
Vegetables_names=list(Vegetables_basket.keys())
Vegetables_cost=list(Vegetables_basket.values())
plt.bar(Vegetables_names,Vegetables_cost)
plt.title("Bar Plot")
plt.xlabel("Vegetables_names")
plt.ylabel("Vegetables_cost")
plt.grid(True)
#plt.cla()
plt.clf()
plt.close()
'''
#plt.show()

'''Vegetables_basket = {"Brinjal":100, "Potatos": 145, "Tomatoes": 123}
Vegetables_names=list(Vegetables_basket.keys())
Vegetables_cost=list(Vegetables_basket.values())
plt.bar(Vegetables_names,Vegetables_cost)
plt.title("Bar Plot")
plt.xlabel("Vegetables_names")
plt.ylabel("Vegetables_cost")
plt.grid(True)
#plt.cla()
plt.clf()
plt.close()
'''

'''x = np.arange(1,11)
y = 2*x
print(x)
print(y)
plt.plot(x,y)
plt.clf()

plt.title("SimpleLine Plot")
plt.xlabel("data on x-axis")
plt.ylabel("data on y-axis")
#plt.cla()

plt.show()
'''


'''x = np.arange(1,11)
y = 2*x
print(x)
print(y)
plt.plot(x,y)
#plt.clf()
plt.title("SimpleLine Plot")
plt.xlabel("data on x-axis")
plt.ylabel("data on y-axis")
#plt.cla()
plt.show()
'''

'''We can set the Inner and Outer colors of the plot. set_facecolor() method is used to 
change the inner background color of the plot. figure(facecolor='color') method is used 
to change the outer background color of the plot.'''


'''import matplotlib.pyplot as plt
  
# giving values for x and y to plot
student_marks = [50, 60, 70, 80, 90]
student_grade = ['B', 'B', 'B+', 'B+', 'A']
  
plt.plot(student_marks, student_grade)
  
# Giving x label using xlabel() method
# with bold setting
plt.xlabel("student_marks", fontweight='bold')
  
# Giving y label using xlabel() method
# with bold setting
plt.ylabel("student_grade", fontweight='bold')
  
# Giving title to the plot
plt.title("Student Marks v/s Student Grade")
  
# Showing the plot using plt.show()
plt.show()'''


'''import matplotlib.pyplot as plt
  
# giving values for x and y to plot
student_marks = [50, 60, 70, 80, 90]
student_grade = ['B', 'B', 'B+', 'B+', 'A']
ax = plt.axes()
ax.set_facecolor("yellow")

plt.plot(student_marks, student_grade)
  
# Giving x label using xlabel() method
# with bold setting
plt.xlabel("student_marks", fontweight='bold')
  
# Setting the background color of the plot 
# using set_facecolor() method
 
# Giving y label using xlabel() method 
# with bold setting
plt.ylabel("student_grade", fontweight='bold')
  
# Giving title to the plot
plt.title("Student Marks v/s Student Grade")
'''


  
# Showing the plot using plt.show()
#plt.show()


'''x = np.arange(1,11)
y = 2*x
print(x)
print(y)
ax=plt.axes()
ax.set_facecolor('pink')
plt.plot(x,y)
plt.show()'''


'''Vegetables_basket = {"Brinjal":100, "Potatos": 145, "Tomatoes": 123}
Vegetables_names=list(Vegetables_basket.keys())
Vegetables_cost=list(Vegetables_basket.values())
ax=plt.axes()
ax.set_facecolor('pink')
plt.bar(Vegetables_names,Vegetables_cost)
plt.title("Bar Plot")
plt.xlabel("Vegetables_names")
plt.ylabel("Vegetables_cost")
plt.grid(True)
plt.show()'''

#What is stack plot and why we use it

'''Stackplot is used to draw a stacked area plot. It displays the complete data for 
visualization. It shows each part stacked onto one another and how each part makes 
the complete figure. It displays various constituents of data and it behaves like a 
pie chart. It has x-label, y-label, and title in which various parts can be 
represented by different colors. 

The idea of stack plots is to show “parts to the whole” over time. It is used to 
represent various datasets without overlapping over each other.
'''
'''a = [1,2,3,4,5] # It will pass on x axis

b = [7,8,6,11,7] # rest of the four list passon y axis.
c = [2,3,4,3,2]
d = [7,8,7,2,2]
e = [8,5,7,8,13]
plt.plot([],[], color = 'r', label = 'APPLE', linewidth = 5)
plt.plot([],[], color = 'y', label = 'Mango', linewidth = 5)
plt.plot([],[], color = 'brown', label = 'Cherry', linewidth = 5)
plt.plot([],[], color = 'orange', label = 'Orange', linewidth = 5)
plt.stackplot(a,b,c,d,e,colors=['r','y','brown','orange'])
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.show()'''


#Error: could not build wheels for pandas, which is required to install pyproject.toml based projects

'''x = pd.Series([7,  8,   8, 8,   9,   9,   9,   10,  11,  14,  14,  15])
a=x.mean()
#print(a)
a=x.mode()
print(a)
'''


'''import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset

dataset = pd.read_csv('C:/Users/shpoo/Desktop/Data set for ML/Social_Network_Ads.csv')
x = dataset.iloc[:, 2:4].values
y = dataset.iloc[:, 4].values
print(x)
#print(y)'''


'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/diamonds.csv')
y=x.head()
#print(y)
sns.distplot(x['price'],rug=True)
#sns.histplot(x['price'],color='purple')
#sns.displot(x['price'])
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/diamonds.csv')
y=x.head()
#print(y)
sns.distplot(x['price'],color='purple',kde=False)
plt.show()'''


'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/diamonds.csv')
y=x.head()
#print(y)
sns.distplot(x['price'],color="b",hist=False)
plt.show()
'''

'''a = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = a.head()
print(y)
sns.boxplot(x='Churn',y='tenure',data=a)
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
#y = x.head()
y=x.shape[0]
print(y)
sns.boxplot(x='InternetService',y='MonthlyCharges',data=x)
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
#print(y)
sns.boxplot(x='InternetService',y='tenure',data=x,color="yellow",linewidth=5)
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
#print(y)
sns.boxplot(x='Contract',y='tenure',data=x,order=["Two year","Month-to-month","One year"])
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
print(y)
sns.boxplot(x='Contract',y='tenure',data=x,hue="PaymentMethod")
plt.show()
'''

'''one = [1,2,3,4,5,6,7,8,9]
two = [1,2,3,4,5,4,3,2,1]
three = [6,7,8,9,8,7,6,5,4]

x = list([one,two,three])

plt.boxplot(x)
plt.show()'''

#VIOLIN PLOT

'''one = [1,2,3,4,5,6,7,8,9]
two = [1,2,3,4,5,4,3,2,1]
three = [6,7,8,9,8,7,6,5,4]

x = list([one,two,three])

plt.violinplot(x)
plt.show()'''

'''one = [1,2,3,4,5,6,7,8,9]
two = [1,2,3,4,5,4,3,2,1]
three = [6,7,8,9,8,7,6,5,4]

x = list([one,two,three])

plt.violinplot(x,showmedians=True)
plt.show()
'''

'''a = pd.read_csv('titanic.csv')
y=a.head()
#print(y)
sns.barplot(x='who', y = 'fare', hue = 'class', data = a, palette='Blues')
plt.show()
'''



'''a = sns.load_dataset('titanic')
#print(a)
sns.barplot(x ='who',y = 'fare',hue='class',data = a, palette = 'Blues')
plt.show()


x = pd.read_csv('iris.csv')
y=x.head()
print(y)
sns.histplot(x['sepal_width'])
plt.show()'''


'''import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset

dataset = pd.read_csv('C:/Users/shpoo/Desktop/Data set for ML/Social_Network_Ads.csv')
x = dataset.iloc[:, 2:4].values
y = dataset.iloc[:, 4].values
'''#print(x)
#print(y)


#Splitting the dataset into the Training set and Test set

'''from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size = 0.20,random_state=0)
#print(x_train,x_test,y_train,y_test)


# Feature Scaling

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
#print(x_test)
#print(x_train)

# Training the K-NN model on the Training set

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 7, metric = 'minkowski', p = 2)
z=classifier.fit(x_train, y_train)
#print(z)

# Predicting the Test set results
y_pred = classifier.predict(x_test)
#print(y_pred)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
ac = accuracy_score(y_test, y_pred)
print(ac)'''


'''x = pd.DataFrame({"Name":["kajal","Ritu","Priya"], "Marks": [78,67,92]}, index = [1,2,3])
y = pd.DataFrame({"Name":["Shivam","Sheenu","koyal"], "Marks": [56,34,89]}, index = [4,5,6])
z = (x,y)
w = pd.concat(z)
print(w)
'''


'''x = pd.DataFrame({"Name":["Abc","xyz","Awd"], "Marks": [78,67,92]}, index = [1,2,3])
y = pd.DataFrame({"Name":["Raj","Deepak","Kanika"], "Marks": [56,34,89]}, index = [4,5,6])
z=x.append(y)
print(z)
'''


#USE OF inner merge

'''x = pd.DataFrame({'Name_1':['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'],'Eng':[99,78,98,87,97,67]})
#print(x)

y = pd.DataFrame({'Name_2':['Ashish','Tajesvi','Omkar','Nikhil','Abhishek','Rahul','Ranjeet'],'Math':[99,98,87,97,67,75,98]})
#print(y)

z=pd.merge(left=x, right=y, how='right', left_on='Name_1',right_on='Name_2',indicator = True)
print(z)'''


'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])
#print(x)
print(x.str.title())
'''
'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])
print(x.str.len())
print(len(x))
'''
'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])
print(x.str.split())
'''
'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])

print (x.str.cat(sep='**'))
'''

'''x = pd.Series(['Ashish','Arvind','Sahil','Deepak','Nikhil','Abhishek'])
print (x.str.contains('ee'))
'''
#x = [23,45,66,77,88,100,23]

'''x = pd.Series([56,23,66,77,88,100,23])
print(x.mode())
print(x.count())
'''

'''x= [66, 67, 67, 68, 68, 68, 68, 69, 69, 69, 69, 70, 70, 71, 71, 72, 73, 75]
IQR= stats.iqr(x, interpolation = 'midpoint')
  
print(IQR)
'''

'''x = [4,3,2,1,5]
I=stats.iqr(x,interpolation = 'midpoint')
print(I)'''

'''x = [12,45,67,89,12,34,56,23,12,12,89,56]
IQR= stats.iqr(x,interpolation = 'midpoint')
print(IQR)'''

'''x=[34,22,12,22,33,44,55,66,12]
IQR= stats.iqr(x,interpolation = 'midpoint')
print(IQR)'''


import numpy as np
'''   
# 1D array
arr = [20, 2, 7, 1, 34]
print("arr : ", arr)
print("50th percentile of arr : ",
       np.percentile(arr, 50))
print("25th percentile of arr : ",
       np.percentile(arr, 25))
print("75th percentile of arr : ",
       np.percentile(arr, 75))'''


'''{75, 77, 78, 78, 80, 81, 81, 82, 83, 84, 84, 84, 85, 87, 87, 88, 88, 88, 89, 90}.

n = (20/100) x 20

n = 4
'''

'''x = [75, 77, 78, 78, 80, 81, 81, 82, 83, 84, 84, 84, 85, 87, 87, 88, 88, 88, 89, 90]
z = np.percentile(x,75)
print(z, "75 th percentile of x")'''


'''x = [75, 77, 78, 78, 80, 81, 81, 82, 83, 84, 84, 84, 85, 87, 87, 88, 88, 88, 89, 90]

z = 75/100
print(z*20)
'''

'''data = np.array([6, 7, 7, 12, 13, 13, 15, 16, 19, 22])
a=stats.zscore(data)
print(a) 
'''


'''data = np.array([6, 7, 7, 12, 13, 13, 15, 16, 19, 22])
a=np.mean(data)
#print(a)

a=np.std(data)
#print(a)


e = 6-13
print(e/a)'''



'''z = x-mean      
    _______
     std
'''

'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.normal(loc=1, scale=2, size=(2, 3))

print(x) 
'''

'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000), hist=False)

plt.show() 
'''
'''import numpy as np
from scipy.stats import kurtosis

x = [55, 78, 65, 98, 97, 60, 67, 65, 83, 65]
a=np.mean(x)
s = np.std(x)'''
#print(s)


#print(kurtosis(x, fisher=False))

#k = E(x-73.3)s
#k = 3*(x-a)/s
#print(k)

'''z =(x-a)/s
print(z)
'''
'''from scipy.stats import kurtosis


x = [55, 78, 65, 98, 97, 60, 67, 65, 83, 65]


print(kurtosis(x, fisher=False))

How do we calculate kurtosis?

k = E ( x − μ ) 4 σ 4 , where μ is the mean of x, σ is the standard deviation of x, and E(t) represents 
the expected value of the quantity t. The kurtosis function computes a sample version of this 
population value.'''



#a2=[[[[2,3,4,5],[40,50,60,90]]]]
#a2=np.array(a2)
#print(a2)
#print(a2[0][0][:,2])
#print(a2[0][0][[0,1],[1,3]])## 3 and 90
#print(a2[0][0][[0,1],[1,2]])## 3 and 60
#print(a2[0][0][[0,0],[1,2]])## note

#print(a2)
'''print(a2[0][0][[0,1],[1,3]])
print(a2[0][0][[0,1],[1,1]])
print(a2[0][0][[0,1],[1,2]])
print(a2[0][0][[0,1],[1,0]])'''
#print(a2[0][0][[0,2],[1,1]])


x = pd.read_csv('iris.csv')
#print(x)
#print(x.shape)
#print(x.head())
#print(x.head(12))
#print(x.tail())
#print(x.tail(12))
#use of iloc[] method

y =x.iloc[30:70,0:]
#print(y)

y = x.iloc[54:69,2:4]
#print(y)

#Use of loc[] method

y = x.loc[30:56,'petal_width']
#print(y)

y = x.loc[40:56,('petal_length','sepal_length')]
#print(y)

#print(x.describe())
#print(x.count())
#print(x.mean())
#print(x.sum())
#print(x.min())
#print(x.max())
#print(x.std())
#print(x.mode())
#print(x.median())
#print(x.value_counts('species'))
#print(x.sort_values(by = 'petal_length'))
y = x.drop([4,6,8], axis=0)
#print(y.head(10))

y = x.drop('petal_length', axis=1)
#print(y)


x =pd.Series([7,8,8,9,9,9,10,11,14,14,15])
#print(x.mode())




'''x = pd.DataFrame({"Name":['Arvind','Akash','Prashant'], 'Marks':[88,98,78]},index =[1,2,3])
y = pd.DataFrame({"Name":['Anurag','Abhinav','Anushka'],'Marks':[87,69,94]},index =[4,5,6])
z = (x,y)
w = pd.concat(z)
print(w)
'''

'''x = pd.DataFrame({"Name":['Arvind','Akash','Prashant'], 'Marks':[88,98,78]},index =[1,2,3])
y = pd.DataFrame({"Name":['Anurag','Abhinav','Anushka'],'Marks':[87,69,94]},index =[4,5,6])
z=x.append(y)
print(z)'''


'''import scipy.stats as stats
 
# Creating data groups
x = np.array([14, 15, 15, 16, 13, 8, 14,
                        17, 16, 14, 19, 20, 21, 15,
                        15, 16, 16, 13, 14, 12])
y = np.array([15, 17, 14, 17, 14, 8, 12,
                        19, 19, 14, 17, 22, 24, 16,
                        13, 16, 13, 18, 15, 13])
 
# Print the variance of both data groups
print(np.var(x), np.var(y))
z = stats.ttest_ind(a=x, b=y, equal_var=True)
print(z)'''



'''import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing,neighbors
import warnings
warnings.filterwarnings('ignore')

ss = pd.read_csv('IRIS.csv')
#print(ss)

x = ss.iloc[0:,2:4]
#print(x)
y = ss.iloc[0:,0:1]
#print(y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = .2, random_state = 10)
#print(x_train)
#print(y_train)
clf = neighbors.KNeighborsClassifier()
print(clf)
'''#sit = KNeighborsClassifier(n_neighbors = 5)
#print(sit)
#aq = sit.fit(x_train, y_train)    #continous error
#print(aq)
#print(aq.predict(x_test))

'''from sklearn import preprocessing
from sklearn import utils

#convert y values to categorical values
lab = preprocessing.LabelEncoder()
y_transformed = lab.fit_transform(y)

#view transformed values
print(y_transformed)

'''

'''import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

ss = pd.read_csv('IRIS.csv')
#print(ss)

x = ss.iloc[0:,2:4]
#print(x)
y = ss.iloc[0:,0:1]
#print(y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = .2)
#print(x_train)
#print(y_train)

knn = KNeighborsClassifier(n_neighbors = 4)
#print(knn)
z=knn.predict(x_test)
print(z)'''

'''import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing,neighbors
import warnings
warnings.filterwarnings('ignore')

ss = pd.read_csv('IRIS.csv')
#print(ss)

x = ss.iloc[0:,2:4]
#print(x)
y = ss.iloc[0:,0:1]
#print(y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = .2, random_state = 10)
#print(x_train)
#print(y_train)
clf = neighbors.KNeighborsClassifier()
#print(clf)
from sklearn.preprocessing import StandardScaler   
st_x= StandardScaler()    
x_train= st_x.fit_transform(x_train)    
x_test= st_x.transform(x_test)  
#print(x_train) 
#print(x_test)    
print(clf.predict(x_test))'''

'''The sklearn. preprocessing package provides several common utility functions and transformer 
classes to change raw feature vectors into a representation that is more suitable for the 
downstream estimators. In general, learning algorithms benefit from standardization of the 
data set.
'''


'''import pandas as pd
import numpy as np 
from sklearn import preprocessing,neighbors
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")


emp = pd.read_csv('Employee_monthly_salary.csv')
print(emp)

m = emp.iloc[0:,6:10]
#print(m)

n = emp.iloc[0:,5:8]
#print(n)

m_train,m_test,n_train,n_test,=train_test_split(m,n,test_size = 15)
#print(m_train)
#print(m_test)
#print(n_train)
#print(n_test)

from sklearn.preprocessing import StandardScaler
kk = StandardScaler()

m_train = kk.fit_transform(m_train)
m_test = kk.fit_transform(m_test)
#print(m_train)
#print(m_test)'''

'''from scipy.stats import chi2_contingency
  
# defining the table
data = [[207, 282, 241], [234, 242, 232]]
stat, p, dof, expected = chi2_contingency(data)
  
# interpret p-value
alpha = 0.05
print("p value is " + str(p))
if p <= alpha:
    print('Dependent (reject H0)')
else:
    print('Independent (H0 holds true)')
'''

'''from scipy.stats import chisquare

a=chisquare([16, 18, 16, 14, 12, 12])
print(a)
'''

'''f_test(x, y):
    x = np.array(x)
    y = np.array(y)
    f = np.var(x, ddof=1)/np.var(y, ddof=1) #calculate F test statistic 
    dfn = x.size-1 #define degrees of freedom numerator 
    dfd = y.size-1 #define degrees of freedom denominator 
    p = 1-scipy.stats.f.cdf(f, dfn, dfd) #find p-value of F test statistic 
    return f, p'''


'''from scipy import stats
import numpy as np 

x = [7, 9, 12, 15, 21]
y = [5, 8, 14, 13, 25]
z = np.array(x)
r = np.array(y)
f = np.var(z)/np.var(r)
print(f)'''

'''from scipy import stats
  
# Defining data groups
x = [7, 9, 12, 15, 21]
y = [5, 8, 14, 13, 25]
z = [6, 8, 8, 9, 5]
  
'''# Conduct the Kruskal-Wallis Test 

'''g = stats.kruskal(x, y, z)
  
print(g)'''

'''import numpy as np 
from sklearn import preprocessing,neighbors,svm
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")


emp = pd.read_csv('C:/Users/shpoo/Desktop/Data set for ML/Employee_monthly_salary.csv')
#print(emp)

#z=emp.drop(['Name','Gender','Date_of_Birth','Join_Date'],1)
#print(z)
#print(z.shape)
m = emp.iloc[0:,6:8]
#print(m)

n = emp.iloc[0:,8:9]
#print(n)

m_train,m_test,n_train,n_test,=train_test_split(m,n,test_size = .25)
#print(m_train)
#print(m_test)
#print(n_train)
#print(n_test)

clf = svm.SVC()
print(clf)
a=clf.fit(m_train, n_train)
print(a)

accuracy = clf.score(m_test,n_test)
print(accuracy)

from sklearn.preprocessing import StandardScaler
kk = StandardScaler()

m_train = kk.fit_transform(m_train)
m_test = kk.fit_transform(m_test)
print(m_train)
#print(m_test)


from sklearn.metrics import confusion_matrix
mc_linear = confusion_matrix(n_test, y_pred_linear)
print(mc_linear)'''


'''from sklearn.preprocessing import StandardScaler
kk = StandardScaler()

m_train = kk.fit_transform(m_train)
m_test = kk.fit_transform(m_test)
#print(m_train)
#print(m_test)

classifier_linear = SVC(kernel = 'linear', random_state = 0)
classifier_linear.fit(m_train,n_train)
y_pred_linear = classifier_linear.predict(m_test)
print(y_pred_linear)

#from sklearn.metrics import confusion_matrix
#mc_linear = confusion_matrix(n_test, y_pred_linear)
#print(mc_linear)

#from sklearn.metrics import classification_report
#class_report_linear = classification_report(n_test, n_pred_linear)
#print(class_report_linear'''


x = pd.read_csv('dataone.csv')
#print(x)

#Change into original data set

'''x.dropna(inplace=True)
print(x)'''

#Change into copy data

'''z = x.dropna()
print(z)'''

'''x.fillna('aaa',inplace=True)
print(x)'''

'''z = x.fillna('aaa')
print(z)'''

'''x['Calories'].fillna(549876,inplace=True)
print(x)
'''
'''z=x['Calories'].fillna(45638748)
print(z)'''


'''x.dropna(inplace=True)
x['Date'] = pd.to_datetime(x['Date'])
print(x)'''

'''z=x.dropna()
z['Date'] = pd.to_datetime(z['Date'])
print(z)'''


'''x.loc[7,'Duration'] = 45
print(x)
'''

#Aggregate methods with the help of groupby()

'''x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(y)'''


'''x = pd.read_csv('C:/Users/shpoo/Desktop/stock-load-ETL')
print(x)
'''

'''import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

rat = pd.read_csv('C:/Users/shpoo/Desktop/Data set for ML/Employee_monthly_salary.csv')
#print(rat)

x = rat.iloc[0:,4:5]
#print(x)
y = rat.iloc[0:,8:9]
#print(y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.25, random_state = 42)
#print(x_train)

from sklearn.preprocessing import StandardScaler
tt = StandardScaler()
x_train = tt.fit_transform(x_train)
x_test = tt.transform(x_test)
#print(x_train)
#print(x_test)

from sklearn.svm import SVC
classifier_linear = SVC(kernel = 'linear', random_state = 0)
classifier_linear.fit(x_train,y_train)
y_pred_linear = classifier_linear.predict(x_test)
#print(y_pred_linear)

from sklearn.metrics import confusion_matrix
mc_linear = confusion_matrix(y_test, y_pred_linear)
#print(mc_linear)

from sklearn.metrics import classification_report, accuracy_score
class_report_linear = classification_report(y_test, y_pred_linear)
#print(class_report_linear)

mid = accuracy_score(y_test, y_pred_linear)
print(mid)'''


'''import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

rat = pd.read_csv('C:/Users/shpoo/Desktop/Data set for ML/Employee_monthly_salary.csv')
#print(rat)

x = rat.iloc[0:,6:8]
#print(x)
y = rat.iloc[0:,8:9]
#print(y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.25, random_state = 0)
#print(x_train)

from sklearn.preprocessing import StandardScaler
tt = StandardScaler()
x_train = tt.fit_transform(x_train)
x_test = tt.transform(x_test)
#print(x_train)
#print(x_test)

from sklearn.svm import SVC
classifier_linear = SVC(kernel = 'linear', random_state = 0)
classifier_linear.fit(x_train,y_train)
y_pred_linear = classifier_linear.predict(x_test)
#print(y_pred_linear)

from sklearn.metrics import confusion_matrix
mc_linear = confusion_matrix(y_test, y_pred_linear)
#print(mc_linear)

from sklearn.metrics import classification_report, accuracy_score
class_report_linear = classification_report(y_test, y_pred_linear)
#print(class_report_linear)

mid = accuracy_score(y_test, y_pred_linear)
print(mid)'''


'''import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

rat = pd.read_csv('C:/Users/shpoo/Desktop/Data set for ML/Employee_monthly_salary.csv')
#print(rat)

x = rat.iloc[0:,4:5]
#print(x)
y = rat.iloc[0:,8:9]
#print(y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.25, random_state = 0)
#print(x_train)

from sklearn.preprocessing import StandardScaler
tt = StandardScaler()
x_train = tt.fit_transform(x_train)
x_test = tt.transform(x_test)
#print(x_train)
#print(x_test)

from sklearn.svm import SVC
classifier_linear = SVC(kernel = 'linear', random_state = 0)
classifier_linear.fit(x_train,y_train)
y_pred_linear = classifier_linear.predict(x_test)
#print(y_pred_linear)

from sklearn.metrics import confusion_matrix
mc_linear = confusion_matrix(y_test, y_pred_linear)
#print(mc_linear)

from sklearn.metrics import classification_report, accuracy_score
class_report_linear = classification_report(y_test, y_pred_linear)
#print(class_report_linear)

mid = accuracy_score(y_test, y_pred_linear)
print(mid)'''

'''import pandas as pd
import numpy as np 
from sklearn import preprocessing,neighbors
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")


emp = pd.read_csv('C:/Users/shpoo/Desktop/Data set for ML/Employee_monthly_salary.csv')
#print(emp)

m = emp.iloc[0:,6:10]
#print(m)

n = emp.iloc[0:,5:8]
#print(n)

m_train,m_test,n_train,n_test,=train_test_split(m,n,test_size = 15)
#print(m_train)
#print(m_test)
#print(n_train)
#print(n_test)

from sklearn.preprocessing import StandardScaler
kk = StandardScaler()

m_train = kk.fit_transform(m_train)
m_test = kk.fit_transform(m_test)
print(m_train)
#print(m_test)'''

'''import numpy as np
import scipy.stats
  
# Create data
group1 = [0.28, 0.2, 0.26, 0.28, 0.5]
group2 = [0.2, 0.23, 0.26, 0.21, 0.23]
  
# converting the list to array
x = np.array(group1)
y = np.array(group2)
  
# calculate variance of each group
print(np.var(group1), np.var(group2))
  
def f_test(group1, group2):
    f = np.var(group1, ddof=1)/np.var(group2, ddof=1)
    a = x.size-1
    b = y.size-1
    p_value = 1-scipy.stats.f.cdf(f, a, b)
    return f, p_value
  
# perform F-test
f_test(x, y)'''


'''from numpy import random

x = random.normal(loc=1, scale=2, size=(2, 3))

print(x) 

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000), hist=False)

plt.show() 
'''

'''from numpy import random

x = random.binomial(n=10, p=0.5, size=10)

print(x)


#Visualization of Binomial Distribution
#Example
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=False, kde=True)

plt.show() '''

'''x = pd.DataFrame()
x.to_excel('uuuuuuu.xlsx')

with pd.ExcelWriter('uuuuuuu.xlsx')as writer:
  x = pd.DataFrame({"Name":["Kajal","Koyal","Kiran"], "Marks": [78,67,92]}, index = [1,2,3])
  x.to_excel(writer,sheet_name='Student marks')
  x = pd.DataFrame({"Fruits":["Apple","Mango","Banana"], "Cost": [89,67,23]}, index = ["a","b","c"])
  x.iloc[0,1] = 200 # You can change in ur existing sheet like this.
  x.to_excel(writer,sheet_name='These are Fruits Names')
  x = pd.DataFrame({"Vegetables":["Potato","Tomato","Peas"], "Cost": [34,56,78]}, index = ["A","B","C"])
  x.to_excel(writer,sheet_name='Vegetables_names')

# Now I want to read my excel sheet one by one.

x = pd.read_excel('uuuuuuu.xlsx',sheet_name='Student marks')
#print(x)

x = pd.read_excel('uuuuuuu.xlsx',sheet_name='These are Fruits Names')
#print(x)

x = pd.read_excel('uuuuuuu.xlsx',sheet_name='Vegetables_names')
#print(x)

#Now I will read all sheets together

x = pd.read_excel('uuuuuuu.xlsx',sheet_name=['Student marks','These are Fruits Names','Vegetables_names'])  
print(x)
'''


'''x = random.poisson(lam=2, size=10)

print(x)

#Visualization of Poisson Distribution
#Example
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.poisson(lam=2, size=1000), kde=False)

plt.show()
'''

'''x = pd.DataFrame({'Name': ["Akash","Akash","Akash","Bhanu","Bhanu","Bhanu","Rahul","Rahul","Rahul"],
  'Subjects':['Python','Maths','Science','Python','Maths','Science','Python','Maths','Science'],
  'Marks' :[65,79,89,55,78,90,112,82,77]})
#print(x)
z=x.pivot(index = 'Name', columns = 'Subjects', values='Marks')
print(z)'''

'''x = pd.DataFrame({"Name":["Ashish","Arun","Anurag"], "Marks": [78,67,92]})
#print(x)
y = pd.DataFrame(x)

School = ['School_A','School_B','School_C']
y['School'] = School
print(y)





x = pd.DataFrame({"Name":["Ashish","Arun","Anurag"], "Marks": [78,67,92],"Roll_no":[11,12,13]})
#print(x)

y=pd.DataFrame(x)
y.insert(0,'School',['School_A','School_B','School_C'])

print(y)
'''


'''x = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two',

                           'two'],

                   'bar': ['A', 'B', 'C', 'A', 'B', 'C'],

                   'baz': [1, 2, 3, 4, 5, 6],

                   'zoo': ['x', 'y', 'z', 'q', 'w', 't']})

#print(x)

z=x.pivot(index='foo', columns='bar', values='baz')
#print(z)

z=x.pivot(index='foo', columns='bar')['baz']
#print(z)

z=x.pivot(index='foo', columns='bar', values=['baz', 'zoo'])
print(z)'''

'''x = pd.DataFrame({'Name': ["Akash","Akash","Akash","Bhanu","Bhanu","Bhanu","Rahul","Rahul","Rahul"],
  'Subjects':['Python','Maths','Science','Python','Maths','Science','Python','Maths','Science'],
  'Marks' :[65,79,89,55,78,90,112,82,77]})
#print(x)
z=x.pivot(index = 'Name', columns = 'Subjects', values='Marks')
print(z)
'''




#print("hello")

#This is my addition programme.

'''a = 34
b = 45
c = a+b 
print(c)
'''

'''a = 56 
b = 66
c = a*b 
print(c)'''


'''a = 56 
b = 66
c = a/b 
print(c)'''



#Indentation Rules, four space or one tab. after colon :

'''x = 9 
if x<20:
  print('hello')'''

import pandas as pd

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Data set for ML/carprices.csv')
#print(x)
a = x[['Mileage','Age(yrs)']]  # this is independent variable
b = x['Sell Price($)']    # this is dependent variable
'''#print(a)
#print(b)

#from sklearn.mode1_selection import train_test_split
'''from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size= 0.3)
print(x_train)
'''

'''df = pd.read_csv('C:/Users/shpoo/Desktop/Data set for ML/carprices.csv')
from sklearn.model_selection import train_test_split

#print(df)

x = df[['Mileage','Age(yrs)']]
y = df['Sell Price($)']
#print(y)
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2)
#print(x_train)
#print(x_test)
#print(y_train)
#print(y_test)
#print(len(x))
print(len(y_train))'''



#Data Type

'''x = 45 
print(type(x))'''

'''x = 45.67 
print(type(x))'''

'''x = 45j 
print(type(x))'''


'''x = 'Arun'
print(type(x))'''


'''x = 45 
print(float(x))'''


'''x = 3.12 
print(complex(x))'''


'''x = 56.3 
print(int(x))

x = 56 
print(complex(x))'''




'''x = pd.read_csv('carprice.csv')
#print(x)
a = x[['Mileage','Age(yrs)']]  # this is independent variable
b = x['Sell Price($)']    # this is dependent variable
#print(a)
#print(b)

from sklearn.mode1_selection import train_test_split

c = x_train,x_test,y_train,y_test = train_test_split(x,y, test_size = 0.3)
print(c)'''


'''x = np.arange(1,11)
y = 2*x
print(x)
print(y)
plt.plot(x,y)
plt.show()
'''

'''x = np.arange(1,11)
y = 2*x
print(x)
print(y)
plt.plot(x,y)
plt.title("SimpleLine Plot")
plt.xlabel("data on x-axis")
plt.ylabel("data on y-axis")
plt.show()
'''

'''x = np.arange(1,11)
y = 2*x
print(x)
print(y)
plt.plot(x,y,color='red',linestyle = ':', linewidth = 5)
plt.title("SimpleLine Plot")
plt.xlabel("data on x-axis")
plt.ylabel("data on y-axis")
plt.show()
'''

'''Vegetables_basket = {"Brinjal":100, "Potatos": 145, "Tomatoes": 123}
Vegetables_names=list(Vegetables_basket.keys())
Vegetables_cost=list(Vegetables_basket.values())
plt.bar(Vegetables_names,Vegetables_cost)
plt.title("Bar Plot")
plt.xlabel("Vegetables_names")
plt.ylabel("Vegetables_cost")
plt.grid(True)
plt.show()'''


'''Vegetables_basket = {"Brinjal":100, "Potatos": 145, "Tomatoes": 123}
Vegetables_names=list(Vegetables_basket.keys())
Vegetables_cost=list(Vegetables_basket.values())
plt.barh(Vegetables_names,Vegetables_cost,color='green')
plt.title("Bar Plot")
plt.xlabel("Vegetables_names")
plt.ylabel("Vegetables_cost")
plt.grid(True)
plt.show()
'''


'''x = 20
if x < 10:
  print('Hello')
else:
  print('goodmorning')
'''

#This is nested if

'''a = int(input("Enter a number: "))
if a > 10:
  print("Above ten")
  if a < 20:
    print("It is above 16 also")
  elif a == 20:
    print("this is elif block")
  else:
    print("Not above 20")

else:
  print('good')

#How can we take user input

x = int(input("Enter a number: "))

if x > 30 and x < 40:
  print('This is good')'''


#Nested if

x = 'Hello Delhi'
#print(type(x))

x = 56 
#print(type(x))

x = 6.34
#print(type(x))

x = 6j 
#print(type(x))

#How can we do Type conversion:

x = 56 
#print(float(x))

x = 56 
#print(complex(x))

x = 3.12 
#print(int(x))
#print(complex(x))

'''x = 0 
while x<5:
  print('Hello')
  x+=1'''


'''x = 1 
while x < 11:
  print(x)
  x+=1'''

'''x = 10 
while x>0:
  print(x)
  x-=1'''

'''x = int(input('Enter a number: '))
y = 1
while y<=10:
  print(x*y)
  y+=1'''

'''x = int(input('Enter a number: '))
y = 1 
z = 1
while y<=x:
  if z%2==0:
    print(z)
    z+=1
  y+=1'''


'''x = int(input('enter a number: '))
  y = 1 
  z = 0
  c=0
  while y<=x:
    z+=1
    if z%2==0:
      print(z)
      y+=1
      c+=z
  print('Sum of all even numbers: ', c)
  '''  

'''i = 1
while i < 10:
  if i == 8:
    break
  print(i)
  i += 1'''

'''x = int(input("Enter a number: "))
z = 0
y = 0
c = 0
while z < x:
   y+=1
   if y%2==0:
      print(y)
      z+=1
      c+=y
print("sum of n even numbers:", c)'''

'''x = int(input('Enter a number: '))
z = 0 
y = 0 
while z < x:
  y+=1
  if y%2==0:
    print(y)
    z+=1'''


'''i = 1
while i < 10:
  print(i)
  if i == 8:
    break
  #print(i)
  i += 1
'''

'''x = 3 
if x<20 and x>1:
  print('True')
else:
  print('False')'''


'''x = 3 
if x<20 or x>45:
  print('True')
else:
  print('False')'''

'''x = 30 
if x<20 or x>45:
  print('True')
else:
  print('False')'''

'''x = 3
if x<20 and x>45:
  print('True')
else:
  print('False')'''

'''x = 3
if not(x<20 and x>45):
  print('True')
else:
  print('False')'''


'''x = 30
if not(x<20 or x>45):
  print('True')
else:
  print('False')'''


'''x = ['apple','mango','banana']
y = ['apple','mango','banana']
if x is y:
  print('True')
else:
  print('False')
'''

'''x = ['apple','mango','banana']
y = ['apple','mango','banana']
if x is not y:
  print('True')
else:
  print('False')
'''

'''x = ['apple','mango','banana']
y = ['apple','mango','banana']
if x == y:
  print('True')
else:
  print('False')
'''

'''x = ['apple','mango','banana']
if'apple' in x:
  print('True')
else:
  print('False')
'''

'''x = ['apple','mango','banana']
if'apple' not in x:
  print('True')
else:
  print('False')

'''

'''x = np.arange(1,11)
y = 2*x
print(x)
print(y)
ax=plt.axes()
ax.set_facecolor('pink')
plt.plot(x,y)
plt.show()
'''

'''Vegetables = ["Potato","Tomato","Brinjal","chilly"]
Cost= [64,34,100,56]
plt.pie(Cost,labels=Vegetables)
plt.show()
'''

'''Vegetables = ["Potato","Tomato","Brinjal","chilly","carrot"]
Cost= [64,34,100,56,78]
plt.pie(Cost,labels=Vegetables,autopct='%0.2f%%',colors=['yellow','purple','green','red','teal'])
plt.show()
'''

'''Vegetables = ["Potato","Tomato","Brinjal","chilly","carrot"]
Cost= [64,34,100,56,78]
plt.pie(Cost,labels=Vegetables,radius=1)
plt.pie(Cost,labels=Vegetables,autopct='%0.1f%%',colors=['yellow','grey','green','red','blue'])
plt.pie([1],colors=['w'],radius=0.4)
plt.show()
'''


'''x = sns.load_dataset("fmri")
y=x.head()
#print(y)
sns.lineplot(x="timepoint",y = "signal",data=x,hue = 'event',style = 'event',markers=True)
plt.show()
'''

'''x=pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/pokemon.csv')
y=x.head()
print(y)
sns.set(style = "whitegrid")
sns.barplot(x="Legendary",y="Speed",data=x)
plt.show()
'''


'''x=pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/pokemon.csv')
print(x)
sns.set(style = "whitegrid")
sns.barplot(x="Legendary",y="Speed",hue = "Generation",data=x)
plt.show()
'''

'''x=pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/pokemon.csv')
y=x.head()
#print(y)
sns.set(style = "whitegrid")
sns.barplot(x="Legendary",y="Speed",data=x,color = "yellow")
plt.show()
'''

'''x = pd.read_csv('iris.csv')
y=x.head()
print(y)
sns.scatterplot(x = 'sepal_length',y = 'petal_length',hue = 'species', style ='species',data=x)
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/diamonds.csv')
y=x.head()
print(y)
sns.distplot(x['price'])
plt.show()'''

import warnings
warnings.filterwarnings('ignore')

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/diamonds.csv')
y=x.head()
print(y)
sns.displot(x['price'])
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/diamonds.csv')
y=x.head()
print(y)
sns.distplot(x['price'],rug = True)
plt.show()
'''
'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/diamonds.csv')
y=x.head()
print(y)
sns.displot(x['price'],color = 'purple')
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/diamonds.csv')
y=x.head()
#print(y)
sns.distplot(x['price'],color="g",kde=False)
plt.show()
'''
'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/diamonds.csv')
y=x.head()
#print(y)
sns.distplot(x['price'],color="b",hist=False)
plt.show()
'''
'''tes = input("Enter the number:")

tes = int(tes)

while():
'''
'''n = int(input("Enter a number: "))
if n<2:
  print("Not a Prime number")
else:
  for i in range(2,n):
    #print(i)
    if n%i==0:
      print("Not a Prime Number")
      break
  else:
    print("Number is prime")'''

'''x = int(input('enter a number: '))
#z= int(input('enter a number'))
s=1
if x<2:
  print('Not a Prime Number')
else:
  while x>s:
    if x%2==0:
      print(x)
    #else:
      #print(s)
    s+=1
'''

#PRIME NUMBER WITH THE HELP OF PRIME NUMBER

'''z = 0
n = int(input('Enter a number : '))
i = 2
while i <= (n/2):
    if (n%i) == 0:
        z = 1
        break
    i += 1
if n == 1:
    print('1 is not a prime number')
elif z == 0:
    print(n,' is a prime number.')
elif z == 1:
    print(n,' is not a prime number.')
'''

'''z = 1 
n = int(input('enter a number: '))
while z<=n:
  z+=1
  if z%2!=0:
    print(z)
  elif n<2:
          print('Not prime')
        else:
          print('prime')
      '''

#Use of for loop

'''x = ('apple','Banana','Mango','papaya')
for i in x:
  print(i)'''

#Use of range function in for loop:


'''for i in range(10):
    print(i)
  '''

'''for i in range(2,11):
  print(i)
'''

'''for i in range(2,22,2):
  print(i)'''


'''z = 0
n = int(input('Enter a number : '))
i = 2
while i <= (n/2):
    if (n%i) == 0:
        z = 1
        #print(z)
        print(n)
        break
    i += 1
'''
'''if n == 1:
    print('1 is not a prime number')
elif z == 0:
    print(n,' is a prime number.')
elif z == 1:
    print(n,' is not a prime number.')

'''

# Use of break and continue statement in for loop:

'''days = ["sun","Mon","Tues","wed","Thurs","Friday","Sat"]
for i in days:
  print(i)
  if i == "wed":
    break'''


'''days = ["sun","Mon","Tues","wed","Thurs","Friday","Sat"]
for i in days:
  if i == "wed":
    break
  print(i)
'''

'''days = ["sun","Mon","Tues","wed","Thurs","Friday","Sat"]
for i in days:
  if i == "wed":
    continue
  print(i)'''


#print odd number from 1 to 10.
'''sum=0
for i in range(1,11):
  if(i%2!=0):
    print(i)
    sum+=i
print("This is the sum of all odd numbers: ", sum)'''

#How can we take user input
'''x = int(input("Enter a number: "))
if x < 20:
  print('hello')
else: 
  print('runaway')

a = 100
b = 35
c = 200
'''
'''if a > b and c > a:
  print("Both conditions are True")
'''

'''if a < b and c > a:
  print("Both conditions are True")
else:
  print("this is false")
'''


'''if a < b or c > a:
  print("Atleast one condition should be true")
else:
  print("this is false")
'''

#How can we take user input
'''x = int(input('Enter a number: '))
y = int(input('Enter a number: '))

if x>y and y<x:
  print('True')
else:
  print('False')
'''

'''x=int(input("Enter the number to caluclate factorial: "))
a = 1
while x>0:
  a = x*a
  #print(a)
  x-=1
print(a)
'''

'''for i in range(6):
  for y in range(i):
    print("*",end=" ")
  print()


*
* *
* * *
* * * *
* * * * *

* * * * *
* * * * 
* * *
* *
*

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5


1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

5 5 5 5 5 
4 4 4 4
3 3 3
2 2
1

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1'''

'''x = int(input("Enter a number: "))
for i in range(x):
  for j in range(i+1):
    print(1, end="")
  print("\n")
'''

'''x = int(input("Enter a number: "))
for i in range(x):
  for j in range(i+1):
    print(1, end=" ")
  print("\n")
'''
'''x = int(input("enter a number: "))
for i in range(x,0,-1):
  #print(i)
  for y in range(i):
    print("*",end=" ")
  print()
'''

'''x = int(input("Enter a number: "))
for i in range(x):
  for j in range(1,i+1):
    print(j, end=" ")
  print("\n")
'''

'''x = int(input("Enter a number: "))
for i in range(1,x):
  for j in range(1,i):
    print(j, end=" ")
  print("\n")
'''


'''for i in range(1,5):
  for y in range(i):
    print(y,end=" ")
  print()
'''
'''x = int(input('enter a number: '))
for i in range(x+1):
  for y in range(i):
    print(i,end=' ')
  print(' ')'''


#String or text or character

'''x = 'hello delhi'
print(x)
'''
'''x = "hello delhi"
print(x)
print(type(x))
print(len(x))

print(x[1])
print(x[-10])
print(x[1:7])
print(x[-10:-4])

x = 'ARUNACHAL PRADESH'
Find the type of this Data
find the length 
extract U, D, S, L, N 

extract NA (NACHA) 
A to D (AL PRAD)
D to H (DESH)
R to N (RUN)
R to D (RUNACHAL PRAD)
D TO E (DE)'''


#Python - Modify Strings

a = "Hello Delhi"
#print(a.upper())


#The lower() method returns the string in lower case:
a = "Hello Delhi"
#print(a.lower())


'''Remove Whitespace

Whitespace is the space before and/or after the actual text, and very often you want to remove 
this space. Example

The strip() method removes any whitespace from the beginning or the end:'''

a = " Hello, Delhi "
#print(a)
#print(a.strip())


'''Replace String
Example

The replace() method replaces a string with another string:'''

a = "Hello, Delhi"
#print(a.replace("H", "J"))


#Split String

'''The split() method returns a list where the text between the specified separator becomes the list items.
Example



The split() method splits the string into substrings if it finds instances of the separator:'''
a = "Honesty is the best policy"
#print(a.split())


'''String Concatenation

To concatenate, or combine, two strings you can use the + operator.
Example

Merge variable a with variable b into variable c:'''
'''a = "Hello"
b = "Delhi"
c = a + b
print(c)'''


#To add a space between them, add a " ":
'''a = "Hello"
b = "World"
c = a + " " + b
print(c)

x = 'Hello'
y = 'Delhi'
c= x,y 
print(c)'''


'''Honesty is the best policy


Hello
India

x = HIMACHAL PRADESH

print this in reverse.'''

'''a = 89
if a > 10:
  print("Above ten")
  if a < 20:
    print("It is above 20 also")
  elif a == 20:
    print("this is elif block")
  else:
    print("Not above 20")'''


#Nested if/else:


'''x = int(input("enter a number: "))
if x<=100:
  print('This is mango')
  if x < 20:
    print('This is apple')
  elif x==99:
    print('This is banana')
  else:
    print('This is not good')
else:
  print("Number out of range")
'''

'''Take user input if number is less than and equal to 23 so enter into the if block
and if number is equal to 14 then print number is equal to 14 if number is less than
13 then print number is less than 13, if number is greater than 20 then print
number is greater than 20, else print number doesn't match with 13 and 20. and if 
all conditions are not satisfied then print number out of range.
'''


'''The format() method takes the passed arguments, formats them, 
and places them in the 
string where the placeholders {} are:

Example

Use the format() method to insert numbers into strings:'''

'''age = 16
a = "My name is Ashu, and I am {} years old"
print(a.format(age))
'''
'''The format() method takes unlimited number of arguments, and 
are placed into the 
respective placeholders:

Example'''

'''quantity = 13
item_no = 765
price = 89.67
order = "I want {} pieces of item_no {} for {} dollars."
print(order.format(quantity, item_no, price))'''

'''You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
Example
'''
'''quantity = 12
item_no = 112
price = 78.98
order = "I want to pay {2} dollars for {0} pieces of item {1}."

print(order.format(quantity, item_no, price))
'''


'''x = 'Hello Delhi'
  i=0
  #print(len(x))
  while i<(len(x)):
    print(x[i])
    i+=1
  '''  
'''for i in x:
  print(i)'''

'''x = 'Hello Delhi'
y = len(x)-1
#print(y)
i = 0 
while y>=i:
  print(x[y])
  y-=1
'''
'''x = 'Hello Delhi'
z=len(x)-1
#print(z)
for i in range(z,-1,-1):
  print(x[i])'''

'''x="hello delhi"
a=len(x)-1
y=0
while y<=a:
  print(x[a],end=" ")
  a=a-1
'''

'''x="hello delhi"
a=len(x)-1
y=0
while y<=a:
  print(x[a],end=" ")
  a=a-1'''




'''x = 'HIMACHAL PRADESH'

print this with the help of while loop and for loop, print this in reverse way with the help
of while loop and for loop.'''


'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
print(y)
sns.boxplot(x='InternetService',y='MonthlyCharges',data=x)
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
#print(y)
sns.boxplot(x='InternetService',y='tenure',data=x,color="yellow",linewidth=3)
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
#print(y)
sns.boxplot(x='Contract',y='tenure',data=x,color="green",linewidth=3)
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
#print(y)
sns.boxplot(x='Contract',y='tenure',data=x,order=["Two year","Month-to-month","One year"])
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
print(y)
sns.boxplot(x='Contract',y='tenure',data=x,hue="PaymentMethod")
plt.show()
'''

'''x = sns.load_dataset("iris")
y=x.head()
print(y)
sns.pairplot(x, hue="species")
plt.show()
'''

'''x = pd.read_csv('iris.csv')
y=x.head()
print(y)
sns.pairplot(x,hue ="species")
plt.show()
'''
'''x = pd.read_csv('iris.csv')
y=x.head()
print(y)
sns.pairplot(x)
plt.show()
'''


'''x = pd.read_csv('C:/Users/shpoo/Desktop/IRIS.csv')
#print(x)
print(x.head())
plt.hist(x['sepal_length'],bins=30,color="g")
plt.show()
'''


'''x = pd.read_csv('C:/Users/shpoo/Desktop/IRIS.csv')
#print(x)
print(x.head())
plt.hist(x['sepal_length'],color="g")
plt.show()
'''



'''x = pd.read_csv('C:/Users/shpoo/Desktop/IRIS.csv')
print(x)
print(x.head())
plt.hist(x['petal_length'],color="r")
plt.show()
'''


'''one = [1,2,3,4,5,6,7,8,9]
two = [1,2,3,4,5,4,3,2,1]
three = [6,7,8,9,8,7,6,5,4]

x = list([one,two,three])

plt.boxplot(x)
plt.show()
'''



'''one = [1,2,3,4,5,6,7,8,9]
two = [1,2,3,4,5,4,3,2,1]
three = [6,7,8,9,8,7,6,5,4]

x = list([one,two,three])

plt.violinplot(x,showmedians=True)
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')
y = x.head()
#print(y)
sns.boxplot(x='Contract',y='tenure',data=x,order=["Two year","Month-to-month","One year"])
plt.show()
'''

'''x = pd.read_csv('C:/Users/shpoo/Desktop/Datasets/ONE/Churn.csv')

y = x.head()
#print(y)
sns.boxplot(x='Contract',y='tenure',data=x,order=["One year","Month-to-month","Two year"])
plt.show()
'''

'''with pd.ExcelWriter('U9.xlsx')as writer:
  x = pd.DataFrame({"Name":["Kajal","Koyal","Kiran"], "Marks": [78,67,92]}, index = [1,2,3])
  x.to_excel(writer,sheet_name='Sheet1')
  x = pd.DataFrame({"Fruits":["Apple","Mango","Banana"], "Cost": [89,67,23]}, index = ["a","b","c"])
  x.iloc[0,1] = 900 # You can change in ur existing sheet like this.
  x.to_excel(writer,sheet_name='Sheet2')
  x = pd.DataFrame({"Vegetables":["Potato","Tomato","Peas"], "Cost": [34,56,78]}, index = ["A","B","C"])
  x.to_excel(writer,sheet_name='Sheet3')
'''



'''x = pd.read_csv('iris.csv')
#print(x)
z=x.head()
y=x.tail()
w=x.iloc[1:30,2:4]
x.to_excel('prabhu.xlsx')
with pd.ExcelWriter('prabhu.xlsx')as writer:
  x=z
  x.to_excel(writer,sheet_name='First Five Rows')
  x=y
  x.iloc[0,2]=2000000 #How can we change in excel sheet from pandas
   
  x.to_excel(writer,sheet_name='Bottom five Rows')
  x=w 
  x.to_excel(writer,sheet_name='Two columns')

x = pd.read_excel('prabhu.xlsx',sheet_name='First Five Rows')
#print(x)

x = pd.read_excel('prabhu.xlsx',sheet_name='Bottom five Rows')
#print(x)

x = pd.read_excel('output.xlsx',sheet_name='Two columns')
#print(x)

#Now I will read all sheets together'''

'''x = pd.read_excel('output.xlsx',sheet_name=['First Five Rows','Bottom five Rows','Two columns'])  
print(x)'''


'''x=str(input("enter text : "))
a=len(x)
for i in range(a-1,-1,-1):
  print(x[i],end=" ")


x = 'Arunachal Pradesh'
Count the vowel from this string.

Take user input and count the vowels in this string. 
'''

#x = int(input("Enter a number: "))
'''x= 10
z = 0
y = 0
while z < x:
   y+=1
   if y%2==0:
      print(y)
      z+=1
'''

#print 10 even numbers with the help of while loop.

'''x = int(input('enter a number: '))
z = 0 
y = 0 
while z<x:
  y+=1
  if y%2==0:
    print(y)
    z+=1
'''
#How can we print random number of table

'''x = 2
y = 0 
while y<10:
  y+=1
  print(x*y)'''


'''cm = confusion_matrix(a,model_pred)
cm

cm = confusion_matrix(y.argmax(axis=1),yhat.argmax(axis=1))

 confusion_matrix(
    y_test.values.argmax(axis=1), predictions.argmax(axis=1))'''



'''Create a list with help of 8 items.
and extract the values with the help of negative and positive indexing. 

extract, item 3,6,8,1,4,5 
Extract items third to sixth item 
Extract items fourth to last item 
Extract items fifth to six item 
Extract items first to second last item 
Extract items second to seventh item 
Reverse this list.
'''


'''x = 'hello' 
z = len(x)
#print(z)
y = 0
while y<z:
  print(x[y])
  y+=1
'''

'''x = 'hello' 
z = len(x)
y = 0
c=0
while y<z:
  if x[y] == 'a' or x[y] == 'e' or x[y]== 'i' or x[y]== 'o' or x[y]== 'u':
    print(x[y])

  y+=1
'''

'''x = 'hello' 
z = len(x)
y = 0
c=0
while y<z:
  if x[y] == 'a' or x[y] == 'e' or x[y]== 'i' or x[y]== 'o' or x[y]== 'u':
    print(y)

  y+=1
'''

#Find the number of vowels in any string

'''x = str(input('Enter a number: '))
z= len(x)
y=0
for i in range(z):
  if x[i] == 'a' or x[i] == 'e' or x[i] == 'i' or x[i] == 'o' or x[i] == 'u' or x[i] == 'A' or x[i] == 'E'or x[i] == 'I' or x[i] == 'O' or x[i] == 'U':
    count=1
    y+=count
print('This is total number of string',y)'''
  


#Find the vowels in this random string

'''x = str(input('Enter a number: '))
z= len(x)
y=0
for i in range(z):
  if x[i] == 'a' or x[i] == 'e' or x[i] == 'i' or x[i] == 'o' or x[i] == 'u' or x[i] == 'A' or x[i] == 'E'or x[i] == 'I' or x[i] == 'O' or x[i] == 'U':
    print(x[i])
'''


#Find the index where vowels are situated in this string

'''x = str(input('Enter a number: '))
z= len(x)
y=0
for i in range(z):
  if x[i] == 'a' or x[i] == 'e' or x[i] == 'i' or x[i] == 'o' or x[i] == 'u' or x[i] == 'A' or x[i] == 'E'or x[i] == 'I' or x[i] == 'O' or x[i] == 'U':
    print(i)
'''


'''x = sns.load_dataset("iris")
y=x.head()
print(y)
#sns.pairplot(x) 
sns.pairplot(x, hue="species")

plt.show()
'''

'''x = []
for i in range(1,11):
  x.append(i)
print(x)'''


'''x = []
y=0 
while y<100:
  y+=1
  x.append(y)
print(x)'''

'''x = int(input('Enter a number: '))
y = 1 
z=0
while x>z:
  y=x*y
  x-=1
print(y)'''

'''x = []
for i in range(1,11):
  #print(i)
  x.append(i)
print(x)'''

'''x = [1,2,["sun","mon",["apple","banana"],"Tues"],5,6]
x[2][2].insert(1,'mango')
print(x)'''

#Try to make a dynamic list with the help of eval() method.

#x = eval(input('Enter any value: '))
'''y = 0 
z = []
while y<=5:
  x = eval(input('Enter any value: '))
  z.append(x)
  y+=1
print(z)
'''
'''import pandas as pd  
df = pd.read_csv('C:/Users/shpoo/Downloads/archive(28)/zomato.csv')
print(df)'''

'''a = int(input('enter a number: '))
x = []
y = 0 
while y<a:
  z = eval(input('Enter a number: '))
  x.append(z)
  y+=1
  s=tuple(x)
print(s)'''


'''a = int(input('Enter a number: '))
y = 0 
z =[]
while y<a:
  x = eval(input('enter any element: '))
  z.append(x)
  y+=1
  s = set(z)
print(s)
'''

'''x = [[[]]]
  a = int(input('Enter a number: '))
  y = 0 
  while y<a:
  '''  

#First five even numbers
'''y = 0
z = 10 
while y<z:
  y+=1
  if y%2==0:
    print(y)
'''
'''x = int(input('enter a number: '))
y = 0
z = 0 
while z<x:
  y+=1
  if y%2==0:
    print(y)
    z+=1
'''

'''x = int(input('enter a number: '))
z = 0 
y = 0 
while z<x:
  y+=1
  if y%2==0:
    print(y)
    z+=1
'''

'''x = {'sunday','monday','tuesday','wednesday','thursday','friday','saturday'}
y = list(x)
s = len(y)
z = 0
while z<s:
    #print(y[z])
    z+=1
x=set(y)
print(x)'''


'''days = ["sun","Mon","Tues","wed","Thurs","Friday","Sat"]
for i in days:
  if i == "wed":
    break
  print(i)


days = ["sun","Mon","Tues","wed","Thurs","Friday","Sat"]
for i in days:
  if i == "wed":
    continue
  print(i)
'''

'''i = 0
  while i < 10:
    i += 1
    if i == 8:
      continue
    print(i)
  '''  


'''for i in range(1,11):
  if i == 6:
    break
  print(i)'''

'''for i in range(1,11):
  if i == 6:
    continue
  print(i)
'''

'''x = int(input('Enter a number: '))
y = 0 
z = 1
while y<x:
  z=z*x
  x-=1
print('Factorial of this number is', z)'''

'''x = int(input('Enter a number: '))
z=1
for i in range(x,0,-1):
  z=z*i
  i-=1
print('This is the factorial of this number:', z)'''

#create a tuple and fill only even eight numbers
#create a tuple and fill only odd eight numbers
#Create a tuple and extract string where put any vowel.
#print a string and count how many vowels has in this string.
#print a string and find the vowels in this string.

'''x = int(input('enter a number: '))
    y = []
    z = 0 
    s = 0
    while z<x:
      s+=1
      if s%2==0:
        y.append(s)
        z+=1
    r=tuple(y)
    print(r)
    '''    


'''x=['apple', 'mango', 'ghjy','llrrt', 'kkllr']
y=len(x)
z = 0 

while z<y:
  if x[z]=='apple'or x[z]=='mango':
    print(x[z])
  z+=1
'''


#if x[z]=='a'or x[z]=='e' or x[z]=='i'or x[z]=='o' or x[z]=='u'or x[z]=='A'or x[z]=='B':
  
'''x = int(input("Enter a number: "))
for i in range (1,x*2+1):
  if i%2==0:
    print(i)
'''
'''x = int(input("Enter a number: "))
for i in range(0,x*2,2):
  print(i)'''


'''x = int(input('Enter a number: '))
for i in range(1,x*2+1):
  if i%2==0:
    print(i)
'''
'''y = []
x = int(input('enter a number: '))
for i in range(2,x*2+1,2):
  y.append(i)
s=set(y)
print(s)'''




'''x = pd.DataFrame()
x.to_excel('Sandeep.xlsx')

with pd.ExcelWriter('Sandeep.xlsx')as writer:
  x = pd.DataFrame({"Name":["Kajal","Koyal","Kiran"], "Marks": [78,67,92]}, index = [1,2,3])
  x.to_excel(writer,sheet_name='Sheet1')
  x = pd.DataFrame({"Fruits":["Apple","Mango","Banana"], "Cost": [89,67,23]}, index = ["a","b","c"])
  x.iloc[0,1] = 90000000 # You can change in ur existing sheet like this.
  x.to_excel(writer,sheet_name='Sheet2')
  x = pd.DataFrame({"Vegetables":["Potato","Tomato","Peas"], "Cost": [34,56,78]}, index = ["A","B","C"])
  x.to_excel(writer,sheet_name='Sheet3')
'''


#x = pd.read_csv('iris.csv')
#print(x)
'''z=x.head()
y=x.tail()
w=x.iloc[1:30,2:4]
with pd.ExcelWriter('output.xlsx')as writer:
  x=z
  x.to_excel(writer,sheet_name='First Five Rows')
  x=y 
  x.to_excel(writer,sheet_name='Bottom five Rows')
  x=w 
  x.to_excel(writer,sheet_name='Two columns')

x = pd.read_excel('output.xlsx',sheet_name='First Five Rows')
#print(x)

x = pd.read_excel('output.xlsx',sheet_name='Bottom five Rows')
#print(x)

x = pd.read_excel('output.xlsx',sheet_name='Two columns')
#print(x)

#Now I will read all sheets together

x = pd.read_excel('output.xlsx',sheet_name=['First Five Rows','Bottom five Rows','Two columns'])  
print(x)
'''

'''x = int(input('Enter a number: '))
y = []
z = 0 
while z<x:
  s = eval(input('Enter any element: '))
  y.append(s)
  z+=1
r=tuple(y)
print(r)'''



'''x = int(input('Enter a number: '))
y = 0 
z={}
while y<x:
  s = eval(input('Enter key: ' ))
  g = eval(input('Enter values: '))
  z[s]=g
  y+=1

print(z)'''


'''Take user input and make list with only even numbers.

Take user input and make a dyanamic list.

Take user input and make a dyanamic tuple and set with the help of while and for loop.

Take user input and make a dyanamic dictionary with the help of while and for loop 
'''

















'''x = int(input('Enter a number: '))
y = []
s = 0
for i in range(x):
  s+=1
  if s%2==0:
    y.append(s)
print(y)
'''

'''x = int(input('Enter a number: '))
y = []
z = 0 
s = 0
while z<x:
  s+=1
  if s%2==0:
    y.append(s)
    z+=1
print(y)
'''


'''x = int(input('Enter number of elements: '))
z = 0 
y = []
while z<x:
  s = eval(input('Enter the elements: '))
  y.append(s)
  z+=1
#print(y)
a=tuple(y)
#print(a)
r = set(y)
print(r)
'''

#make a list with square values

'''x = int(input('Enter any value: '))
z = 1 
y = []
while z<=x:
  y.append(z**2)
  z+=1
print(y)'''


'''x = int(input('Enter any number: '))
z = 0 
y = []
while z<x:
  s = int(input('Enter any number: '))
  y.append(s**2)
  z+=1 
print(y)'''


'''x = int(input('Enter any value: '))
z = 0 
y = []
while z<x:
  s = int(input('Enter any number: '))
  y.append(s**3)
  z+=1 
print("These are the cubes of all numbers: ",y)'''

# I want counting between 100 to 300 which is divisible by 3 only.

'''Implementing end to end data pipelines for serving reporting and data science capabilities.
Work with AI/ML algorithms like Classification Model, Prescriptive Models ,Time Series Models, 
Deep Learning Models, & Clustering Models.'''


'''x = 99
y = 200

while x<y:
  x+=1
  if x%3==0:
    print(x)
'''

'''x = 100
count=0

for i in range(x,300):
  if i%3==0:
    print(i)
    count+=1
print('Total Numbers are: ', count)'''


'''Take user input
x = "Honesty is the best policy" print this string in order and in reverse order with the help of 
while and for loop.'''


'''x = str(input('Enter any string: '))
y = len(x)
z = 0 
while z<y:
  print(x[z])
  z+=1
'''

'''x = str(input('Enter any string: '))
y = len(x)-1
z = 0 
while z<=y:
  print(x[y])
  y-=1
'''
#x = str(input('Enter any string: '))

'''a =[10,20,30,40,50]

def x(n):
  return n*2

result = map(x,a)
#print(result)
#print(type(result))
for i in result:
  print(i)'''

'''x = [10,20,30,40,50]
z=[]
for i in x:
  y=i+2
  z.append(y)
  print(y)
print(z)'''


'''x = [10,20,30,40,50]

def a(n):
  return n*2


o=map(x,a)
for i in o:
  print(i)'''


'''x = 56j
print(abs(x))
'''

'''x = int(input('Enter the elements of dictionary: '))
y = {}
z = 0
while z'''


'''class car:
  def __init__(self,make,model,year):
    self.make=make
    self.model=model
    self.year=year
    #print(self.model)
  def Q (self):
    return("This is awesome car")

class electric(car):
  def __init__(self,make,model,year,color):
    super(). __init__(make,model,year)
    self.color=color
    
z=electric("Honda",2000,2019,"Red")
print(z.Q())
print(z.make)
print(z.model)
print(z.year)
print(z.color)
'''


'''class car:
  def A(self,make,model,year):
    self.make=make
    self.model=model
    self.year=year
    #print(self.model)
  def Q (self):
    return("This is awesome car")

class electric(car):
  def __init__(self,make,model,year,color):
    super(). A(make,model,year)
    self.color=color
    #print(make)
    #print(model)
    #print(color)
z=electric("Honda",2000,2019,"Red")
print(z.Q())
print(z.make)
print(z.model)
print(z.year)
print(z.color)
'''

'''class Gparent():
  def first(self):
    print("Apple is good for health")
class parent(Gparent):
  def second(self):
    print("Honesty is the best policy")
class child(parent):
  def third(self):
    print("Apple is good for health")

ob = child()
ob.first()
ob.second()
ob.third()
'''

'''class Parrot:
  def fly(self):
    print("Parrot can fly")
  def swim(self):
    print("Parrot can't swim")

class Penguin:
  def fly(self):
    print("Penguin can't fly")
  def swim (self):
    print("Penguin can swim")

def flying_test(self):
  self.fly()
  self.swim()

bird = Parrot()
Peggy = Penguin()

flying_test(bird)
flying_test(Peggy)
'''


'''class first:
    def a(self,q,w):
        self.q=q
        self.w=w
        self.e=q-w
    def b(self,q,w):
        print('this is my substraction')
class second:
    def a(self,q,w):
        print('I can do it')
    def b(self,q,w):
        self.q=q
        self.w=w
        self.x=q+w
class third:
    def a(self,j,k):
        print('have a good day')
    def b(self,s,z):
        self.s=s
        self.z=z
        self.d=s*z
def sun(self):
    self.a(6,4)
    self.b(3,4) 
ob=first()
ob1=second()
ob2=third()
sun(ob)
print(ob.e)
sun(ob1)
print(ob1.x)
sun(ob2)
print(ob2.d)'''


'''x = int(input('Enter a number: '))
y = 0 
z = 0
while y<x:
  y+=1
  z+=y 
  print(y)

print('Sum of these numbers: ', z)
'''



'''def sum():
  y = 0 
  z = 0
  x = int(input('Enter a number: '))
  while y<x:
    y+=1
    z+=y 
    print(y)
  print('Sum of these numbers: ', z)

sum()
'''

'''x = int(input('Enter a number: '))
y = []
z = 0
while z<x:
  s = eval(input('enter a number'))
  z+=1
  y.append(s)
print(y)
'''

'''x = int(input('Enter a number: '))
y = []
z = 0 
while z<x:
  z+=1
  y.append(z)
print(y)'''


'''x = open("New_3.py", "w")
x.write("write method will overwrite the content")
x = open("New_3.py", "r")
print(x.read())
'''

'''z = open("z9.py", "x")
z = open("z9.py","w")
z.write("apple is good for health")
z = open("z9.py","r")
print(z.read())'''


'''x = open('New_4.py','x')
x.write('Apple is good for health')
x = open('New_4.py','r')
print(x.read())
'''

'''import os
os.remove("New_3.py")
'''

'''import os
os.rmdir("www")
'''

'''x = int(input('Enter a number: '))
y = 0 
z = []
while y<x:
  y+=1
  z.append(y)
print(z)
'''


#take user input
'''String = str(input('enter any string: '))
for i in String:
    #initialize a count variable
    count = 0
    for j in String:
        #check for repeated characters
        if i == j:
            count+=1
        #if character is found more than 1 time
        #brerak the loop
        if count > 1:
            break
    #print for nonrepeating characters
    if count == 1:
        print(i,end = " ")'''


'''x = str(input('Enter any string: '))
for i in x:
  a = 0

  for j in x:
    if i == j:
      a+=1
    elif a > 1:
      break
  if a == 1:
    print(i,end = " ")
'''

'''x = str(input('Enter any string: '))
a = 0
for i in x:
  for j in x:
    if i == j:
      a+=1
    elif a > 1:
      break
  if a == 1:
    print(i,end = " ")
'''
    
'''x = str(input('Enter any string: '))
for i in x:
  a = 0
  for j in x:
    if i == j:
      a+=1
    elif a>1:
      break
  if a == 1:
    print(i, end=" ")'''



'''a = 89
if a > 10:
  print("Above ten")
  if a < 20:
    print("It is above 20 also")
  elif a == 20:
    print("this is elif block")
  else:
    print("Not above 20")'''

'''x = 0
while x < 10:
  x += 1
  if x == 7:
    continue
  print(x)
'''

# Use of for loop

'''x = 'hello'
for i in x:
  print(i)
'''
'''x = [1,2,3,4,5,6]
for i in x:
  print(i)'''


'''x = ['apple','mango','banana','orange']
for i in x:
  print(i)'''

'''for i in range(10):
  print(i)
'''


'''for i in range(2, 10):
  print(i)'''

'''for i in range(2, 22, 2):
  print(i)'''


'''x = pd.read_csv('iris.csv')
#print(x)
z=x.head()
y=x.tail()
w=x.iloc[1:30,2:4]
x.to_excel('put.xlsx')
with pd.ExcelWriter('put.xlsx')as writer:
  x=z
  x.to_excel(writer,sheet_name='First Five Rows')
  x=y 
  x.to_excel(writer,sheet_name='Bottom five Rows')
  x=w 
  x.to_excel(writer,sheet_name='Two columns')

x = pd.read_excel('put.xlsx',sheet_name='First Five Rows')
#print(x)

x = pd.read_excel('put.xlsx',sheet_name='Bottom five Rows')
#print(x)

x = pd.read_excel('put.xlsx',sheet_name='Two columns')
#print(x)

x = pd.read_excel('put.xlsx',sheet_name=['First Five Rows','Bottom five Rows','Two columns'])  
print(x)

'''

'''import mod
print(mod.x)
'''

'''x = int(input('Enter a number: '))
y = []
z = 0
while z<x:
    s = eval(input('Enter any elements: '))
    y.append(s)
    z+=1
print(y)'''



'''W=pd.DataFrame(df1.groupby("brand").agg({"sales":"sum"}))
A=list(W.index)
B=list(W.values)
W'''

'''x = pd.DataFrame({'Mathmetics':[98,78,95],'Science':[99,98,79]})
#print(x)
y = pd.DataFrame({'Mathmetics':[100],'Science':[88]})
#print(y)
#a=pd.concat([x,y])
#print(a)
#a= x.append(y)
#print(a)

#How can we add a row on specific column:

x = pd.DataFrame({'Mathmetics':[98,78,95],'Science':[99,98,79]},index =['Riya','Jahanvi','Aliya'])
#print(x)
y = pd.DataFrame({'Mathmetics':[100],'Science':[88]}, index = ['kajal'])
#print(y)'''

#import pandas as pd

'''x = pd.DataFrame()
x.to_excel('U9.xlsx')

with pd.ExcelWriter('U9.xlsx')as writer:
  x = pd.DataFrame({"Name":["Kajal","Koyal","Kiran"], "Marks": [78,67,92]}, index = [1,2,3])
  x.to_excel(writer,sheet_name='Sheet1')
  x = pd.DataFrame({"Fruits":["Apple","Mango","Banana"], "Cost": [89,67,23]}, index = ["a","b","c"])
  x.to_excel(writer,sheet_name='Sheet2')
  x = pd.DataFrame({"Vegetables":["Potato","Tomato","Peas"], "Cost": [34,56,78]}, index = ["A","B","C"])
  x.to_excel(writer,sheet_name='Sheet3')
'''







#x.iloc[0,1] = 900 # You can change in ur existing sheet like this.






#HOW CAN I READ EXCEL SHEET ONE BY ONE, AND HOW CAN I READ ALL EXCEL SHEETS TOGETHER.

'''x = pd.read_csv('iris.csv')
#print(x)
z=x.head()
y=x.tail()
w=x.iloc[1:30,2:4]
x.to_excel('output.xlsx')
with pd.ExcelWriter('output.xlsx')as writer:
  x=z
  x.to_excel(writer,sheet_name='First Five Rows')
  x=y 
  x.to_excel(writer,sheet_name='Bottom five Rows')
  x=w 
  x.to_excel(writer,sheet_name='Two columns')

x = pd.read_excel('output.xlsx',sheet_name='First Five Rows')
#print(x)

x = pd.read_excel('output.xlsx',sheet_name='Bottom five Rows')
#print(x)

x = pd.read_excel('output.xlsx',sheet_name='Two columns')
#print(x)

#Now I will read all sheets together

x = pd.read_excel('output.xlsx',sheet_name=['First Five Rows','Bottom five Rows','Two columns'])  
print(x)

x = pd.DataFrame({'Name': ["Akash","Bhanu","Rahul","Akash","Bhanu","Rahul","Akash","Bhanu","Rahul",],'Subjects':['Python','Maths','Science','Python','Maths','Science''Python','Maths','Science'],'Marks' :[65,79,89,78,89,100,39,44,58],})
#print(x)



Create a file with ExcelWriter and make some programs on sheets, on first sheet perform description of data 
set, on second sheet perform value count of data set, on third sheet print any 40 rows and three column from the 
mid of the data set. on fourth make Groupby of this data set and perform the mean, sum, median, count, value_count
of this data set. After this read this data set one by one. Read all sheets together. 
'''


df = pd.read_csv('C:/Users/shpoo/Desktop/Data_set_for_ML/missing.csv')
#print(df)
#print(df.shape)

# All NaN row will be remove, but with this important records also remove.

a = df.dropna() 
#print(a)
#print(a.shape)

# Use of fillna() with the help of fillna we can fill 0 in each and every row where NaN is filled

a = df.fillna(0)
#print(a)

# There is a categorical column so there is no meaning of 5 here.
a = df.fillna(5)
#print(a)

# we can fiil this NaN value with this previous value

# Fill the NaN value with the previous value with this method argument.

a = df.fillna(method = "pad")
#print(a)

# If I want to fill this missing value with the next value

a = df.fillna(method = 'bfill')
#print(a)

# Now fill this NaN value column wise

a = df.fillna(method = 'pad',axis = 1)
#print(df)
#print(a)

# Now fill this NaN value column wise.

a = df.fillna(method = 'bfill', axis = 1)
#print(a)

a = df.fillna(method = 'pad', axis = 0)
#print(a)
#print(df)

# If I want to fill different values in replace of NaN value in multiple column together. 


a = df.fillna({'Age': 1000,
  'Country': 'Japan'})

#print(a)

a = df.fillna({'Age': 1000,
  'Country': 'Japan','Salary': 30000.00})

#print(a)

# If I want to fill the missing value with the mean value in a specific columns

a = df['Age'].mean()
#print(a)

a = df.fillna(df['Age'].mean())
#print(a)

a = df.fillna(df['Age'].min())
#print(a)

a = df.fillna(df['Age'].max())
#print(a)

a = df.fillna(df['Age'].median())
#print(a)

a = df.fillna(df['Age'].sum())
#print(a)


# This any argument will remove the all row if in a single cell there is mentioned NaN value.
a = df.dropna(how = 'any')
#print(a)


# This all argument will remove row, if in any row and all columns has NaN value.

a = df.dropna(how = 'all')
#print(a)

a = df.interpolate(method = 'pad')
#print(a)


from datetime import datetime


# It will show you present time datetime.
t1 = datetime.now()
#print(t1)

t2 = datetime(2000,1,1)
#print(t2)
diff = t1 - t2
#print(diff)
#print(type(diff))

x = pd.read_csv('C:/Users/shpoo/Desktop/Data_set_for_ML/AAPL.csv')
#print(x.head())
#print(type(x.Date[0]))

x = pd.read_csv('C:/Users/shpoo/Desktop/Data_set_for_ML/AAPL.csv', parse_dates = ['Date'])
#print(x.head())

#print(type(x.Date[0]))

# If I want to make my date column to be index.

x = pd.read_csv('C:/Users/shpoo/Desktop/Data_set_for_ML/AAPL.csv', parse_dates = ['Date'], index_col = 'Date')
#print(x)

# Now I want to check the index of this data set

#print(x.index)

# Why we make this datetime column to index, what will be the beneficial, with the help of this
# we can find specific month data. for example:

#print(x['2022-01'])
#print(x['2023-01'])

# You can find the Average price of apple's stock in jan, 2022

#print(x['2022-01'].Close

# You can find the mean on that

#print(x['2022-01'].Close.mean())

# You can retrive the price of day wise also

#ex: Date wise

#print(x['2022-01-03'])

# You can give the range of dates also. # You can get the data of one week.
#print(x['2022-01-01':'2022-01-07'])

# You can use resample here also with the resample you can find more clearity in the frequency in 
# specific date, day, and time.

#print(x.Close.resample('M').mean())

# We can find the monthly frequency

#print(x.Close.resample('M').mean())

# We can find the weekley frequency

#print(x.Close.resample('W').mean())

# We can find quartely frequency

#print(x.Close.resample('Q').mean())

# We can plot a chart here also

#%matplotlib inline
#print(x.Close.resample('M').mean().plot())

# You can also create a bar chart also


#%matplotlib inline
#print(x.Close.resample('Q').mean().plot(kind = 'bar'))



'''x = []
y = int(input('Enter any number: '))
z = 0 
while z<y:
  s = eval(input('Enter any element: '))
  x.append(s)
  z+=1
print(x)'''


'''x = ()
e = list(x)
y = int(input('Enter number: '))
z = 0 
while z<y:
  s = eval(input('Enter any number: '))
  e.append(s)
  z+=1
#print(e)
x = tuple(e)
print(x)'''


'''x = {}
y = list(x)
e = int(input('Enter number: '))
z = 0 
while z<e:
  s = eval(input('Enter any number: '))
  y.append(s)
  z+=1
x =set(y)
print(x)'''


x = {}
e = int(input('Enter number: '))
z = 0 
while z<e:
  s = eval(input('Enter key names: '))
  d = eval(input('Enter values: '))
  x[s]=d
  z+=1
print(x)





#print(y)
#x=dict(y)
#print(x)
