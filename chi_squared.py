# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 10:42:45 2015

@author: Administrator
"""

from scipy import stats
import collections
import pandas as pd
import matplotlib.pyplot as plt

 # Loads the Lending Club data
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

 # Clean data
loansData.dropna(inplace=True)

 # Creates a collection
freq = collections.Counter(loansData['Open.CREDIT.Lines'])
print freq

 # Bar Chart
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()

 # Chi-Squared Test
chi, p = stats.chisquare(freq.values())
print chi
print p