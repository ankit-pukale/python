from pickle import TRUE


lucky_no2=["sperman1","sperman2","sperman3"]
print("**************************")
#append() =>add element at end of list
lucky_no2.append('sperman4')
print(lucky_no2) #['sperman1', 'sperman2', 'sperman3', 'sperman4']
print("**************************")
#insert()=>insert at the given index position (dont replace existing item it shift one pos)
#syntax = list.insert(start el,value)
lucky_no2.insert(2,'Batman3')
print(lucky_no2) #['sperman1', 'sperman2', 'Batman3', 'sperman3', 'sperman4']
print("**************************")
#extend()
lucky_no2=["sperman1","sperman2","sperman3"]
lucky_no3=["Batman1","Batman2","Batman3"]
lucky_no2.extend(lucky_no3)
print(lucky_no2) #['sperman1', 'sperman2', 'sperman3', 'Batman1', 'Batman2', 'Batman3']
#this can aslo done as following way i.e concat
#concat
lucky_no2=["sperman1","sperman2","sperman3"]
lucky_no3=["Batman1","Batman2","Batman3"]
print(lucky_no2+lucky_no3)#['sperman1', 'sperman2', 'sperman3', 'Batman1', 'Batman2', 'Batman3']
print("**************************")

lucky_no1=[ 2,4,6,3,2,5,8,9]
#sort =>sort elemets of list
lucky_no1.sort()
print(lucky_no1)#[2, 2, 3, 4, 5, 6, 8, 9]
lucky_no1.sort(reverse=True)
print(lucky_no1)#[9, 8, 6, 5, 4, 3, 2, 2]
#copy
print("*********copy************")
luckycopy=lucky_no1.copy()
print(luckycopy)#[9, 8, 6, 5, 4, 3, 2, 2]
print("**********remove*************")
#remove remove particular element
luckycopy.remove(2)
luckycopy.remove(2)
print(luckycopy)#[9, 8, 6, 5, 4, 3] 2 removed
#pop =>remove last elemenet if parameter not provided 
print("***********pop**********")
luckycopy.pop()
print(luckycopy)#[9, 8, 6, 5, 4]
#if index provided remove element from that index
luckycopy.pop(0)
print(luckycopy)#[8, 6, 5, 4]
print("*********clear***********")
#clear =>clear list
luckycopy.clear()
print(luckycopy)#[]
