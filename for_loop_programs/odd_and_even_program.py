even_list = []
odd_list = []
getting_input = int(input("How many numbers do you want to enter? "))
for i in range (getting_input) :
    getting_input_2 = int(input("Enter the number : "))
    even = getting_input_2 % 2
    if even == 0 :
        even_list.append(getting_input_2)
    elif even != 0 :
        odd_list.append(getting_input_2)

print ("The Sum of Even numbers that you have entered is : ", sum(even_list))
print ("The Sum of Odd numbers that you have entered is  : ", sum(odd_list))