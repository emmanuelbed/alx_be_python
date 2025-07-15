# Objective: Use user input, variables, and arithmetic operations to calculate and provide feedback on a user’s monthly savings and potential future savings without applying conditional statements.

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

interest = 0.05

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * interest)

print("Your monthly savings are ", str(monthly_savings))
print("Projected savings after one year, with interest, is: $", str(projected_savings))