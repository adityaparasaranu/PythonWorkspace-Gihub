question_file = open("questions.txt", "r")
marks = 0
list_of_questions = []

for questions in question_file.readlines():
    list_of_questions.append(questions.strip())
question_file.close()

for question in list_of_questions:
    split_list = question.split('=')
    user_input = int(input(f"{split_list[0]}="))
    if user_input == int(split_list[-1]):
        marks = marks + 1

result_file = open("result.txt", "w")
result_file.write(f"You scored {marks}/{len(list_of_questions)}")
print('See your results in "result.txt" file')

