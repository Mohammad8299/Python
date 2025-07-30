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
