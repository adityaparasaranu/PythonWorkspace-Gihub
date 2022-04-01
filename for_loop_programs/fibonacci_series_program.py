num = int(input('Enter a number : '))
count = 0
list = []
for i in range (num) :
    count = count + 1
    if count >= 3:
        sum = list[count - 2] + list[count - 3]
        list.append(sum)
        print(sum)
    else:
        print(i)
        list.append(i)