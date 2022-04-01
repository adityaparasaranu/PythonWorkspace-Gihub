positive_list = []
negative_list = []
zero_list = []
num1 = int(input("How many numbers do you want to enter? "))
for i in range (num1) :
    num = input("Enter the number : ")
    remove_whitespace = num.strip()
    checking_numeric = num.isnumeric()
    if num == "0" :
        zero_list.append(num)
    elif remove_whitespace[0] == "-" :
        negative_list.append(num)
    elif num.isnumeric() == False :
        print("Please enter a numeric value")
        num = input("Enter the number : ")
    else:
        positive_list.append(num)

print ('No of "Positive Numbers" you entered is : ', len(positive_list))
print ('No of "Negative Numbers" you entered is : ', len(negative_list))
print ('No of "Zero" you entered is : ', len(zero_list))

