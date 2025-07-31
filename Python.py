#Beginers

import random

print ('hello world') #-->>>>hello world

x = 6
print(x)#-->>>>6

y = 15.678
print (y)#-->>>>15.678

##############################################################################################################

z = "mohammad"
print(type(z))#-->>>><class 'str'>

x1 = 10
x2 = 20

a , b , c = "red" , "green" , 'blue'
print (a,b,c)#-->>>>red green blue

a = b = c = 'orange'
print (a,b,c)#-->>>>orange orange orange
 
color = ['red' , 'blue' , 'green']
a , b , c = color
print (a,b,c)#-->>>>red green blue

##############################################################################################################

var = 'micro'
print (var + 'learn')#-->>>>microlearn

x3 = 'hello '
x4 = 'world'
print(x3 + x4)#-->>>>hello world

print (144+156)#-->>>>300

##############################################################################################################

x5 = 'hello' # this is global

def myFunct():
    x5 = 'hi' # this is local
    print(x5 + ' world')#-->>>>hi world

myFunct()

print(x5 + ' world')#-->>>>hello world

##############################################################################################################

x6 = 123
x7 = 123.054
x8 = 17j
print(type(x6))#-->>>><class 'int'>
print(type(x7))#-->>>><class 'float'>
print(type(x8))#-->>>><class 'complex'>

x9 = 9e11
print(x9) #Scientific representation of numbers 9 * 10 ^ 11 #-->>>>900000000000.0

##############################################################################################################

x10 = 45
x11 = 15.26
x12 = float (x10)
print(x12)#-->>>>45.0

print (type(x12))#we can conversion int to complex and float to int and float to complex #-->>>><class 'float'>

# we cant conversion complex to int or float
# Part 10 Random numbers 40:02 _ 42:14
# we should add module to this python(import random in head we codes)

print(random.randrange(20,30))#-->>>>29

##############################################################################################################

x13 = int (1)
x14 = int(4023.245)
x15 = int("123")
print(x13 ,x14 , x15 )#-->>>>1 4023 123

x16 = float (1)
x17 = float(4023.245)
x18 = float("123")

print(x16 ,x17 , x18 )#-->>>>1.0 4023.245 123.0
x19 = str(1)
x20 = str(4023.245)
x21 = str("123")
print(x19 ,x20 , x21 )#-->>>>1 4023.245 123

##############################################################################################################

print(12 > 14)#-->>>>False
print(5<6)#-->>>>true
x22 = 12
x23 = 56

##############################################################################################################

#Additional Tips For Beginers And Operators

x22 = 12
x23 = 56

if x22 > x23 :
    print('12 is greater than 56')
else:
    print('56 is greater than 12')

#-->>>>56 is greater than 12

##############################################################################################################

# Boolean function 

print(bool(15)) #-->>>>True
print(bool(0))#-->>>>False

x24 = 'hello'
print (bool(x24))#-->>>>True
print (bool(None))#-->>>>False

def myFunct2():
    return True
if myFunct2():
    print('its true')
else:
    print('its false')

#-->>>>its true


##############################################################################################################

#Operators 

#1-Computational operators

