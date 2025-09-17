import Training2 as TR
TR.Mymodul("mohammad")

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

#Dictionary

myCar = {
    'name' : 'samand',
    'color' : 'white' ,
    'year' : 1400
    #key : value
}
print(myCar)#-->>>>{'name': 'samand', 'color': 'white', 'year': 1400}

myCar ['year'] = 1399
print(myCar)#-->>>>{'name': 'samand', 'color': 'white', 'year': 1399}

myCar.update({'company' : 'ir'})
print(myCar)#-->>>>{'name': 'samand', 'color': 'white', 'year': 1399, 'company': 'ir'}

#dictionary is structure in other language

myStudents = {
    'student1' : {
        'name' : 'mohammad' ,
        'id' : 1025
    },
    'student2': {
        'name' : 'kourosh' ,
        'id' : 1120
    }
}
print(myStudents)#-->>>>{'student1': {'name': 'mohammad', 'id': 1025}, 'student2': {'name': 'kourosh', 'id': 1120}}

##############################################################################################################

#Condition

x33=65
x34=65

if x33 > x34:
    print("x33 greater")
elif x34 > x33:
    print("x34 greater")
else:
    print("x34 == x33")

#-->>>>x34 == x33

print('a > b') if x33 > x34 else print('a <= b')#-->>>>a <= b

##############################################################################################################

#Loops

i = 1

while i < 8 :
    print(i)#-->>>>1 2 3 4 5
    if i == 5:
        break
    i+= 1

i = 1

while i < 5 :
    i += 1
    if i == 3:
        continue
    print(i)#-->>>>2 4 5

string1 = 'microlearn'

for char in string1 :
    print(char)#-->>>>m i  c r o l e a r n

for i in range(1,120,40):
    print(i)#-->>>>1 41 81

##############################################################################################################

#Function

def name():
    print('hi every one')
name()#-->>>>hi every one

def mean(score1,score2):
    return (score1+score2) / 2
print(mean(12,45))#-->>>>28.5

def power(x,n):
    result = 1 
    for item in range(n) :
        result *= x
    return result
print(power(2,10))#-->>>>1024

def power_recursion(x,n):
    if n > 0:
        result = x * power_recursion(x,n-1)
        return result
    elif n == 0 :
        return 1
print(power_recursion(2,10))#-->>>>1024

##############################################################################################################

#Advanced Python

#we can use mysql with pyton for database

#Generator

def firstn():# yeild like return
    yield 1
    yield 2
    yield 3

for i in firstn():
    print(i) #-->>>> 1 2 3 

#yeild  returns our outputs one by one, unlike return in function.
# means yeild return us : 1 and go to the for loop and 2 go to the for loop and 3 go to the for loop.

#tips for debuging python in vs code : next or near of number line , you click and see red cicrle , and clicl F5 and line to line click F11 for debuging

#Lambda

x35 = lambda x:x + 5
print(x35(4))#-->>>> 9
lists = [2,4,6]
def myfunc (n):
    return n * 2

#Map

newList2 = map(lambda x : x * 2,lists)
print(list(newList2))#-->>>>[4, 8, 12]

newList3 = filter(lambda x: True if x > 3 else False , lists)
print(list(newList3))#-->>>>[4, 6]

##############################################################################################################

#Oop

class myclass:
    x =13 
myObject = myclass()
print(myObject.x)#-->>>>13
class circle :
    def readRadius (self):#self is a variable
        self.radius = int(input("Enter radius : "))#  12<<----
    def calculate(self):
        self.area = 3.14 * self.radius ** 2
    def display(self):
        print('Radius : ' , self.radius , 'Area' , self.area)#-->>>>Radius :  58 Area 10562.960000000001
myCircle = circle()
myCircle.readRadius()
myCircle.calculate()
myCircle.display()

class rectangle :
    def __init__(self,l,w):#init==initialization
        self.length =1 
        self.width = 2
    def calculatering(self):
        self.area=self.length*self.width
    def display(self):
        print('Area: ',self.area)#-->>>2
rect = rectangle(12,7) # for init
rect.calculatering()
rect.display()

#inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return "Generic animal sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof woof!"
    
    def chase_tail(self):
        return f"{self.name} is chasing its tail!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
    def scratch_furniture(self):
        return f"{self.name} is scratching the furniture!"

dog1 = Dog("Rex")
cat1 = Cat("Whiskers")

print(dog1.make_sound())#-->>>>Woof woof!
print(dog1.chase_tail())#-->>>>Rex is chasing its tail!

print(cat1.make_sound())#-->>>>Meow!
print(cat1.scratch_furniture())#-->>>>Whiskers is scratching the furniture!

