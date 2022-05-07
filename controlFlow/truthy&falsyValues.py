'''falsy values
The number zero (0)
An empty string ''
False
None
An empty list []
An empty tuple ()
An empty dictionary {}'''
from cmath import nan


if 1:
    print("true") #true
else:
    print("false")

if 0:
    print("true")
else:
    print("false") #false
if "":
    print("true")
else:
    print("false") #false
if None:
    print("true") 
else:
    print("false")#false

if []:
    print("true") 
else:
    print("false")#false
if {}:
    print("true") 
else:
    print("false")#false

if []:
    print("true") 
else:
    print("false")#false

if -1:
    print("true") #true
else:
    print("false")

if 0.1:
    print("true") #true
else:
    print("false")

if '0':
    print("true") #true
else:
    print("false")

if None:
    print("true") 
else:
    print("false")#false

if nan:
    print("true") #true
else:
    print("false")


print('****Membership conditions*******')
even1=(1,2,3,4,5,6,7,8)
if 8 in even1:
    print('present')#present
else:
    print('absent')

if 13 not in even1:
    print('present')#present
else:
    print('absent')

name1='Minskole'
if 'M' in even1:
    print('present')#present
else:
    print('absent')