from file_handling_programs.mile_stone_project.utils import database

user_choice = """
Enter 
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark as a book read
- 'd' to delete a book
- 'q' to quit
Enter here : """
user_input = input(user_choice)
while user_input != 'q' :
    if user_input == 'a':
        database.add_book()

    elif user_input == 'l':
        database.list_books()

    elif user_input == 'r':
        database.read_book()

    elif user_input == 'd':
        database.delete_book()

    else:
        print("It is a wrong command")

    user_input = input(user_choice)
