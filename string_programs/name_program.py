print ("Enter your \"First Name\" ")
name1 = input()
print ("Enter your \"Last Name\" ")
name2 = input()





print ("Your First Name and Last Name with Capital Letters   :",name1.capitalize() + " " + name2.capitalize())
print ("Your name with All Capital Letters                   :",name1.upper() + " " + name2.upper())
print ("Your name with All Small Letters                     :",name1.lower() + " " + name2.lower())
print ("The Length of your First Name is                     :",len(name1))
print ("The Length of your Last Name is                      :",len(name2))
print ("Your First Name as Last Name and Vice Versa          :",name2 , name1)
print ("No of Vowels in your First Name is                   :",name1.count('a') + name1.count('e') + name1.count('i') + name1.count('o') + name1.count('u'))
print ("No of Vowels in your Last Name is                    :",name2.count('a') + name2.count('e') + name2.count('i') + name2.count('o') + name2.count('u'))
print ("Your First Name written 5 times                      :",name1 * 5)
print ("Your Last Name written 5 times                       :",name2 * 5)
