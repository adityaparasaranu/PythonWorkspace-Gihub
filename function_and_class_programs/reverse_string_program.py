user_input = input("Enter your name : ")

def reverseString(user_input) :
    reverse_string = ""
    for i in range (len(user_input) - 1, -1 , -1) :
        reverse_string = reverse_string + user_input[i]
    return reverse_string

print(reverseString(user_input))
