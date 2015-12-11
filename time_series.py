# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:13:50 2015

@author: Administrator
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as api

df = pd.read_csv('LoanStats3c.csv', header=1, low_memory=False)

# converts string to datetime using pandas
df['issue_d_format'] = pd.to_datetime(df['issue_d'])
dfts = df.set_index('issue_d_format')
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']

plt.plot(loan_count_summary)
plt.show()

#ACF plot
api.graphics.tsa.plot_acf(loan_count_summary)

#PACF plot
api.graphics.tsa.plot_pacf(loan_count_summary)