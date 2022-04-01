book = []


def add_book():
    name = input("Enter the book name :")
    author = input("Enter the author of the book :")
    book.append({"name": name, "author": author, "read":False})


def list_books():
    print(book)


def read_book():
    name = input("Enter the book name to mark it as read :")
    for dictionary in book:
        if dictionary["name"] == name:
            dictionary["read"] = True


def delete_book():
    name = input("Enter the book name to delete:")
    for dictionary in book:
        if dictionary["name"] == name:
            book.remove(dictionary)

