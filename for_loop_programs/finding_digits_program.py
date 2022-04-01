print ("Enter a \"Number\" below to find its \"Digits\" ")
num = int (input())
input_num = num
count = 0
while num != 0 :
    num = int(num/10)
    count = count + 1
print ("The \"Number\"" , input_num , "has" , count , "Digits")