print ("Do you want to check a number whether a number it is \"Fully Divisible of a Divisor\" ?  ")
print ("Enter the \"Dividend\" below 👇")
num1 = int (input())
print ("Enter the \"Divisor\" below 👇")
num2 = int (input())
rem = num1 % num2
if rem == 0 :
    print ("Yes , the \"Dividend\" is \"Fully Divisible by Divisor\" ")
else:
    print ("No , the \"Dividend\" is not \"Fully Divisible by Divisor\" ")