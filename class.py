#helping A traveler
hungry=input("are you hungry y/n:")
thirsty=input("are you thirsty y/n:")
travelling=input("are you travelling y/n:")
no_money=input("are you having money y/n:")
if hungry=='y' or thirsty=='y' and travelling=='y' and no_money=='y':
    print('we will help you')
else:
    print('you dont need out help') 
#yyyn -->we will help you
if (hungry=='y' or thirsty=='y' )and (travelling=='y' and no_money=='y'):
    print('we will help you')
else:
    print('you dont need out help') 
    #y y y n -->you dont need out help