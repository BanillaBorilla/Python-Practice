import csv

best_month = ""
worst_month = ""
worst_revenue = 10000000
best_revenue = 0
total = 0
count = 0     

with open("revenue.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        revenue = float(row[1])
        total = total + float(row[1])
        count = count + 1
        if revenue > best_revenue:
            best_revenue = revenue
            best_month = row[0]
        if revenue < worst_revenue:
            worst_revenue = revenue
            worst_month = row[0]

with open("report.txt", "w") as report:
          report.write("REVENUE REPORT\n")
          report.write("Total revenue: " + str(total)+ "\n")
          report.write("Average monthly: " + str(round(total / count, 2)) + "\n")
          report.write("Best month: " + best_month + " (" + str(best_revenue) + ")\n")
          report.write("Worst month: " + worst_month + " (" + str(worst_revenue) + ")\n")
          report.write("Report Produced by BanillaBorilla" "\n")

print("Report written to report.txt")
