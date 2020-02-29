import statistics as stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load datasets for 2009, 2014, 2018
df09 = pd.read_excel('~/Downloads/HUD/data/Data_Level2_HUD_HUDPrograms_2009.xlsx')
df14 = pd.read_excel('~/Downloads/HUD/data/Data_Level2_HUD_HUDPrograms_2014.xlsx')
df18 = pd.read_excel('~/Downloads/HUD/data/Data_Level2_HUD_HUDPrograms_2018.xlsx')

df_list = [df09, df14, df18]

for df in df_list:
    df = df.drop(['HEAD_ID',
                'ADLT_AGE_18_21_CNT',
                'ADLT_AGE_22_25_CNT',
                'ADLT_AGE_26_35_CNT',
                'ADLT_AGE_36_49_CNT',
                'ADLT_AGE_50_61_CNT',
                'ADLT_AGE_62_85_CNT',
                'ADLT_AGE_ABOVE85_CNT',
                'CHLDRN_AGE_0_3_CNT',
                'CHLDRN_AGE_4_5_CNT',
                'CHLDRN_AGE_6_12_CNT',
                'CHLDRN_AGE_13_17_CNT',
                'H6_CD',
                'total_annl_incm_amnt_rounded',
                'gross_rent_amnt_rounded',
                'asstn_pymnt_amnt_rounded',
                'total_fmly_crbtn_amnt_rounded'],
               axis =1)

df09.describe()
df14.describe()
df18.describe()



# Load 2018 datasets for each program type
df1 = pd.read_excel('~/Downloads/HUD/data/HUD_Type1_2018.xlsx')
df2 = pd.read_excel('~/Downloads/HUD/data/HUD_Type2_2018.xlsx')
df3 = pd.read_excel('~/Downloads/HUD/data/HUD_Type3_2018.xlsx')

df1 = df1.drop(['Year',
                'H6_CD',
                'total_annl_incm_amnt_rounded',
                'gross_rent_amnt_rounded',
                'asstn_pymnt_amnt_rounded',
                'total_fmly_crbtn_amnt_rounded'],
               axis =1)
df2 = df2.drop(['Year',
                'H6_CD',
                'total_annl_incm_amnt_rounded',
                'gross_rent_amnt_rounded',
                'asstn_pymnt_amnt_rounded',
                'total_fmly_crbtn_amnt_rounded'],
               axis =1)
df3 = df3.drop(['Year',
                'H6_CD',
                'total_annl_incm_amnt_rounded',
                'gross_rent_amnt_rounded',
                'asstn_pymnt_amnt_rounded',
                'total_fmly_crbtn_amnt_rounded'],
               axis =1)


df1.describe()
df2.describe()
df3.describe()



# Closer look at some significant predictors

df_list2 = [df1, df2, df3]
variables = ['HEAD_ELDLY_INDR', 'HEAD_GNDR_CD', 'HEAD_RACE_CD', 'CNTRL_CITY_CD']
program_types = ['Public housing', 'Housing choice voucher', 'Multi-family']
i = 0

for df in df_list2:
    print(program_types[i])
    for var in variables:
        print(df[var].value_counts(normalize=True), end ='\n\n')

    med_hispanic = df['HISPANIC_PRCNT'].median()
    print('Median Hispanic Percentage: %.2f' % med_hispanic, end = '\n\n\n')
    i += 1
