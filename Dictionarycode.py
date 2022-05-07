print('**********dictionary**********')
#after python 3.7 its states that dictonary order make matter
#creating dictionary
#check for duplicate value ---> this will return final updated value in below example value of 5 is five++ 
pair1={
    1:'one',
    2:'two',
    5:'five+',
    3:'three',
    4:'four',
    5:'five',
     5:'five++'
}
print(pair1) #{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
print('**********Retrive**********')
pair1={
    'first':'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five'
}
print(pair1['first'])#one
# b=pair1[6]
# print(b) #KeyError: 6   beacause key not exist 
print('**********get method to retrive Retrive**********')
#get get method is slow it will return none if value not exist i.e code will not crash
a=pair1.get(5)
print(a)#five
a=pair1.get(6)
print(a)#none

print('**********add /create**********')
pair1[6]='six'
print(pair1) #{'first': 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}
pair1[7]='seven'
print(pair1)#{'first': 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven'}

print('**********update**********')
pair1[7]='seven+' #this is fast
print(pair1)#{'first': 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven+'}
print('**********update method**********')
#this method add /update dictionary
pair1.update({8:'seven-'})
print(pair1)
print('**********delete**********')
del pair1[7]
print(pair1)#{'first': 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}
#if we delete same key agan it will produce error
pair1.pop(6)
print(pair1)#{'first': 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
print(pair1.pop(6,'a')) # this will give output == a
print('**********printing only kets**********')
print(pair1.keys())#dict_keys(['first', 2, 3, 4, 5, 8])
print(type(pair1.keys())) #<class 'dict_keys'>
print('**********printing only values**********')
print(pair1.values())#dict_values(['one', 'two', 'three', 'four', 'five', 'seven-'])
print(type(pair1.values())) #<class 'dict_values'>

print('**********printing item**********')
#print items of dictionary i.e key value pair
print(pair1.items())#dict_items([('first', 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'), (8, 'seven-')])
print(type(pair1.items()))#<class 'dict_items'>

print('**********fromkeys**********')
pair2 = dict.fromkeys(pair1.keys(),pair1.values())
print(pair2)#{'first': 'values12', 2: 'values12', 3: 'values12', 4: 'values12', 5: 'values12', 8: 'values12'}
print('**********copy **********')
#note pair1=pair3 use same memory i.e if we change pair1 then pair3 also get changed automatically
pair3=pair1.copy()
print(pair3)
del pair1[8]
print(pair3)