#!/usr/bin/env python
# coding: utf-8

# In[110]:


#Import libraries
import csv
import os

#Read input data
budget_csv_file = os.path.join(".", "Resources", "budget_data.csv")

#Find number of months
total_months = len (open (budget_csv_file).readlines ()) - 1 # first line is the header

# create a new list for output
updated_budget=[]

#read each row from input file
with open(budget_csv_file,"r") as budget:
    budget_file_contents = csv.reader(budget, delimiter=',')
    #Skip the header
    budget_file_header = next(budget_file_contents)
    
    print(f' -----------------Financial Analysis----------------')
    
    #Declare variables
    totalProfitLoss=0
    prevProfitLoss=0xffffffff 
    maxPlusChange=0
    averageChangeInProfitLoss=0
    maxMinusChange=0
    
    for row in budget_file_contents:
        #Calculate total PNL
        totalProfitLoss += int(row[1])
        if (prevProfitLoss == 0xffffffff):   #For first row, since there is no pre value, 
                                            # we set the change value to 0. 
            row.append("0")
        else:
            row.append(str(int(row[1])-int(prevProfitLoss)))
        prevProfitLoss= int(row[1])   # update prev value with current value
        
        if (int(row[2]) > maxPlusChange):    #Track min and max. Note that row[2] is the new item
                                             # we added to the list that tracks the changeinProfitandLoss
                maxPlusChange=int(row[2])
        elif (int(row[2]) < maxMinusChange):
                maxMinusChange=int(row[2])
        
        averageChangeInProfitLoss += int(row[2])
        updated_budget.append(row[0])  # Update the new list with month
        updated_budget.append(row[2])  # Update the new list with changeinprofitandloss
    #print(updated_budget)
    averageChangeInProfitLoss=averageChangeInProfitLoss/(total_months-1)  #because first month is ignored for increase/decrease 
    maxincreasemonth=updated_budget[updated_budget.index(str(maxPlusChange))-1] # to get to the month
    maxdecreasemonth=updated_budget[updated_budget.index(str(maxMinusChange))-1] # to get to the month
    print(f' Total Months : {total_months}')
    print(f' Total : {totalProfitLoss}')
    print(f' Average Change : {averageChangeInProfitLoss}')
    print(f' Greatest increase in Profits : {maxPlusChange} during month of {maxincreasemonth}')
    print(f' Greatest decrease in Profits : {maxMinusChange} during month of {maxdecreasemonth}')

#Write output file
output_path = os.path.join(".", "", "Results.csv")
with open(output_path, 'w') as csvfile:
#Note that csvwriter API wasnt used since it wasnt easy to use writerow with delimitor set to space. 
#Setting the delimiter to | or tab or : was possible but when I set delimiter to " ", output file would have
# unnecessary "" around every print string. Using print function was much easier
    print("Summary",file=csvfile)
    print("-----------------",file=csvfile)
    print(f"Total Months:{total_months}",file=csvfile)
    print(f"Total Profit and Loss:{totalProfitLoss}",file=csvfile)
    print(f"Average Change in Profile and Loss:{averageChangeInProfitLoss}",file=csvfile)
    print(f"Greatest increase in Profits:{maxPlusChange} during month of {maxincreasemonth}",file=csvfile)
    print(f"Greatest decrease in Profits:{maxMinusChange} during month of {maxdecreasemonth}",file=csvfile)
#close file
csvfile.close()


# In[ ]:





# In[ ]:




