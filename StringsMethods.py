#Various String Methods
himesh ='''
Junoon junoon junoon junoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon


Junoon junoon junoon junoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon


Junoon junoon junoon junoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon


Aye meri tamanna
Bin tere kahin na
Aye meri tamanna
Bin tere kahin na
Aaye mujhe sukoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon


Junoon junoon junoon junoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon


Hai meri tamanna
Bin tere kahin na
Aaye mujhe sukoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon


Main teri yaadon mein
Gumshuda humnashin
Jaan-e-jaan tum
Jahan zindagi hai wahi
Tere khayalon se
Jude mere raat din
Jeena mera hai bin
Tere ab na mumkin


Aye meri tamanna
Bin tere kahin na
Aaye mujhe sukoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon


Junoon mujhpe chhaaya
Tere ishq ka junoon


Kyon tere ishq mein
Dil kahin na lage
Tanha yeh dil jale
Ek pal na dhale
In dhadkano se aati
Hai ab to yeh sada
Teri hi khwaahish ab
To hai tera hi nasha


Aye meri tamanna
Bin tere kahin na
Aaye mujhe sukoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon.
'''
# print(himesh)
#Len property
print(len(himesh))

#Find -->Return index of First Occurance
#Syntax string.find("value")
print(himesh.find("Junoon"))#1

#count -->return number of occurance
print(himesh.count("Junoon")) #25

#title-->convert string to proper case(1st letter capital of each word)
himesh2=himesh.title()
print(himesh2.count("Junoon"))
#upper -->convert full string to upper case
#swapCase-->swap first letter of each word

# replace-->replace perticular work with new one
himes3=himesh2.replace("Junoon","Afternoon")
print(himes3)