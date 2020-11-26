"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
if sales>=0 and sales < 1000:
    low_bonus = sales * 0.1
    print("The bonus is {:.2f}".format(low_bonus))
elif sales >= 1000:
    high_bonus = sales * 0.15
    print("The bonus is {:.2f}".format (high_bonus))
else:
    print("Error")

