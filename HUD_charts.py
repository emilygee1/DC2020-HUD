
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel('Data_Level2_HUD_HUDPrograms_2009.xlsx')


race = df['HEAD_RACE_CD'].value_counts(normalize=True) * 100

print(race)
plt.pie(race, pctdistance=2, autopct='%1.01f%%')
plt.legend(labels=race.keys(), bbox_to_anchor=(-0.1, 1.),fontsize=8)
plt.show()



race = df['pgm_type_edited'].value_counts(normalize=True) * 100

print(race)
plt.pie(race, pctdistance=2, autopct='%1.01f%%')
plt.legend(labels=race.keys(), bbox_to_anchor=(-0.1, 1.),fontsize=8)
plt.show()



df = pd.read_excel('Data_Level2_HUD_HUDPrograms_2014.xlsx')


race = df['HEAD_RACE_CD'].value_counts(normalize=True) * 100

print(race)
plt.pie(race, pctdistance=2, autopct='%1.01f%%')
plt.legend(labels=race.keys(), bbox_to_anchor=(-0.1, 1.),fontsize=8)
plt.show()


# In[115]:


race = df['pgm_type_edited'].value_counts(normalize=True) * 100

print(race)
plt.pie(race, pctdistance=2, autopct='%1.01f%%')
plt.legend(labels=race.keys(), bbox_to_anchor=(-0.1, 1.),fontsize=8)
plt.show()




df = pd.read_excel('Data_Level2_HUD_HUDPrograms_2018.xlsx')




race = df['HEAD_RACE_CD'].value_counts(normalize=True) * 100

print(race)
plt.pie(race, pctdistance=2, autopct='%1.01f%%')
plt.legend(labels=race.keys(), bbox_to_anchor=(-0.1, 1.),fontsize=8)
plt.show()


race = df['pgm_type_edited'].value_counts(normalize=True) * 100

print(race)
plt.pie(race, pctdistance=2, autopct='%1.01f%%')
plt.legend(labels=race.keys(), bbox_to_anchor=(-0.1, 1.),fontsize=8)
plt.show()

