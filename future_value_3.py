def future_value(principal, rate, years):
    return principal * (1 + rate) ** years

def present_value (future_amount, rate, years):
    return future_amount / (1 + rate) ** years

# Use them like built-in commands:
print("Invest $10,000 at 6% for 30 years:", future_value(10000, 0.06, 30))
print("Need $100,000 in 25 years at 7%, invest today:", present_value(10000, 0.07, 25))
print("Invest $5,000 at 5% for 20 years:", future_value(5000, 0.05, 20))

def total_interest(principal, rate, years):
    return future_value(principal, rate, years) - principal
print("Interest on $10,000 at 6% for 30 years:", total_interest(10000, 0.06, 30))

      