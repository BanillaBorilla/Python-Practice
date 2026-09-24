def npv(rate, cash_flows):
    total = 0
    for year in range (len(cash_flows)):
        total = total + cash_flows[year] / (1 +rate) ** year
    return total

cash_flows = [-10000, 3000, 4000, 5000, 6000]
print("NPV at 10%:", round(npv(0.10, cash_flows), 2))

result = npv(0.10, cash_flows)

if result > 5000: 
    print("Decision: STRONG BUY - NPV is positive")
elif result > 0: 
    print("Decision: INVEST - NPV is positive")
else:
    print("Decision: WALK AWAY - NPV is negative")
