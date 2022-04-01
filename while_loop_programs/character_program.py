print ("Enter your \"Name\" below")
name = input()
count = 0
length = len(name)
no_char = 0
no_num = 0
no_other = 0
while count != length :
        temp = name[count]
        if temp.islower() or temp.isupper() :
            no_char = no_char + 1
        elif temp.isnumeric() :
            no_num = no_num + 1
        else:
            no_other = no_other + 1
        count = count + 1

print ("No of \"Alphabets\" in your Name is       :" , no_char)
print ("No of \"Numerical Values\" in your Name is:" , no_num)
print ("No of \"Special Characters in your Name is:" , no_other)