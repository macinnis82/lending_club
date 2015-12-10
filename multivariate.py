# -*- coding: utf-8 -*-
"""
Created on Wed Dec 09 20:42:55 2015

@author: Administrator
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm

loanStats = pd.read_csv('LoanStats3c.csv', skiprows=1, low_memory=False)

 # pull a subset of only attributes used in model
df = pd.DataFrame(columns=['Interest.Rate', 'Annual.Income', 'Home.Ownership'])
df['Interest.Rate'] = loanStats.int_rate
df['Annual.Income'] = loanStats.annual_inc.astype(float)
df['Home.Ownership'] = loanStats.home_ownership

print 'Cleaning the data ...'

 # drop rows with missing data
df.dropna(inplace=True)

 # strip percent signs in int_rate and convert to float
#loanStats['int_rate'] = loanStats['int_rate'].map(lambda \
#    x: round(float(x.rstrip('%')) / 100, 4))
df['Interest.Rate'] = df['Interest.Rate'].map(lambda x: str(x).rstrip('%'))
df['Interest.Rate'] = df['Interest.Rate'].astype(float)  

 # Create an Intercept
#df['Intercept'] = float(1.0)

print 'Building Model #1 ...'

 # The dependent variable
y = np.matrix(df['Interest.Rate']).transpose()
 # The independent variable
x = np.matrix(df['Annual.Income']).transpose()

X = sm.add_constant(x)
model1 = sm.OLS(y, X).fit()

print '=============================================================================='
print '                                 MODEL #1                                      '
print '=============================================================================='
print model1.summary()

print 'Building Model #2 ...'

df['Home.Ownership'] = pd.Categorical(df['Home.Ownership']).codes

# The dependent variable
y = np.matrix(df['Interest.Rate']).transpose()
 # The independent variables
x1 = np.matrix(df['Annual.Income']).transpose()
x2 = np.matrix(df['Home.Ownership']).transpose()

x = np.column_stack([x1, x2])

X = sm.add_constant(x)
model2 = sm.OLS(y, X).fit()

print '=============================================================================='
print '                                 MODEL #2                                      '
print '=============================================================================='
print model2.summary()

print 'Building Model #3 ...'

df['Interaction'] = df['Annual.Income'] * df['Home.Ownership']

# The dependent variable
y = np.matrix(df['Interest.Rate']).transpose()
 # The independent variables
x1 = np.matrix(df['Annual.Income']).transpose()
x2 = np.matrix(df['Home.Ownership']).transpose()
x3 = np.matrix(df['Interaction']).transpose()

x = np.column_stack([x1, x2, x3])

X = sm.add_constant(x)
model3 = sm.OLS(y, X).fit()

print '=============================================================================='
print '                                 MODEL #3                                      '
print '=============================================================================='
print model3.summary()
