print("**************for loop *******************")
#for loop                                
#table of 8
for i in range (1,11):
    print("The table of 8 * " ,  i," is :", i*8) #indentation space in front of print
    print("*********************************")   

print("**************if else*******************")
#if else
#checking if the citizen is eligible to vote: age 18+
name=input("Enter Your Name:")
age=int(input("Enter your age:"))
if age>18:
    print("Mr.",name," your eligible for voting")
    print("use your voting rights carefully")
else:
    print("Mr.",name,"your age is less than 18")
    print("your not eligible for voting")
    
