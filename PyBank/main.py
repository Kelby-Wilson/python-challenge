import os
import csv

budget_data = ['1','2']

month_counter = 0
sum_revenue = 0
sum_revenue_change = 0

for files in budget_data:
    budget_data.csv = os.path.join("Desktop/UCB_work/PyBank", 'budget_data' + files + '.csv')
   
    with open(budget_data.csv) as csvfile:

        csvreader = csv.reader(csvfile, delimiter=',')

next(csvReader, None)
        
        line = next(csvreader,none)
        max_month = line[0]
        min_month = line[0]
        revenue = float(line[1])
        min_revenue = revenue
        max_revenue = revenue
        previous_revenue = revenue
        month_counter = 1
        sum_revenue = float(line[1])
        sum_revenue_change = 0

        for line in csvReader
            month_counter = month_counter + 1

            revenue = float(line[1])

            sum_revenue = sum_revenue + revenue

            revenue_change = revenue - previous_revenue

            sum_revenue_change = sum_revenue_change + revenue_change

            if revenue_change > max_revenue:
                max_month = line[0]
                max_revenue = revenue_change

            if revenue_change < min_revenue:
                min_month = line[0]
                min_revenue = revenue_change
 
            previous_revenue = revenue

        average_revenue = sum_revenue/month_counter
        average_revenue_change = sum_revenue_change/(month_counter-1)

        sum_revenue = int(sum_revenue)
        average_revenue_change = int(average_revenue_change)
        max_revenue = int(max_revenue)
        min_revenue = int(min_revenue)
        
        print(f"Financial Analysis:")
        print("-------------------------------------------------------")
        print(f"Total Months: {month_counter}")
        print(f"Total Revenue: {sum_revenue} USD")
        print(f"Average Revenue Change: {average_revenue_change} USD")
        print(f"Greatest Increase in Revenue: {max_month} {max_revenue} USD")
        print(f"Greatest Decrease in Revenue: {min_month} {min_revenue} USD")
        print("")
        
        output_file = budget_data.csv[0:-4]

        write_budget_data.csv = f"{output_file}_PyBank_results.txt"

        filewriter = open(write_budget_data,csv, mode = 'w')

        filewriter.write(f"Financial Analysis:\n")
        filewriter.write("-------------------------------------------------------\n")
        filewriter.write(f"Total Months: {month_counter}")
        filewriter.write(f"Total Revenue: {sum_revenue} USD\n")
        filewriter.write(f"Average Revenue Change: {average_revenue_change} USD\n")
        filewriter.write(f"Greatest Increase in Revenue: {max_month} {max_revenue} USD\n")
        filewriter.write(f"Greatest Decrease in Revenue: {min_month} {min_revenue} USD\n")
        filewriter.write("")

        filewriter.close()
