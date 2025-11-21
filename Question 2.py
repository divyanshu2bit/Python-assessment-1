# Cost calculations for hosting provider

cost_per_hour = 0.51
cost_per_day = 24 * cost_per_hour
cost_per_week = 7 * cost_per_day
cost_per_month = 4 * cost_per_week   # assuming 4 weeks per month

balance = 918

days_operable = balance / cost_per_day

print("Cost per day: $", cost_per_day)
print("Cost per week: $", cost_per_week)
print("Cost per month: $", cost_per_month)
print("Number of days you can operate with $918:", days_operable)
