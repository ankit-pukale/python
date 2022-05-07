#for loop can be applied on sequence only
name1='minskole'
for i in name1:
    print(i)   # m i n s k o l e

print('********print capital letter from string***********')
name1='MinsKole'
capitalletter=""
for i in name1:
    if i.isupper():
        capitalletter=capitalletter+i
        # print(i)

print(capitalletter)

print('********print only numbers from string***********')
name1='MinsKole1234'
capitalletter=""
for i in name1:
    if i.isnumeric():
        capitalletter=capitalletter+i
        # print(i)

print(capitalletter)

