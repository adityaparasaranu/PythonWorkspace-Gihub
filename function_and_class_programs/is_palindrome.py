user_input = input("Enter your name : ")

def isPalindrome(user_input) :
    reverse_string = ""
    palindrome = "What you have entered is a Palindrome"
    not_palindrome = "What you have entered is not Palindrome"
    for i in range (len(user_input) - 1, -1 , -1) :
        reverse_string = reverse_string + user_input[i]
    if reverse_string == user_input :
        return palindrome
    else:
        return not_palindrome

print(isPalindrome(user_input))
