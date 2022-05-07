#TUPLES =>tuples are immutable
#how to create a tuple
secret_recipe1=('step1','step2','step3','step4','step5')
print(secret_recipe1)#('step1', 'step2', 'step3', 'step4', 'step5')
print(type(secret_recipe1)) #<class 'tuple'>
#check the characteristics for single element/item and blank/none
secret_recipe3=('step1')
print(type(secret_recipe3)) #<class 'str'>

secret_recipe3=('step1',)#after adding comma this will be tuple ()
print(type(secret_recipe3)) #<class 'tuple'>

print('*******reading value by index**********')
#reading value by index
print(secret_recipe1[1]) #step2
print(secret_recipe1[0:2])#('step1', 'step2')

print('*******check if tule is mutable or not**********')
#secret_recipe1[2]='step7' #display this error : secret_recipe1[2]='step7'TypeError: 'tuple' object does not support item assignment
#print(secret_recipe1.replace('step1','step7')) #ttributeError: 'tuple' object has no attribute 'replace'

'''tuple methods()'''
print('*******count()**********')
#count  tuple.count('value)
print(secret_recipe1.count('step1')) #1
print('*******index()**********')
#index  tuple.index('value') => return index of value
print(secret_recipe1.index('step5')) #4
