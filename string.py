# name1="Minskole"
# #String Stores value sequentially by index(Strings are immutable)
# print(name1[0])
# print(name1[1])
# #slicing : Printing value/characters in range
# aim="Complte Python in 3 month"
# print(aim[0:8]) #(Start value:end value -1)
# print(aim[6:10]) #e Py
# print(aim[:4]) #Comp (print value by default from 0 Comp)
# print(aim[4:]) #lte Python in 3 month(print value up to end)
# print(aim[:]) # print the whole sentence
# print(aim[5:1]) # reverse not allowed print blank string

# #Concat
# str1="Minskole"
# str2=" Pune"
# print(str1+str2) #Minskole Pune

# #repeat (string multiplication)
# str3="*"
# print(str3*5) # ***** (repeat * 5 times)

# #Home Work
str="Minskole"
print(str[-7:5])
print(str[6:-1])
print(str[-7:-5])
print(str[:])
print(str[5:])
print(str[-4:])
print(str[:-2])

#slicing with jump/skip value (skip-1 steps will be skipped)
print(str[0:5:6])
len =len(str)
print(str[0:len:3])