#IOT = Internet Object Or Internet Things

##############################################################################################################

#Modul

#we can create a new file by name is  : Training2 and save codes of about this moduls
#from use element special in moduls we must :

#from Training2 import variable_name

#we can use moduls standards in python :
import sys
sys.path.append(r'address : c:/users/ea/da/da/')

#from Training2 import * : means import all elements 

##############################################################################################################

#File

file = open('readme.txt') #or file = open ('address : c:/users/ea/da/da/')
#file = open('address.txt' , 'r') , r means just read
#file = open('address.txt' , 'a') , a means append and push in end codes 
#file = open('address1.txt' , 'a' or 'w' or 'x') , address1.text isn't file and this commond means create address1.text and w means write
#file = open('address.txt' , 'xt' or 'xb') , t means text and b means binary

print (file.read())#print (file.read(10)) means 10 first char just read 
#for item in file.read():{print(item)} is Read it one by one char
#for item in file.readline():{print(item)} is read first line one by one char
# if again this : for item in file.readline():{print(item)}  is read seccond line one by one char
#file.close() : for memory
#file.write('this is new text') # push in end of readme.txt #file = open('address1.txt' ,'w') # delete data and write this is new text
file = open('readme.txt')
print (file.read())

import os
#os.rename("readme.txt" , "readme2.txt") # change name file
#os.remove("readme.txt") # remove file

import pandas as pd#Main use: Managing and processing structured data (such as tables) or chart data
import numpy as np#Main use: Numerical calculations and working with multidimensional arrays
import matplotlib.pyplot as plt#Main use: drawing diagrams and images
from sklearn.impute import SimpleImputer#Main use: replacing missing values (not used in this code but commonly used for this purpose)

# Create a sample dataset with missing values

data = {
    'Age': [25, 30, np.nan, 35, 40, np.nan, 45, 50, 55, np.nan],
    'Income': [50000, np.nan, 70000, np.nan, 90000, 100000, 110000, np.nan, 130000, 140000],
    'Score': [3.5, 4.0, np.nan, 4.5, np.nan, 5.0, 5.5, 6.0, np.nan, 6.5]
}
#or your use exel : excel_path = "address:C:/User/.../.../abc.xlsx"
#df = pd.read_excel(excel_path)
df = pd.DataFrame(data)

print("Original dataset with missing values:")
print(df)

#-->>>>Original dataset with missing values:
#    Age    Income  Score
#0  25.0   50000.0    3.5
#1  30.0       NaN    4.0
#2   NaN   70000.0    NaN
#3  35.0       NaN    4.5
#4  40.0   90000.0    NaN
#5   NaN  100000.0    5.0
#6  45.0  110000.0    5.5
#7  50.0       NaN    6.0
#8  55.0  130000.0    NaN
#9   NaN  140000.0    6.5

# Calculate statistical measures before processing
print("\nStatistical measures before processing:")
print(df.describe())

#-->>>>Statistical measures before processing:
#             Age         Income     Score
#count   7.000000       7.000000  7.000000
#mean   40.000000   98571.428571  5.000000
#std    10.801234   31847.852585  1.080123
#min    25.000000   50000.000000  3.500000
#25%    32.500000   80000.000000  4.250000
#50%    40.000000  100000.000000  5.000000
#75%    47.500000  120000.000000  5.750000
#max    55.000000  140000.000000  6.500000

# Show count of missing values in each column
print("\nCount of missing values in each column:")
print(df.isnull().sum())

# Method 1: Dropping records with missing values
df_dropped = df.dropna()

# Calculate statistical measures after dropping records
print("\nStatistical measures after dropping records with missing values:")
print(df_dropped.describe())

#-->>>>Statistical measures after dropping records with missing values:
#             Age         Income     Score
#count   2.000000       2.000000  2.000000
#mean   35.000000   80000.000000  4.500000
#std    14.142136   42426.406871  1.414214
#min    25.000000   50000.000000  3.500000
#25%    30.000000   65000.000000  4.000000
#50%    35.000000   80000.000000  4.500000
#75%    40.000000   95000.000000  5.000000
#max    45.000000  110000.000000  5.500000

# Method 2: Filling missing values with different approaches
# a) Filling with mean
df_mean = df.fillna(df.mean())

# b) Filling with median
df_median = df.fillna(df.median())

# c) Filling with mode (not typically used for numerical data)

# d) Filling with random normal distribution (mean + std)
def fill_with_random_normal(series):
    mean = series.mean()
    std = series.std()
    null_indices = series.isnull()
    series.loc[null_indices] = np.random.normal(mean, std, size=null_indices.sum())
    return series

