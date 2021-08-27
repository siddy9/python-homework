## Python script to calculate:
# Total no. of months in dataset
# Net total of profit/losses over the period
# Average of changes in profit/losses 
# Greatest increase in profits (date and amount)
# Greatest loss (date and amount)
### Print final results in terminal and export to a text file


from pathlib import Path
import csv

max_pnl = 0
min_pnl = 0
total_pnl = 0
pnl = []
pnl_dates = []
pnl_change = []

##Set file path
csvpath = Path("budget_data.csv")

##Pass through csv.reader function and populate lists for calculations
with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)
    for row in csv_reader:
        pnl.append(int(row[1]))
        pnl_dates.append(row[0])
        total_pnl += int(row[1])

##Calculate average change in profits and losses

for x in range(1, len(pnl)):
    change = pnl[x] - pnl[x - 1]
    pnl_change.append(int(change))

avg_change = round(sum(pnl_change)/len(pnl_change), 2)

##Logic to determine max profit and loss

for profloss in pnl:
    if profloss > max_pnl:
        max_pnl = profloss
    elif profloss < min_pnl:
        min_pnl = profloss

##Indexing dates to max profit and loss 

max_pnl_index = pnl.index(max_pnl)
min_pnl_index = pnl.index(min_pnl)

max_pnl_date = pnl_dates[max_pnl_index]
min_pnl_date = pnl_dates[min_pnl_index]

##Print calculations to terminal

print("Financial Analysis")
print("-------------------")
print(f"Total Months: {len(pnl)}")
print(f"Net total: ${total_pnl}")
print(f"Average Change: ${avg_change}")
print(f"Greatest increase in profits: {max_pnl_date} (${max_pnl})")
print(f"Greatest decrease in profits: {min_pnl_date} (${min_pnl})")

##Write calculations to text file

with open('financial_analysis.txt', 'w') as f:
    f.write("Financial Analysis\n")
    f.write("-------------------\n")
    f.write(f"Total Months: {len(pnl)}\n")
    f.write(f"Net Total: ${total_pnl}\n")
    f.write(f"Average Change: ${avg_change}\n")
    f.write(f"Greatest increase in profits: {max_pnl_date} (${max_pnl})\n")
    f.write(f"Greatest decrease in profits: {min_pnl_date} (${min_pnl})")
