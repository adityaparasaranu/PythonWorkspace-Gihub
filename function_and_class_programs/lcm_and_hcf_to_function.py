def find_hcf_and_lcm(num1, num2) :
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
        divisor = remainder
        dividend = divisor

    print(f"The HCF of the 2 Numbers is {divisor}")
    print(f"The LCM of the 2 Numbers is {(num1 * num2) / divisor}")

find_hcf_and_lcm(76, 96)
