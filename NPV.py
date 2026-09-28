def npv(rate, cash_flows):
    total = 0
    for year in range(len(cash_flows)):
        total = total + cash_flows[year] / (1 + rate) ** year
    return total

projects = {
    "Alpha": [-10000, 3000, 4000, 5000, 6000],
    "Beta":  [-8000, 2000, 3000, 4000, 5000],
    "Gamma": [-12000, 5000, 5000, 5000, 5000],
    "Delta": [-10000, 5000,5000, 5000, 5000],
}

for name in projects:
    value = npv(0.10, projects[name])
    print(name, "NPV:", round(value, 2))


