num1 = int(input("Enter a Number : "))
num2 = int(input("Enter a Number : "))

if num1 > num2 :
    dividend = num1
    divisor = num2
elif num2 > num1 :
    dividend = num2
    divisor = num1
else:
    dividend = num1
    divisor = num2

remainder = 1

while remainder != 0 :
    remainder = dividend % divisor
    if remainder == 0:
        continue
    dividend = divisor
    divisor = remainder


print(f"The HCF of the 2 Numbers is {divisor}")
print(f"The LCM of the 2 Numbers is {(num1 * num2) / divisor}")

