from utility import greatestNumber , smallestNumber
user_input = int(input("How many numbers do you want to enter ? "))
list = []
for i in range(user_input):
    num = int(input("Enter a number : "))
    list.append(num)

print("The Greatest number is : ", greatestNumber(list))
print("The Smallest number is : ", smallestNumber(list))
