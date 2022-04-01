name_writing = open('name.txt', 'w')
user_input = input('Enter your name : ')
name_writing.write(user_input)
name_writing.close()

name_reading = open('name.txt', 'r')
print(name_reading.read())
name_reading.close()