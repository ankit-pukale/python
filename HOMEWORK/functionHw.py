
def is_palindrome(string1):
   name2=string1[::-1]
   return name2==string1

word=input("Enter your name to check :")
if is_palindrome(word.casefold()):
       print("Given string is palindrome")
else:
    print("given string is not palindrome")
