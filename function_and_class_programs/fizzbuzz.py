def fizz_buzz(integer):
    if int(integer) % 3 == 0 and int(integer) % 5 == 0:
        return "FizzBuzz"
    elif int(integer) % 3 == 0:
        return "Fizz"
    elif int(integer) % 5 == 0:
        return "Buzz"
    else:
        return integer


for i in range(10):
    print(fizz_buzz(i))
