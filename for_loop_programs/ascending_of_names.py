num = int(input("How many names do you want to enter? "))
list = []
for i in range (num) :
    name = input("Enter the name : ")
    list.append(name)
list.sort()
for i in list :
    print(i , end=' , ')