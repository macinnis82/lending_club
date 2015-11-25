# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 10:20:19 2015

@author: Administrator
"""

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

 # Clean data
loansData.dropna(inplace=True)

 # Boxplot
loansData.boxplot(column='Amount.Requested')
plt.show()
plt.savefig("boxplot.png")

 # Histogram
loansData.hist(column='Amount.Requested')
plt.show()
plt.savefig("histogram.png")

 # QQ Plot
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()
plt.savefig("qqplot.png")

"""
The results are pretty close to the graphs generated
when looking at the Amount.Funded.By.Investors column
"""