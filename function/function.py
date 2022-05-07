'''types
1.inbuilt function
2.User defined function  ->can be user to overcome inbuilt function
defination means defining function
1.defination cann ot start with special character 
2.function can not start with special keywords like print
*) a function bound to an instance of class is called as method 
'''
#function without paramenter and with return type
print("function without parameter without return type")
def mult():
    a=7*5
    return a   #if we dont return and print this will gives output None

answer =mult()
print(answer) #35

print("function with parameter without return type")

def multiply(x,y):
    print(x*y) #10

multiply(5,2)#poistion of argument is important

def add():
    return 10

#palindrome
name1=input("Enter your name to check :")
name2=name1[::-1]
if name2==name1:
    print("Given string is palindrome")
else:
    print("given string is not palindrome")

#check palindrome string using function 

print("****check string is palindrome or not with function****")
#creating user defined string and comparing
def is_palindrome(string1):
   name2=string1[::-1]
   print("backword")
   return name2==string1

word=input("Enter your name to check :")
if is_palindrome(word.casefold()):
       print("Given string is palindrome")
else:
    print("given string is not palindrome")




