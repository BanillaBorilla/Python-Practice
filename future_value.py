principal = float(input("Principal amount: "))
rate = float(input("Annual rate (as a decimal) "))
years = int(input("Number of years: "))
future_value = principal * (1 + rate) ** years
print("Future Value:", future_value)
