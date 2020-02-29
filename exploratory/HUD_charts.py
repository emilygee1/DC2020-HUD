import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load datasets for 2009, 2014, 2018
df09 = pd.read_excel('Data_Level2_HUD_HUDPrograms_2009.xlsx')
df14 = pd.read_excel('Data_Level2_HUD_HUDPrograms_2014.xlsx')
df18 = pd.read_excel('Data_Level2_HUD_HUDPrograms_2018.xlsx')

df_list = [df09, df14, df18]

# Replace keys for race and program type with the actual names
for df in df_list:
    df['HEAD_RACE_CD'] = df['HEAD_RACE_CD'].replace({1:'White',
                                                    2:'Black',
                                                    3:'Native American',
                                                    4:'Asian',
                                                    5:'Hawaiian or Pacific Islander',
                                                    6:'More than one race'})
    df['pgm_type_edited'] = df['pgm_type_edited'].replace({1:'Public housing',
                                                          2:'Housing voucher',
                                                          3:'Multi-family'})

year = ['2009', '2014', '2018']
i = 0

# Pie charts to display program breakdown for each year
for df in df_list:    
    race = df['pgm_type_edited'].value_counts(normalize=True) * 100
    explode = (.1, 0, 0)
    plt.pie(race, explode = explode, pctdistance=2, autopct='%1.01f%%', shadow=True)
    plt.title('Breakdown by Program - ' + year[i])
    plt.legend(labels=race.keys(), bbox_to_anchor=(-0.1, 1.),fontsize=12)
    plt.show()
    i += 1

j = 0

# Pie charts to display race breakdown of head of households for each year
for df in df_list:    
    race = df['HEAD_RACE_CD'].value_counts(normalize=True) * 100
    explode = (.1, 0, 0, 0, 0, 0)
    plt.pie(race, explode = explode, pctdistance=2, autopct='%1.01f%%', shadow=True)
    plt.title('Breakdown by Race - ' + year[j])
    plt.legend(labels=race.keys(), bbox_to_anchor=(-0.1, 1.),fontsize=12)
    plt.show()
    j += 1
