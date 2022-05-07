# ui=int(input("enter Percentage:"))
# print(ui>=40)
himesh='''O.. huzoor
Tera tera tera suroor
Meri baatein, meri yaadein, tanha raatein
Tera tera tera suroor
Mere kisse, meri saanein, meri aahein
Tera tera tera suroor
O. huzoor
Tera tera tera suroor
Tujh mein basi hai meri duniya
Tujh mein rawaan hai meri khushiya
Tujh se ummeedein mujhko badi
Todd na dena dil ki kadi
Iss dard ka ehsaas poocho na
Poocho na poocho na, poocho na
Poocho na sanam
Mere armaan, mere lamhe, mere nagme
Tera tera tera suroor
Tanhaiyon mein tu hi shaamil,
Tere bina jeena bada mushkil
Tere siva kuch na aaye nazar
Nazron pe chaaya tera manzar
Rab hi jaane ye pyaas kaisi hai
Dekho na dekho na dekho na
Dekho na sanam
Meri dhadkan, meri tadpan, mera jeevan
Tera tera tera suroor
Meri baatein, meri yaadein, tanha raatein
Tera tera tera suroor
'''
himesh2=himesh.title()
print("****Number of Occurance of Word Tera*******")
print(himesh2.count("Tera"))
himesh3=himesh2.replace("Tera","mera")
print("****Word Tera Replaced With word mera*******")
print(himesh3) 
print("****First Occurance of Word poocho*******")
print(himesh.find("poocho"))
print("****is all characters are alphabet letters*******")
print(himesh3.isalpha())

       
