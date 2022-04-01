print ("These are the \"Prime Number\" from 1 to 50 :")
for i in range (50) :
    if i == 2 or i == 5 or i == 7 or i ==3 :
        print(i)
    elif i%2 == 0 or i%3 == 0 or i%5 == 0 or i%7 == 0 :
        continue
    else:
        print (i)