x25 = 25
print (x25 / 13)#-->>>>1.9230769230769231
print (x25 // 13)#-->>>>1
print (x25 ** 13)#-->>>>1490116119384765625

##############################################################################################################

#2-assignment operator

x25 += 2 # == x25 = x25 + 2
x26=50
x26+=1 
print(x26)#-->>>>51
##############################################################################################################

#3-Comparison operators

x27 = 45
print(x27 == 50)#-->>>>False
print(x27 != 50)#-->>>>True

##############################################################################################################

#4-Logical operators and or not

print (13 < 15 or 13 > 11)#-->>>>True
print (13 < 15 and 13 > 11)#-->>>>True
print (not (13 > 11))#-->>>>False

##############################################################################################################

#5-Identity operators

fruits = [ 'apple' , 'banana']

frt = [ 'apple' , 'banana']

list1= fruits

print(fruits is frt)#-->>>>False
print(fruits == frt)#-->>>>True
print(fruits is list1)#-->>>>True
print(fruits is not list1)#-->>>>False
print(fruits == list1)#-->>>>True

##############################################################################################################

#6-Membership operators

string = 'microlearn'
print('M' in string)#-->>>>False
print('M' not in string)#-->>>>True

##############################################################################################################

#7-Bitwise operators # | ^ ~ << >> are 0 , 1
x28 = 0b10110
x29 = 0b10101
print(bin(x28 | x29))#-->>>>0b10111
print(bin(x28 & x29))#-->>>>0b10100
print(bin(x28 ^ x29))#-->>>>0b11
print(bin(x28 >> x29))#-->>>>0b0

##############################################################################################################

#Input

x30 = input ("enter a number : ")#12 <<<<--
print ("enterd number is : ",x30)#-->>>> 12

##############################################################################################################

#String

x31 = '''
#this is python
#this is python
#this is python
#this is python
#this is python
'''

print(x31)#-->>>> 
#this is python
#this is python
#this is python
#this is python
#this is python

str1 = "mohamad"

print(str1[5])#-->>>>a

for x32 in str1:
    print(x32)#-->>>>mohamad
print(len(str1))#-->>>>7

l = len(str1)

print(str1[l-1])#-->>>>d
print(str1[1:3])#-->>>>oh
print(str1[-4:-2])#-->>>>am

##############################################################################################################

#List

list2 = [1 , 2 , 'hello' , ['3', "5"]]
print(list2)#-->>>>[1, 2, 'hello', ['3', '5']]

list2[2] ="mohammad"
print(list2)#-->>>>[1, 2, 'mohammad', ['3', '5']]
print(len(list2))#-->>>>4

list3=list((1,2,"a"))
print (list3)#-->>>>[1, 2, 'a']

list2[3][1] = 33
print(list2)#-->>>>[1, 2, 'mohammad', ['3', 33]]

list2.insert(2,"micro")
print(list2)#-->>>>[1, 2, 'micro', 'mohammad', ['3', 33]]

list2.append("world")
print(list2)#-->>>>[1, 2, 'micro', 'mohammad', ['3', 33], 'world']

##############################################################################################################

list4 = [100,4001,23]
list2.extend(list4)
print(list2)#-->>>>[1, 2, 'micro', 'mohammad', ['3', 33], 'world', 100, 4001, 23]

list2.remove(1)
print(list2)#-->>>>[2, 'micro', 'mohammad', ['3', 33], 'world', 100, 4001, 23]

list2.pop()
print(list2)#-->>>>[2, 'micro', 'mohammad', ['3', 33], 'world', 100, 4001]

del list2[2]
print(list2)#-->>>>[2, 'micro', ['3', 33], 'world', 100, 4001]

list2.clear()
print(list2)#-->>>>[]

list5=[15,4,34,7]
list5.sort()
print(list5)#-->>>>[4, 7, 15, 34]

list5.sort(reverse=True)
print(list5)#-->>>>[34, 15, 7, 4]

##############################################################################################################

#sort use for alphabet.

def myFunct(n):
    return abs(n - 10)

list6=[56,54,21,87,49,34]
list6.sort(key = myFunct)
print(list6)#-->>>>[21, 34, 49, 54, 56, 87]

def myFunct3(n):
    return abs(n - 10)

list7=['Z','v','h','G','M','a']
list7.sort(key = str.lower)
print(list7)#-->>>>['a', 'G', 'h', 'M', 'v', 'Z']

##############################################################################################################

list8 = [1,2,3,4]
list9=list8.copy() #====== list9 = list(list8)
print(list9)#-->>>>[1, 2, 3, 4]

list8[2] = 10
print(list9)#-->>>>[1, 2, 3, 4]

myList = ['11111','34',"25" , '987']
newList = [item for item in myList if '1' in item]
print(newList)#-->>>>['1111']

##############################################################################################################

#Tuple

#Tuple is unchangable

myTuple = (100 , 'apple', True,123)
myTuple2=(1)
myTuple3=(1,)

print(type(myTuple2))#-->>>><class 'int'>
print(type(myTuple3))#-->>>><class 'tuple'>

mylist2 = list(myTuple)
mylist2[0] = 500
myTuple = tuple(mylist2)
print(myTuple)#-->>>>(500, 'apple', True, 123)

(*a,b,c) = myTuple
print(a,b,c)#-->>>>[500, 'apple'] True 123

##############################################################################################################

#Sets

set1={1,2,'a',True}
print(set1)#unavailable to sets wwith index because sets hasn't index #-->>>>{1, 'a', 2}

set2={1,21,1,1,1,1,3}
print(set2)#-->>>>{1, 3, 21}
print(type(set2))#-->>>><class 'set'>

set2.add(128)
print(set2) # in sets haven't sort #-->>>>{128, 1, 3, 21}

set2.remove(128)
print(set2)#-->>>>{1, 3, 21}

set3 = set1.union(set2)
print(set3)#-->>>>{1, 2, 3, 21, 'a'}

set1.intersection_update(set2)
print(set1)#-->>>>{1}

set1.symmetric_difference_update(set2)
print(set1)#-->>>>{3, 21}

##############################################################################################################


