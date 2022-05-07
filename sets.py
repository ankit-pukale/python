#set  
'''*set is unordered dont have indexing
*sets are mutable
*sets does not allow duplicates 
* sets used for comparison'''
#how to create Set {values,values}
even1={2,4,6,8}
odd1={1,3,5,9}
#length
print(len(even1))#4
print(even1)#{8, 2, 4, 6} out put will not be in sequence of input 
print(odd1)#{1, 3, 5, 9}
odd1={3}
print(type(odd1)) #<class 'set'>   Note if we print type of empty set then op is dictonary

print('*********************')
#duplicate values not allowed in set
even1={2,4,6,8,2,12,14,16,8}
print(even1) #{16, 2, 4, 6, 8, 12, 14}
print(len(even1))#7

even1={2,4,6,8}
'''Sets Methods'''
print('********ADD*************')
# add  set.add(value)
even1.add(10)
print(even1) #{2, 4, 6, 8, 10}

print('********update*************')
#update used to merge set
#update ==> change orginal set i.e even1 is updated so we printed even1 and this will not allow duplicate values
even1.update(odd1)
print(even1) #{2, 3, 4, 6, 8, 10}

print('********remove*************')
#remove =>remove(value)
even1={2,4,6,8}
even1.remove(8)
print(even1)#even1={2,4,6,8} if we remove same element again then it will show error

#remove method shows error if element is not present discard method will not give any error if element is absent
even1.discard(8) # 8 is not present in set but this method does not show any error

print('********pop*************')
#pop will kick out first element from set
even1={2,4,6,8}
even1.pop()  #note pop()will not accept argument
print(even1) #{2, 4, 6}
#if we remove all element from set it will return empty set() and if we pop empty set it will show error
# home work::check the details of elements removing by pop method
print('********clear*************')
#clear will clear set 
even1.clear()
print(even1) #output=set() 
