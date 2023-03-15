# Part 1 --> Bring Required Modules Based on Python Session 2 Class

import os
import csv
    
    #Module below for mean funciton for monthly chnage 

from statistics import mean 

#From consultation, this will alow code to work on whatever directory i'm in 

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "profit_analysis.txt")

# Part 3 --> Create Data Lists and initiate variables (Moved up to fix sintax errors)
count = 0
profit = []
#previous_profit = 0
Total_Profit = 0
date = []
monthly_delta = []
total_delta_profits = 0
is_first_row = True 

# Part 2 --> Link python file to data base using methiod 2 exprored in class 

csvpath = os.path.join("Resources","Budget_data.csv")
with open(csvpath) as csvfile:

    #tell python the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    Csv_Header = next(csvreader) # unsure if we need this step
    print(csvreader)
    
    
    #no need to read header first as it already exists whilst printing data to ensure link is set up appropiately
    for row in csvreader:
        # line below used to ensure path worked correctly
        #print(row)
        count = count + 1
        #required for greates increase in profit 
        date.append(row[0])
        current_profit = int(row[1])
        #Adding profit info and calculations
        profit.append(current_profit)
       

        #Average chanege in profits 
        #ensuring the first cell equivalent to the excel file is blank
        if not is_first_row:
            monthly_delta_profits = current_profit - previous_profit
            monthly_delta.append(monthly_delta_profits)
        
        # Prepare for next row 
        is_first_row = False
        previous_profit = current_profit

        #average 
        # Get rid of based on consult --> average_delta_profits = total_delta_profits/count
        #average_delta_profits = (monthly_delta_profits)/count
    
    #Results:
    Total_Profit = sum(profit)

    #Min and Max
    Greatest_Delta_Decrease = min(monthly_delta)
    Decrease_Date = date[monthly_delta.index(Greatest_Delta_Decrease)]
    Greatest_Delta_Increase = max(monthly_delta)
    Increase_Date = date[monthly_delta.index(Greatest_Delta_Increase)]
            
    # getting the average DElta
    Average_Delta_Trial = round(sum(monthly_delta)/len(monthly_delta),2)
   



    print("---------------------------------------------")
    print("Financial Analysis")
    print("---------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: $" + str(Total_Profit))
    print("Average Change: $" + str(Average_Delta_Trial))
    print("greatest Increase in Profits: Occured on " +str(Increase_Date) + " Amounting to ($" + str(Greatest_Delta_Increase)+")")
    print("greatest Decrease in Profits: Occured on " +str(Decrease_Date) + " Amounting to ($" + str(Greatest_Delta_Decrease)+")")
    # Leaving the line below as an eater egg, code would not run properly until I added this in. Leaving in for personal Sanity :) 
    #print("I HOPE THIS WORKS")
    print("---------------------------------------------")
    

#Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    financial_results = (
       f"---------------------------------------------\n"
       f"Financial Analysis\n"
       f"---------------------------------------------\n"
       f"Total Months:  {str(count)} \n"
       f"Total Profits: $ {str(Total_Profit)}\n"
       f"Average Change: $  {str(Average_Delta_Trial)}\n"
       f"greatest Increase in Profits: Occured on " +str(Increase_Date) + " Amounting to ($" + str(Greatest_Delta_Increase)+")\n"
       f"greatest Decrease in Profits: Occured on " +str(Decrease_Date) + " Amounting to ($" + str(Greatest_Delta_Decrease)+")\n"
       f"---------------------------------------------\n")
    print(financial_results, end ="")
    txt_file.write(financial_results)
