total_num = int(input("How many numbers do you want to \"Compare\" ? : "))
list = []
for i in range (0 , total_num) :
    num = int(input("Enter the \"Number\" : "))
    list.append(num)

biggest = list[0]
for i in list :
    if i > biggest :
        biggest = i





print ("The \"Biggest\" Number is :" , biggest)
