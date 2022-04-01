print ("Enter three numbers to check which one is \"Greater\" ")
print ("Enter the first number below 👇")
num1 = int (input())
print ("Enter the second number below 👇")
num2 = int (input())
print ("Enter the third number below 👇")
num3 = int (input())

if num1 > num2 and num1 > num3 :
    print (num1 , "is the \"Greatest\" ")
elif num2 > num1 and num2 > num3 :
    print (num2 , "is the \"Greatest\" ")
elif num1 == num2 == num3 :
    print (num1 , num2 , num3 , "are \"Equal\" ")
elif num1 < num3 and num2 < num3 :
    print (num3 , "is the \"Greatest\" ")

if num1 < num2 and num1 < num3 :
    print (num1 , "is the \"Smallest\" ")
elif num2 < num1 and num2 < num3 :
    print (num2 , "is the \"Smallest\" ")
elif num1 == num2 == num3 :
    print (num1 , num2 , num3 , "are \"Equal\" ")
else :
    print (num3 , "is the \"Smallest\" ")