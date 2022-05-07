# To check the Indian Nationality
origin1 = input(" Enter your Country : ").upper()
if "india" in origin1.casefold():
    print("You are {}N ".format(origin1))
else:
    print("Your not indian ")