#!/usr/bin/env python
# coding: utf-8

# In[14]:


import os
import csv

budget_csv_path = os.path.join('..', 'PyBank', 'budget_data.csv')

with open(budget_csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

print("Header: {}".format())


# In[15]:


pwd


# In[16]:


cd ..


# In[17]:


cd PyBank


# In[18]:


cd python-challenge


# In[19]:


cd PyBank


# In[81]:


import os
import csv

budget_csv_path = os.path.join('..', 'PyBank', 'budget_data.csv')

#create lists for each column
months = []
revenue =[]
monthly_change = []
total_change_profits = []

total_months = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

#pass 'r' to read a file
with open(budget_csv_path, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))
        
        total_months = total_months + 1
#print(str(total_months))
        
        total_profit = total_profit + int(row[1])
#print(total_profit)
        
        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit
        
#store monthly changes in a list
        
        monthly_change.append(monthly_change_profits)
        
        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit
        
#averagechangeinprofit

        average_change_profit = (total_change_profits/total_months)
    
#max and min and corresponding dates

        greatest_increase_profits = max(monthly_change)
        greatest_decrease_profits = min(monthly_change)
        
        increase_date = months[monthly_change.index(greatest_increase_profits)]
        decrease_date = months[monthly_change.index(greatest_decrease_profits)]

        print('')
        print('Financial Analysis')
        print('..................')
        print('')
        print("Total Months: " + str(total_months))
        print("Total Profits: " + "$" + str(total_profit))
        print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
        print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
        
#pass 'w' to write a file        
    with open('financial_analysis.txt', 'w') as text: 
        text.write('\n')
        text.write('Financial Analysis' + "\n")
        text.write('..................\n')
        text.write('\n')
        text.write("Total Months: " + str(total_months) + "\n")
        text.write("Total Profits: " + "$" + str(total_profit) + "\n")
        text.write('\n')
        text.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
        text.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")\n")
        


# In[ ]:





# In[ ]:




