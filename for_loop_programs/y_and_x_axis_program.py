y_axis = int(input("Enter the number for y axis here : "))
x_axis = int(input("Enter the number for x axis here : "))
default_symbol = input("Enter the default symbol here : ")
special_symbol = input("Enter the special symbol here : ")

for i in range (y_axis, 0, -1):
    for j in range (1, x_axis+1, 1):
        if i == j:
            print(special_symbol, end=' ')
        else:
            print(default_symbol, end=' ')
    print("\r")
