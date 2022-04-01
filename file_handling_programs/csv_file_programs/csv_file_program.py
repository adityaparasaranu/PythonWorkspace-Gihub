csv_file = open("csv_file.txt", "r")
csv_file_readlines = csv_file.readlines()
csv_file.close()

csv_file_list = [lines.strip() for lines in csv_file_readlines[1:]]

storing_sentence = ''

for line in csv_file_list:
    line = line.split(',')
    name = line[0].strip().title()
    age = line[1].strip()
    passion = line[2].strip().title()

    storing_sentence = storing_sentence + f"Hi {name}. Your age is {age}. And your passion is {passion}.""\n"

print(storing_sentence)