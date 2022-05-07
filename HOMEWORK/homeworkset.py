even1 = {2,4,6,8} 
even1.pop()
print(even1)#{2, 4, 6} 
even1.pop()
print(even1)#{4, 6}
even1.pop()
print(even1)#{6}
print('***On String***')
str={'a','b','c','d','e'}
str.pop()
print(str)#{'c', 'd', 'a', 'b'}
str.pop()
print(str)#{'d', 'a', 'b'}
str.pop()
print(str)#{'a', 'b'}
str.pop()
print(str)#{'b'}
str.pop()
print(str)#set()

print('***Set intersection***')#output=common parts
#Set intersection==>return common part of sets
month1={"jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"}
month31={'jan','mar','may','jul','aug','oct','dec'}
month_30={'apr','jan','sep','nov'}
month_28={'feb'}#only one element
i=month1.intersection(month_28)
print(i)#{'feb'}
b=month_30.intersection(month_28,month1)
print(b)#set()


print('***Symetric difference***')#output =uncommon parts
#Symetric difference   = return un common part of sets if no element is common it print all element
print(month_30.symmetric_difference(month_28))#{'jan', 'apr', 'sep', 'feb', 'nov'}
print(month1.symmetric_difference(month31))#{'sep', 'apr', 'feb', 'nov', 'jun'}




