# #using AND and OR in condition
# name_applicant=input("Please Enter your Name:")
# age_applicant=int(input("Please Enter your age:"))
# #here we will check the age condition
# if age_applicant<60 and age_applicant>21:
#     print("You can Become Uber Partner")
# else:
#     print("your ineligible for Become Partner")

#checking the Qualification and experience 
# name_applicant=input("Please Enter your Name:")
# age_applicant=int(input("Please Enter your age:"))
# qualif_applicant=input("Please Enter your Qualification Grad:")
# exp_applicant=int(input("Please Enter your Experience in years:"))
# if qualif_applicant=='Grad' or exp_applicant>=2:
#         print("You can Become Uber Partner")
# else:
#     print("your ineligible for Become Partner")


#simplified way of thi code
name_applicant=input("Please Enter your Name:")
age_applicant=int(input("Please Enter your age:"))
if 60>=age_applicant >=21:
    print("{}You can Become Uber Partner your age is {} ".format(name_applicant,age_applicant))
else:
    print("{} your ineligible for Become Partner".format(name_applicant))