num = int(input("Enter the number of columns : "))
symbol = input("Enter the symbol that you want to be displayed : ")

# Here i in the loop acts as the row
# and j in the loop acts as the column of numbers
for i in range(1, num+1):
    for j in range(1, i+1):
        print(symbol, end=' ')
    print()
