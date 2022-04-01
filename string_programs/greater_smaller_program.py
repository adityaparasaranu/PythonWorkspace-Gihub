print ("Enter two number to check which one is \"Greater\" ")
print ("Enter the first number below 👇")
num1 = int (input())
print ("Enter the second number below 👇")
num2 = int (input())

if num1 > num2 :
    print ("The Number" , num1 , "\"Greater\"")
elif num1 == num2 :
    print ("Both the Numbers" , num1 ,"and" , num2 , "are equal")
else:
    print (num2 , "is \"Greater\" ")

if num1 < num2 :
    print ("The first number is the \"Smallest\" ")
elif num1 == num2 :
    print ("Both the values are equal")
else:
    print ("Second number is \"Smallest\" ")