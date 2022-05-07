num1=int(input("Enter Number Greater than 10:"))
print(num1%2==0 or num1%3==0 or num1%5==0 or num1%7==0)
r=num1%2 #Number is divisible by 2
s=num1%3 #Number is divisible by 3
t=num1%5 #Number is divisible by 5
u=num1%7 #Number is divisible by 7
print(r,":Checking The divisibility by 2")
print(s,":Checking The divisibility by 3")
print(t,":Checking The divisibility by 5")
print(u,":Checking The divisibility by 7")
print(r==0 or s==0 or t==0 or u==0 )