import csv

total = 0
count = 0

with open("revenue.csv") as file:
    reader = csv.reader(file)
    next(reader) # skip the header row
    for row in reader:
        total = total + float(row[1])
        count = count + 1

print("Total revenue:", total)
print("Average monthly:", round(total / count, 2))
