num = int(input("Enter a number : "))

quotient = num
binary_code = ''

while quotient != 1:
    remainder = quotient % 2
    quotient = int(quotient / 2)
    binary_code = str(remainder) + binary_code

binary_code = str(quotient) + binary_code

print(f'The Binary Code of the Number {num} is : "{binary_code}"')
