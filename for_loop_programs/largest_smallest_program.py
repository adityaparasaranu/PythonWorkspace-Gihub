no_count = int(input("How many numbers do you want to enter? "))
list = []
for i in range (no_count) :
    num = int(input("Enter the number : "))
    list.append(num)

largest = list[0]
smallest = list[1]
for j in list :
    if largest < j :
        largest = j
    elif smallest > j :
        smallest = j
print("The largest number you entered is : " , largest)
print("The smallest number you entered is : " , smallest)