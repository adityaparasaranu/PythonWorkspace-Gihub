print ("Type entering any number to check whether it is \"Prime Number\" or \"Not\" ")
num = int (input())
if num == 1 :
    print (num , "is Neither Prime nor Composite")
elif num%3 == 0 or num%4 == 0 or num%5 == 0 or num%6 == 0 or num%7 == 0 or num%8 == 0 or num%9 == 0 or num%10 == 0 or num%11 == 0 :
    print ("No" , num , "is not a \"Prime Number\". It is a Composite")
elif num == 2 :
    print ("Yes 2 is a \"Prime Number\" ")
else:
    print ("Yes" , num , "is a \"Prime Number\"")
