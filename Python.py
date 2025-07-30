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
