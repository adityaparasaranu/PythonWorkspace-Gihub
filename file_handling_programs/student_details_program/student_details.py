print("Enter 'h' to know the commands")

user_choice = """Enter,
- 'a' to add a student details
- 'l' to list the students who have got the
      percentage above the number you have given
- 'c' to clear the students details
- 'q' to quit
"""


def add_student():
    admission_no = input("Enter the Admission Number : ")
    name = input("Enter the Student Name : ")
    percentage = input("Enter the Student Percentage : ")
    with open("student.dat", "a") as student_file:
        student_file.writelines(f"{admission_no},{name.strip().lower()},{percentage}")
        student_file.writelines("\n")


def count_rec():
    display_list = []
    expecting_percentage = input("Enter the Percentage to list the Students who have got above it : ")
    with open("student.dat", "r") as student_file:
        list_of_contents = student_file.readlines()
    for lists in list_of_contents:
        student_details = lists.strip().split(',')
        if student_details[-1] >= expecting_percentage:
            display_list.append(student_details)

    if len(display_list) != 0:
        for student_detail in display_list:
            print(f"""
Admission Number  : {student_detail[0]}
Name              : {student_detail[1].title()}
Percentage Scored : {student_detail[2]}
""")
    elif len(display_list) == 0:
        print(f"There is no one who scored above {expecting_percentage} percentage")


def clear():
    with open("student.dat", "r+") as student_file:
        student_file.truncate(0)
    print("""
All the Students details are cleared successfully
""")


user_input = input("Enter the command here : ")
user_input = user_input.strip().lower()


while user_input != 'q':
    if user_input == 'a':
        add_student()
    elif user_input == 'l':
        count_rec()
    elif user_input == 'h':
        print(user_choice)
    elif user_input == 'c':
        clear()
    else:
        print("Wrong Command. Enter 'h' to know the commands")
    user_input = input("Enter the command here : ")
    user_input = user_input.strip().lower()
