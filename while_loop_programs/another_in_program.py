print ("Enter your \"First Name\" below")
name1 = input()
print ("Enter your \"Last Name\" below")
name2 = input()
count = 0
length1 = len(name1)
length2 = len(name2)
if length1 != length2 :
    print ("Your \"First Name\" and \"Last Name\" is not the same")
    quit()
while count != length1 :
    temp2 = name2[count]
    if temp2 in name1 :
        print (temp2 , "is there in your \"First Name\". True")
    elif temp2 not in name1 :
        print (temp2 , "is not there in your \"First Name\". False")
        quit()
    count = count + 1


