y_axis = int(input("Enter the number for y axis here : "))
x_axis = int(input("Enter the number for x axis here : "))

for i in range (y_axis, 0, -1):
    for j in range (1 , x_axis + 1, 1) :
        even = j%2
        if even != 0 :
            print ("*" , end=' ')
        # else:
        #     print("$", end=' ')
        elif even == 0 :
            print ("$" , end=' ')
    print("\r")