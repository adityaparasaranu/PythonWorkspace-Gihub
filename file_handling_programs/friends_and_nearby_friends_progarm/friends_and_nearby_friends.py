friends = input("Enter your friends names by commas (without any space) : ").split(',')
name_read = open('name.txt', 'r')
list = name_read.readlines()
name_read.close()

final_names = []

for friend in friends:
    for name in list:
        if name.strip() == friend:
            final_names.append(name)



nearby_file_open = open('nearby_friends.txt', 'w')
nearby_file_open.writelines(final_names)
nearby_file_open.close()

