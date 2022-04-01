print ("Enter your \"Name\" below")
name = input()
count = 0
c_name = ""
length = len(name)
while count != length :
    temp = name[count]
    if temp.islower() :
        #print (temp.upper())
        c_name=c_name+temp.upper()
    else:
        #print (temp.lower())
        c_name = c_name + temp.lower()
    count = count + 1


print ("Change in Lower, Upper",c_name)