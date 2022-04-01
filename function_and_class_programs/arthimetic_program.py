user_input = input("Enter what Arithmetic operator you want to preform : ")
user_input = user_input.strip()
user_input = user_input.upper()

input_num1 = int(input("Enter a number : "))
input_num2 = int(input("Enter another number : "))

def addition(num1, num2) :
    return num1 + num2
def subtraction(num1, num2) :
    return num1 - num2
def multiplication(num1, num2) :
    return num1 * num2
def divison(num1, num2) :
    return num1 / num2

def checking(user_input) :
    if user_input == "ADDITION" :
        print(addition(input_num1, input_num2))
    elif user_input == "SUBTRACTION" :
        print(subtraction(input_num1, input_num2))
    elif user_input == "MULTIPLICATION":
        print(multiplication(input_num1, input_num2))
    elif user_input == "DIVISION":
        print(divison(input_num1, input_num2))

checking(user_input)
