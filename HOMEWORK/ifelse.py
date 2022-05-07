ans=9
guess_num=int(input("Enter your Guess:"))
if guess_num!=ans:
    if guess_num < ans:
        print(" Guess a higher num")
    else:
        print(" Guess a lower num")
    guess_num = int(input())
    if guess_num == ans:
        print("You are correct")
    else:
        print("You are wrong ")            
else:
    print("You Guessed it correct")




     
    