df_std = df.apply(fill_with_random_normal, axis=0)

# Display results from different filling methods
print("\nSample of mean imputation:")
print(df_mean.head())

#-->>>>Sample of mean imputation:
#    Age        Income  Score
#0  25.0  50000.000000    3.5
#1  30.0  98571.428571    4.0
#2  40.0  70000.000000    5.0
#3  35.0  98571.428571    4.5
#4  40.0  90000.000000    5.0

print("\nSample of median imputation:")
print(df_median.head())

#-->>>>Sample of median imputation:
#    Age    Income  Score
#0  25.0   50000.0    3.5
#1  30.0  100000.0    4.0
#2  40.0   70000.0    5.0
#3  35.0  100000.0    4.5
#4  40.0   90000.0    5.0

print("\nSample of normal distribution imputation:")
print(df_std.head())

#-->>>>Sample of normal distribution imputation:
#         Age        Income     Score
#0  25.000000  50000.000000  3.500000
#1  30.000000  81541.783304  4.000000
#2  39.976863  70000.000000  3.589551
#3  35.000000  82407.531279  4.500000
#4  40.000000  90000.000000  5.205863

# Calculate statistical measures for each imputation method
print("\nStatistical measures after mean imputation:")
print(df_mean.describe())

#-->>>>Statistical measures after mean imputation:
#             Age         Income      Score
#count  10.000000      10.000000  10.000000
#mean   40.000000   98571.428571   5.000000
#std     8.819171   26003.662746   0.881917
#min    25.000000   50000.000000   3.500000
#25%    36.250000   92142.857143   4.625000
#50%    40.000000   98571.428571   5.000000
#75%    43.750000  107500.000000   5.375000
#max    55.000000  140000.000000   6.500000

print("\nStatistical measures after median imputation:")
print(df_median.describe())

#-->>>>Statistical measures after median imputation:
#             Age         Income      Score
#count  10.000000      10.000000  10.000000
#mean   40.000000   99000.000000   5.000000
#std     8.819171   26012.817354   0.881917
#min    25.000000   50000.000000   3.500000
#25%    36.250000   92500.000000   4.625000
#50%    40.000000  100000.000000   5.000000
#75%    43.750000  107500.000000   5.375000
#max    55.000000  140000.000000   6.500000

print("\nStatistical measures after normal distribution imputation:")
print(df_std.describe())

#-->>>>Statistical measures after normal distribution imputation:
#             Age         Income      Score
#count  10.000000      10.000000  10.000000
#mean   41.636456   98599.220203   4.951886
#std     9.721002   29358.560203   1.029130
#min    25.000000   50000.000000   3.500000
#25%    36.244216   81758.220298   4.125000
#50%    41.779007   95000.000000   5.102931
#75%    48.750000  125000.000000   5.667586
#max    55.000000  140000.000000   6.500000

# Plotting to compare distributions before and after processing
plt.figure(figsize=(15, 10))

# Age distribution comparison
plt.subplot(2, 2, 1)
df['Age'].plot(kind='kde', label='Original', color='red')
df_mean['Age'].plot(kind='kde', label='Mean Imputation', color='blue')
df_median['Age'].plot(kind='kde', label='Median Imputation', color='green')
df_std['Age'].plot(kind='kde', label='Normal Dist Imputation', color='purple')
plt.title('Age Distribution Before/After Processing')
plt.legend()

# Income distribution comparison
plt.subplot(2, 2, 2)
df['Income'].plot(kind='kde', label='Original', color='red')
df_mean['Income'].plot(kind='kde', label='Mean Imputation', color='blue')
df_median['Income'].plot(kind='kde', label='Median Imputation', color='green')
df_std['Income'].plot(kind='kde', label='Normal Dist Imputation', color='purple')
plt.title('Income Distribution Before/After Processing')
plt.legend()

# Score distribution comparison
plt.subplot(2, 2, 3)
df['Score'].plot(kind='kde', label='Original', color='red')
df_mean['Score'].plot(kind='kde', label='Mean Imputation', color='blue')
df_median['Score'].plot(kind='kde', label='Median Imputation', color='green')
df_std['Score'].plot(kind='kde', label='Normal Dist Imputation', color='purple')
plt.title('Score Distribution Before/After Processing')
plt.legend()

plt.tight_layout()
plt.show()


#-->>>> The all codes with plt show the table

##############################################################################################################

#refrence :

#jadi mirmirani , maktabkhoneh , youtube ---- microlearn ehsan abdollahi

#Robot in telegram with microlearn ehsan andollahi