user_input = int(input("How many numbers do you want to enter ? "))
list = []
def greatestNumber() :
    for i in range (user_input) :
        num = int(input("Enter a number : "))
        list.append(num)
    greatest = list[0]
    for i in list :
        if greatest < i :
            greatest = i
    print("The Greatest Number is : ", greatest)

def smallestNumber() :
    smallest = list[0]
    for i in list :
        if smallest > i :
            smallest = i
    print("The Smallest number is : ", smallest)

greatestNumber()
smallestNumber()