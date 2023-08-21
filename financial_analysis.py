import csv
# import os
# Read the CSV file
# file_to_load = os.path.join(".","PyBank", "Resources", "budget_data.csv")
with open("PyBank/Resources/budget_data.csv", "r") as csvfile:

# with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header
    data = list(csvreader)
    #print(data)
# Initialize variables
total_months = len(data)
net_total = 0
changes = []
prev_profit_loss = int(data[0][1])
#print(prev_profit_loss)

# Calculate net total and changes
for row in data:
    profit_loss = int(row[1])
    net_total += profit_loss
    change = profit_loss - prev_profit_loss
    changes.append(change)
    prev_profit_loss = profit_loss
    #print(change)

# Calculate average change
average_change = sum(changes) / (total_months - 1)

# Find greatest increase and decrease
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Print results
print("Financial Analysis")
print("-" * 30)
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: (${greatest_increase})")
print(f"Greatest Decrease in Profits: (${greatest_decrease})")

# Export results to a text file
with open("financial_analysis_result.txt", "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-" * 30 + "\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: ${greatest_increase}\n")
    txtfile.write(f"Greatest Decrease in Profits: ${greatest_decrease}\n")
