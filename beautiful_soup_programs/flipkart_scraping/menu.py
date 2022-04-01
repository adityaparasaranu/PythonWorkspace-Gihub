from app import *

user_choice = """
Enter : 
- 'h' to know the commands
- 'a' to list all the Laptops
- 'b' to list the best Laptops
- 'c' to list the cheapest Laptops
- 'q' to quit

"""
print(user_choice)

user_input = input("Enter Here : ")
user_input = user_input.strip().lower()

while user_input != 'q':
    if user_input == 'h':
        print(user_choice)
    elif user_input == 'a':
        all_laptops()
    elif user_input == 'b':
        best_laptops()
    elif user_input == 'c':
        cheapest_laptops()
    else:
        print("Wrong Command")

    user_input = input("Enter Here : ")
    user_input = user_input.strip().lower()
