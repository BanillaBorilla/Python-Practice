def future_value(principal, rate, years):
    return principal * (1 + rate) ** years

principal = 5000
rate = 0.05

for year in range (1, 21):
    balance = future_value(principal, rate, years)
    print("Year", year, ":", round(balnace, 2))
    