name = input("Enter here : ")
no_capital_letters = 0
no_small_letters = 0
no_special_symbols = 0
no_numbers = 0
for i in range (0, len(name), 1):
    if name[i].islower():
        no_small_letters = no_small_letters + 1
    elif name[i].isupper():
        no_capital_letters = no_capital_letters + 1
    elif name[i].isnumeric():
        no_numbers = no_numbers + 1
    else:
        no_special_symbols = no_special_symbols + 1

print("No of Characters is      : " , len(name))
print("No of Capital Letters is : " , no_capital_letters)
print("No of Small Letters is   : " , no_small_letters)
print("No of Numericals is      : " , no_numbers)
print("No of Special Symbols is : " , no_special_symbols)

