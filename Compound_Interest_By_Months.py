initial_deposit = 6000000
interest = 0.30         ## 30% annual interest rate
contribution = 0      ## monthly contribution
time_period_months = 12


## For monthly compounding, we divide annual rate by 12
monthly_rate = interest / 12

## Calculate initial deposit growth
total_amount = initial_deposit * (1 + monthly_rate) ** time_period_months

## Calculate contribution growth
total_contribution = contribution * (((1 + monthly_rate) ** time_period_months - 1) / monthly_rate)

final_amount = total_amount + total_contribution


## Format and print with comma separator and 2 decimal places
formatted_amount = "{:,.2f}".format(final_amount)
print(formatted_amount)