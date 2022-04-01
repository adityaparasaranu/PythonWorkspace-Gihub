user_choice = """Enter:
- 'a' to add a book
- 'c' to count the number of books with 
       the author name you have give
- 'q' to quit
Enter here : """


def create_file():
    book_no = input("Enter the Book No : ")
    book_name = input("Enter the Book Name : ")
    author = input("Enter the Author: ")
    price = input("Enter the Price of book : ")
    with open("book.dat", "a") as book_file:
        book_file.writelines(f"{book_no},{book_name.strip().lower()},{author.strip().lower()},{price}")
        book_file.writelines("\n")


def count_rec():
    count = 0
    author = input("Enter the Author to find the books he has written : ")
    with open("book.dat", "r") as book_file:
        list_of_contents = book_file.readlines()

    for lists in list_of_contents:
        book_details = lists.strip().split(',')
        if book_details[2] == author.strip().lower():
            count = count + 1
    print(f'The Author : "{author.strip()}" has written {count} books')


user_input = input(user_choice)

while user_input.strip().lower() != 'q':
    if user_input.strip().lower() == 'a':
        create_file()
    elif user_input.strip().lower() == 'c':
        count_rec()
    else:
        print("Wrong Command")
    user_input = input(user_choice)
