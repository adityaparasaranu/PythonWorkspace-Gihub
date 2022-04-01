import json

csv_file = open("csv_file.txt", "r")

final_dict = []

for lines in csv_file.readlines():
    line = lines.split(',')
    my_list = []
    for word in line:
        my_list.append(word.strip())
    my_dict = {"club" : my_list[0], "city" : my_list[1], "country" : my_list[2]}
    final_dict.append(my_dict)

csv_file.close()

json_file = open("json_file.txt", "w")
json.dump(final_dict, json_file)
json_file.close()
