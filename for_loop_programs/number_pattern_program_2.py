num = int(input("Enter a number : "))
count = 0
for i in range (num + 1) :
    count = count + 1
    for j in range (1 , count) :
        print("*", end='  ')
    print("\r")