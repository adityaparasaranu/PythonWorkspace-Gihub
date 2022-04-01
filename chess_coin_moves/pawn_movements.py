colour = input("What is the colour of the pawn? ")
c_p = input("Enter the current position of the pawn : ")
colour = colour.strip()
colour = colour.upper()
c_p = c_p.strip()
c_p = c_p.upper()
list = ["A", "B", "C", "D", "E", "F", "G", "H"]
for i in list:
    if c_p[0] == i and colour == "WHITE":
        if int(c_p[-1]) == 1:
            print("Movement not possible")
        elif int(c_p[-1]) == 2:
            print("The possible Movement is : ", c_p[0], int(c_p[-1]) + 1)
            print(c_p[0], int(c_p[-1]) + 2)
        elif int(c_p[-1]) > 2 and int(c_p[-1]) <= 7 :
            print(c_p[0], int(c_p[-1]) + 1)
        else:
            print("No movement possible")
    if c_p[0] == i and colour == "BLACK":
        if int(c_p[-1]) == 8 :
            print("Movement not possible")
        elif int(c_p[-1]) == 7:
             print("The possible Movement is : ", c_p[0], int(c_p[-1]) - 1)
             print(c_p[0], int(c_p[-1]) - 2)
        elif int(c_p[-1]) < 7 and int(c_p[-1]) >= 2 :
            print(c_p[0], int(c_p[-1]) - 1)
        else:
            print("Position not possible")
