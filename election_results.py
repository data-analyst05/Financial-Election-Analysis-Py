import csv

# Read the CSV file
with open("PyPoll/Resources/election_data.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header
    data = list(csvreader)

# Initialize variables
total_votes = len(data)
candidates = {}
winner = ""
max_votes = 0

# Count votes for each candidate
for row in data:
    candidate = row[2]
    if candidate in candidates:
        candidates[candidate] += 1
    else:
        candidates[candidate] = 1
    if candidates[candidate] > max_votes:
        max_votes = candidates[candidate]
        winner = candidate

# Print results
print("Election Results")
print("-" * 30)
print(f"Total Votes: {total_votes}")
print("-" * 30)
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-" * 30)
print(f"Winner: {winner}")
print("-" * 30)

# Export results to a text file
with open("election_result.txt", "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-" * 30 + "\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-" * 30 + "\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write("-" * 30 + "\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-" * 30)