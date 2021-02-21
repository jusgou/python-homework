import pathlib
import csv


from pathlib import Path


print(Path.cwd())


csvpath = pathlib.Path("Resources/budget_data.csv")


date = []
line_num = 0


pl_amount = []
line_num = 1


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    line_num += 1
    for row in csvreader:
        profit_list = int(row[1])
        pl_amount.append(profit_list)


max_pl = 0
min_pl = 0 
avg_pl = 0
total_pl = 0
count_pl = 0
greatest_increase_date = [""
greatest_decrease_date = ""


for row in len():
    #sum the total and count variables
    total_pl += profit_list
    count_pl += 1
    


print(len(date_list))
    


print(mx_pl, min_pl, avg_pl)




# Print the metrics
print(max_salary, min_salary, avg_salary)

# Set the output header
header = ["Max_Salary", "Min_Salary", "Avg_Salary"]
# Create a list of metrics
metrics = [max_salary, min_salary, avg_salary]

# Set the output file path
output_path = Path('output.csv')

# Open the output path as a file object
with open(output_path, 'w') as csvfile:
    # Set the file object as a csvwriter object
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the header to the output file
    csvwriter.writerow(header)
    # Write the list of metrics to the output file
    csvwriter.writerow(metrics)



for x in range:
    print(len(csvreader))


net_total_pl = round(total_pl)


avg_pl = round(total_pl / count_pl, 2)








if min_profit ==0
    min_profit == pn_amount
    min_month = month
elif prifot_or_loss < min_profit:
        min_profit = prifotorloss
        min_month 

        


print("")







