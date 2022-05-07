# using while loop while number of attempts are unknown
'''note membership operator = 1.)in   2.)not in '''
#exiting a location with four directions,but dont know how many times user will guess
#using break in the code
#using else in the code 

availavle_exits=['n','s','e','w']
chosen_exit=""
while chosen_exit not in availavle_exits:    
    chosen_exit=input("Enter exit point:").casefold()
    if chosen_exit=="quit":
        print("Game over")
        break
else:          #Note we can use else with while in python 
    print("Your successfully escaped ")
