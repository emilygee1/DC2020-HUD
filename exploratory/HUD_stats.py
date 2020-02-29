#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# Load datasets for each year
df = pd.read_excel('/Data_Level2_HUD_HUDPrograms_2009.xlsx')
df2 = pd.read_excel('/Data_Level2_HUD_HUDPrograms_2014.xlsx')
df3 = pd.read_excel('/Data_Level2_HUD_HUDPrograms_2018.xlsx')


# In[21]:


df_list = [df, df2, df3]


# In[22]:


# Rename some columns for ease of reading
for df in df_list:
    df.rename(columns={'TOTAL_ANNL_INCM_AMNT':'Income',
                      'MNRTY_PRCNT':'Minority Percentage',
                      'PVRTY_PRCNT':'Poverty Percentage',
                      'GROSS_RENT_AMNT':'Rent'},
             inplace=True)


# In[39]:


years = ['2009', '2014', '2018']
key_vars = ['Income', 'Rent', 'Minority Percentage', 'Poverty Percentage']


# In[42]:


i = 0

for df in df_list:
    
    print(years[i] + ' - Medians')
    
    for v in key_vars:
        med = df[v].median()
        
        if v in ['Income', 'Rent']:
            print(v + ': ${:,.2f}'.format(med))
        else:
            print(v + ': ' + str(med) + '%')
    
    print('\n')
    i += 1


# In[ ]:




