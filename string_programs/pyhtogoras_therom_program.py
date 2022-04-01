import math

print('Enter "0" to for the side to be found out')

a = int(input("Enter the length of the side \"a\" of the triangle : "))
b = int(input("Enter the length of the side \"b\" of the triangle : "))
c = int(input("Enter the length of the side \"c\" of the triangle : "))

if a == 0 and b != 0:
    num = c ** 2 - b ** 2
    final_answer = math.sqrt(num)
    print(f"The length of side \"a\" is \"{final_answer}\" ")
    quit()

elif b == 0 and a != 0:
    num = c ** 2 - a ** 2
    final_answer = math.sqrt(num)
    print(f"The length of side \"b\" is \"{final_answer}\" ")
    quit()

elif c == 0 and a != 0:
    num = a ** 2 + b ** 2
    final_answer = math.sqrt(num)
    print(f"The length of side \"c\" is \"{final_answer}\" ")
    quit()

print("You have entered 0 for every value. Pls try again")
