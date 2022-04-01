initial_deposit = int(input('Enter the Initial Deposit   : '))
rate_of_interest = int(input("Enter the Rate of Interest : "))
amount_every_year = int(input("Enter the Possible deposit Amount every year : "))
num_years = int(input("Enter number of years to calculate the savings till that year : "))

interest_amount = (rate_of_interest / 100) * initial_deposit
final_amount = initial_deposit + interest_amount
for i in range(1, num_years + 1):
    print("The amount you get in ", i, " years is ", final_amount)
    final_amount = final_amount + amount_every_year
    interest_amount = (rate_of_interest/100) * final_amount
    final_amount = final_amount + interest_amount
