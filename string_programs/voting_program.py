print ("Please Enter the below details to \"Vote\" ")
print ("What is your \"Name\" ? ")
name = input()
print ("What is your \"Nationality\" ?")
n = input()
if n == "Indian" :
    print ("What is your \"Age\" ?")
elif n == "indian" :
    print ("What is your \"Age\" ?")
else:
    print ("Sorry" , name ,", you are not eligible to vote because of your \"Nationnality\" ")
    quit()
age = int (input())
if age <18 :
    print ("Sorry" , name ,", with \"Nationnality\" as" , n , "you are not eligible to vote because of your \"Age\" ")
    quit()
elif age >=18 :
    print ("What is your \"Identity Proof\" ? ")
pro = input()
if pro == "Passport" :
    print (name , ", you are eligible to \"Vote\" 👍 ")
elif pro == "passport" :
    print (name, ", you are eligible to \"Vote\" 👍 ")
elif pro == "Driving License" :
    print (name, ", you are eligible to \"Vote\" 👍 ")
elif pro == "driving license" :
    print (name, ", you are eligible to \"Vote\" 👍 ")
elif pro == "Adhaar Card" :
    print (name, ", you are eligible to \"Vote\" 👍 ")
elif pro == "adhaar card" :
    print (name, ", you are eligible to \"Vote\" 👍 ")
else:
    print ("Sorry" , name ,",with \"Nationnality\" as " , n ,"and with" , age , "years \"Age\" you are not able to vote because of your \"Identity Proof\" " )
