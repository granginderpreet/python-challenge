#!/usr/bin/env python
# coding: utf-8

# In[108]:


#import libraries
import csv
import os
#load input file
election_data_file = os.path.join(".", "Resources", "election_data.csv")

# total voters = length of file minus 1
total_voters = len (open (election_data_file).readlines ()) - 1 # first line is the header

#Create two dictionaies
summary={}
summary1={}
with open(election_data_file,"r") as election:
    electionData = csv.reader(election, delimiter=',')
    #Skip the header
    electionDataHeader = next(electionData)
    print(f' -----------------Election Results----------------')
    # Builds a diictionary of candidates and increments the value if he/she gets a vote ( each row is new voter)   
    for row in electionData:
        if not row[2] in summary:
            summary[row[2]] = 1
        else:
            summary[row[2]] += 1 
    maxvotes=0.0
output_path = os.path.join(".", "", "Results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile,delimiter=',')  

    # Write the first row (column headers). Note we use print to write to csvfile
    print('Election Results',file=csvfile)
    print("-----------------",file=csvfile)
    csvwriter.writerow(['Name','Count','Percentage'])

    print("Election Results")
    print("-----------------")
    print(f"Total Votes : {total_voters}")
    print("-----------------")
    print("Name Count Percentage")
    for j, k in summary.items():
        #Create a new dict that takes voter count and generates the percentage. The dictionary has candidates
        # as the key and value is a list : [vote count, % of total vote count]
        k1 = [k, str(round(100*float(k)/float(total_voters),2))]
        summary1[j]=k1
        print(f"{j} {k1[0]} {k1[1]}")
        csvwriter.writerow([j,k1[0], k1[1]])
        
    #find candidate with max votes
    max_key= max(summary1, key=summary1.get)
    print(f"The winner is {max_key}")        
    print(f"The winner is {max_key}",file=csvfile)
csvfile.close()


# In[109]:


result_file = os.path.join(".", "", "Results.csv")

with open(result_file,"r") as result:
    result = csv.reader(result, delimiter=',')
    for row in result:
        print (row)


# In[ ]:




