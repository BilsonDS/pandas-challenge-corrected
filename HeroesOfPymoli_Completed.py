#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[2]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# ## Player Count

# * Display the total number of players
# 

# In[3]:


purchase_data.count()


# In[4]:


purchase_data.head()


# In[5]:


player= len(purchase_data["SN"].value_counts())
player_count=pd.DataFrame([player], columns = ["total players "])
player_count


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[7]:


#unique items
unique_items = len(purchase_data["Item Name"].unique())

#avg price
avg_price = purchase_data["Price"].mean()


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[8]:


#gender count and percentage
gender = purchase_data[["SN", "Gender"]]

gender = gender.drop_duplicates()

counts = gender["Gender"].value_counts()

total_counts = [counts[0],counts[1],counts[2]]

percentage = [round((counts[0]/player)*100,2),round((counts[1]/player)*100,2),round((counts[2]/player)*100,2)]



# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[11]:


#gender purchase analysis
gender = purchase_data.groupby(["Gender"])

purchase_fig = gender["SN"].count()

purchase_price = gender["Price"].mean()

purchase_t = gender["Price"].sum()

purchase_gender = pd.DataFrame({"Purchase Count": purchase_fig, 
                               "Avg Purchase Price": purchase_price,
                               "Total Purchase Value": purchase_t})


purchase_gender


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[17]:


#create bins for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 34.90, 39.90, 44.90, 49.90, 54.90, 59.90, 64.90, 69.90, 74.90, 79.90, 84.90, 89.90, 9999]
age_category = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

#use pd.cut
purchase_data["Age Demographics"]= pd.cut(purchase_data["Age"], age_bins, labels=age_category)
age_group =purchase_data.groupby("Age Demographics")

purchase_data.head()


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[ ]:





# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[ ]:





# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[ ]:





# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[ ]:




