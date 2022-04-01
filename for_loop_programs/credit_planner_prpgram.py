purchased_loan = int(input("Enter the loan amount you have purchased : "))
emi = int(input("Enter the emi amount you are paying for it : "))
rate_of_interest = int(input("Enter the rate of interest : "))
num_years = int(input("Enter the number of years to see the balance amount on every month : "))

interest = purchased_loan * (rate_of_interest / 100)
print("Interest Amount (Am I doing the program properly) : ", interest)
# month_interest = interest / 12
# print("Monthly Interest for the loan : ", month_interest)
balance_amount = purchased_loan + interest - emi
print("The balance amount in", 1, "month is", balance_amount)

for i in range(2, num_years * 12):
    interest = balance_amount * (rate_of_interest / 100)
    # month_interest = interest / 12
    balance_amount = balance_amount + interest - emi
    print("The balance amount in", i, "month is", balance_amount)

# purchased_loan = int(input("Enter the loan amount you have purchased : "))
# emi = int(input("Enter the emi amount you are paying for it : "))
# rate_of_interest = int(input("Enter the rate of interest : "))
# num_years = int(input("Enter the number of years to see the balance amount on every month : "))
#
# # interest = purchased_loan * ((rate_of_interest * num_years) / 100)
# interest = purchased_loan * (rate_of_interest / 100)
# print("Interest Amount (Am I doing the program properly) : ", interest)
# # month_interest = ((purchased_loan * rate_of_interest) / 100) / 12
# month_interest = interest / 12
# print("Monthly Interest for the loan : ", month_interest)
# # interest = interest - month_interest
# # total = emi + month_interest
# balance_amount = purchased_loan + month_interest - emi
#
# for i in range(1, num_years * 12):
#     print("The balance amount in", i, "is", balance_amount)
#     interest = (balance_amount * rate_of_interest * num_years) / 100
#     month_interest = ((purchased_loan * rate_of_interest) / 100) / 12
#     interest = interest - month_interest
#     toatl = emi + month_interest
#     balance_amount = balance_amount - total
