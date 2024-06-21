monthly_income = int( input('enter your monthly income please'))
monthly_expenses = int( input('enter your monthly expenses please'))
monthly_savings = monthly_expenses - monthly_income 
annual_interest_rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

print('Your monthly savings are ',monthly_savings)
print('Projected savings after oner year , with interest is :',projected_savings)