month = ['January','February','March','April','May','June','July','August','September','October','November','December']
days = [31 , 28 , 31 , 30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31]
nested_list = []
for i in range (0 , len(month)) :
    temp=[month[i], days[i]]
    nested_list.append(temp)

print(nested_list)


month_input = input('Enter the month name to find its days : ')
month_input_index = month.index(month_input)
no_of_days = nested_list[month_input_index][1]
#print ('Number of Days in the month' , month_input , 'is : ' , days[month_input_index])
print ('Number of Days in the month' , month_input , 'is : ' , no_of_days)