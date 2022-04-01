print ("Enter your \"Name\" below")
name = input()
count = 0
length = len(name)
while count != length :
    temp = name[count]
    if temp.islower() :
        print (temp.upper())
    else:
        print (temp.lower())
    count = count + 1
