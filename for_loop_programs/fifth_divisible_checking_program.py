list = ["0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10" , "11" , "12" , "13" , "14" , "15" , "16" , "17" , "18" , "19" , "20"]
#list = [0 , 1 , 2 , 3 , 4 , 5 , 6 ]
count = 0
for i in list :
    i = int (i)
    temp = (i%5)
    if temp == 0 :
        print (i, end=' ')
        count = count + 1
    else:
        continue
print("\r")

print ("Total Numbers = " , count )

