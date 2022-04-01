print ("Enter a Number to see the number in Reverse Order")
num = int (input())
rev  = ""
while num != 0 :
    rem = int(num%10)
    print(rem)
    num = int(num/10)
    rev = rev + str (rem)

print (rev)