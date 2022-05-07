#list s are N Number of Steps Seperated by Comma
lucky_no1=[0,1,2,3,4,5,6,7,8,9] #=>LIST
print(lucky_no1)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("**************************")
#len
print(len(lucky_no1))#10
print("**************************")
#access Value by Index
print(lucky_no1[7])#7
print("**************************")
#slice => Syntax: list[stratvalue:endvalue-1]
print(lucky_no1[2:5]) #[2, 3, 4]
print("**************************")
#UPDATING VALUE BY INDEX
lucky_no1[9]=11
print(lucky_no1) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 11]
print("**************************")
# updating value in range
lucky_no1[7:9]=[17,18,19]
print(lucky_no1) #[0, 1, 2, 3, 4, 5, 6, 17, 18, 11]