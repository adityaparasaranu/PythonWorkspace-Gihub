print ("Enter your a \"Name\" below")
name1 = input()
print ("Enter another \"Name\" below")
name2 = input()
temp = ""
if name1[0].islower() :
    temp = name1[0].upper()
    #print (name1[0].upper())
    #print (temp)

elif name1[0].isupper() :
    temp = temp + name1[0].lower()
    #print (temp)

if name2[0].isupper() :
    #print (name2[0].lower())
    temp = temp + name2[0].lower()
    #print (temp)

elif name2[0].islower() :
    temp = temp + name2[0].upper()
    #print(temp)

if name1[-1].islower() :
    #print (name1[-1].upper())
    temp = temp + name1[-1].upper()
    #print (temp)

elif name1[-1].isupper() :
    #print (name1[-1].lower())
    temp = temp + name1[-1].lower()
    #print (temp)

if name2[-1].isupper() :
    #print (name2[-1].lower())
    temp = temp + name2[-1].lower()
    #print (temp)

elif name2[-1].islower() :
    #print (name2[-1].upper())
    temp = temp + name2[-1].upper()
    print (temp)
