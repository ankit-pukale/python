# name1=input("Enter Name of Player:")
# score1=input("Enter score of Player 1:")
# name2=input("Enter Name of Player:")
# score2=input("Enter score of Player 2:")
# if score1>score2:
#     print(name1,"is winner")
# else:
#     print(name2,"is winner")


# #give geometrical shape is square or rectangle
# leng1= input("enter Length:")
# brdth1= input("enter Breadth:")
# if leng1==brdth1:
#     print("Giver Figure is a Square")
# else:
#     print("Given Figure is a Rectangle")

# print("**********if else**********")
#guess the Number
ans=7
guess_num=int(input("Enter your Guess:"))
if guess_num >ans :
    print("Number Entered is greater than answer")
    guess_num=int(input("Enter your Guess:"))
    if guess_num==ans:    #giving second condition to user(Nested if else)
        print("Your guess is correct")
    else:
        print("YOur Guess is incorrect")
elif guess_num <ans:
    print("Number Entered is smaller than answer")
    guess_num=int(input("Enter your Guess:"))
    if guess_num==ans:    #giving second condition to user(Nested if else)
        print("Your guess is correct")
    else:
        print("YOur Guess is incorrect")
else:
    print("Entered Number is Equal to answer")


# below code contain error
ans=8
guess_num=int(input("Enter your Guess:"))
for i in range(1,2):
    if i<2:        
        if guess_num>ans:        
            print(" Guess a lower num")     
            if i<2:guess_num=int(input("Enter your Guess:"))
        elif guess_num<ans:
            print(" Guess a Higher num") 
            if i<2:guess_num=int(input("Enter your Guess:"))                       
        else:
            print("You Guessed it correct")
            break
    else:
        print("No chance left")
    