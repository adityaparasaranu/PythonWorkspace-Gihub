print("Welcome to ARADI shop")
first_value = int(input("Enter the Shoulder width (in cm)     : "))
second_value =int(input("Enter the Chest Size (in cm)         : "))
third_value = int(input("Enter the Length of the Shirt (in cm): "))
if first_value <= 28 and first_value >= 20 and second_value <= 25 and second_value >= 15 and third_value <= 35 and third_value >= 20 :
    print("You need a Small size shirt")
elif first_value >= 28 and first_value <= 40 and second_value >= 25 and second_value <=45 and third_value >= 20 and third_value <= 45  :
    print("You will need a Medium size shirt")
elif first_value >= 40 and first_value <= 45 and second_value >= 45 and second_value <= 60 and third_value >= 45 and third_value <= 65  :
    print("You will need a Large size shirt")
elif first_value >= 45 and first_value <= 55 and second_value >= 60 and second_value <= 70 and third_value >= 65 and third_value <= 80  :
    print("You will need a X - Large shirt")
else:
    print("Sorry we could'nt find a shirt with the measurement you have given")


