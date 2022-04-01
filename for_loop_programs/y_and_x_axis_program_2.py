y_axis = int(input("Enter the number for y axis here : "))
x_axis = int(input("Enter the number for x axis here : "))
y_point = int(input("Enter the y axis point : "))
x_point = int(input("Enter the x axis point : "))

for i in range (y_axis, 0, -1):
    for j in range (1, x_axis+1, 1):
        if i == y_point and j == x_point:
            print(" ", end=' ')
        else:
            print("*", end=' ')
    print("\r")