#import libraries
import os
import csv

#File and path
budgetData_csv = os.path.join('Resources', 'budget_data.csv')

#Declare the variables 
total_months = []
total_profit = []
monthly_profit_change = []

#open the file 
with open(budgetData_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #This establishes the csv file to have a header
    header= next(csv_reader)        

    #Go through each row and count the number of rows 
    for row in csv_reader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    #Loop throguh to note the change between months 
    for x in range(len(total_profit)-1):

        monthly_profit_change.append(total_profit[x+1]-total_profit[x])  


    #We will use these variables to have the mac profit/loss change and greatest decrease in profit
    max_increase_value = max(monthly_profit_change)
    max_decrease_value = min(monthly_profit_change)
   
    #This is used to figure out the month in which the greatest increase and decrease of profit came from
    max_increase_month= monthly_profit_change.index(max(monthly_profit_change)) + 1
    max_decrease_month= monthly_profit_change.index(min(monthly_profit_change)) + 1

    #This will be the section of stuff we need to print
    print("PyBankAnalysisResults")
    print("--------------------------")
    
   # The total number of months included in the dataset
    print (f'Total Months: {len(total_months)}')

    # The net total amount of "Profit/Losses" over the entire period
    print (f'Total: ${sum(total_profit)}')

    print(f'Average Change:${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}')

    # Greatest Increase in Profits:
    # Greatest Decrease in Profits: 
    print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(max_increase_value)})")
    print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(max_decrease_value)})")
    

     
# Print the analysis to the terminal and export a text file with the results.
output_file = os.path.join("analysis","PyBankAnalysis.txt")

with open(output_file, 'w') as txt_file:
    txt_file.write("PyBankAnalysis\n")
    txt_file.write("--------------------------\n")
    
   # Number of months in the dataset
    txt_file.write (f'Total Months: {len(total_months)}\n')

    # Total "Profit/Losses" over time
    txt_file.write (f'Total: ${sum(total_profit)}\n')

    # Average changes in "profit/Losses" over time
    txt_file.write(f'Average Change:${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}\n')

    # Greatest Increase in Profits:
    # Greatest Decrease in Profits: 
    txt_file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(max_increase_value)})\n")
    txt_file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(max_decrease_value)})\n")
