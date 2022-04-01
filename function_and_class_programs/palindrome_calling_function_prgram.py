user_input = input("Enter your name : ")

def reverseString(user_input) :
    reverse_string = ""
    for i in range (len(user_input) - 1, -1 , -1) :
        reverse_string = reverse_string + user_input[i]
    return reverse_string

def isPalindrome(user_input) :
    palindrome = "What you have entered is a Palindrome"
    not_palindrome = "What you have entered is not Palindrome"
    reverseString(user_input)
    if reverseString(user_input) == user_input :
        return palindrome
    else:
        return not_palindrome

print(isPalindrome(user_input))