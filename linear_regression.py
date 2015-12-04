# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:57:29 2015

@author: Administrator
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#print loansData['Interest.Rate'][0:5]
#print loansData['Loan.Length'][0:5]
#print loansData['FICO.Range'][0:5]

"""
Interest Rate Lambda
Strip the %
convert to a number
convert to a decimal
Round to 4/5 digits
"""
#x = loansData['Interest.Rate'][0:5].values[1]
#x = x.rstrip('%')
#x = float(x)
#x = x / 100
#x = round(x, 4)
#print x
#y = lambda x: round(float(x.rstrip('%')) / 100, 4)

cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['Interest.Rate'] = cleanInterestRate

"""
Loan Length Lambda
Strip the word month from end
Convert to integer
"""
#x = loansData['Loan.Length'][0:5].values[1]
#x = x.rstrip(' months')
#x = int(x)
#print x
#print type(x)
#y = lambda x: int(x.rstrip(' months'))

cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))
loansData['Loan.Length'] = cleanLoanLength

"""
FICO Range Lambda
Convert values to string
Split strings into 2 numbers
Select the first number - [0] index
"""
#x = loansData['FICO.Range'][0:5].values[1]
#x = x.split('-')
#x = [int(n) for n in x]
#cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-'))
#cleanFICORange = cleanFICORange.map(lambda x: [int(n) for n in x])
#print cleanFICORange[0:5]
#print type(cleanFICORange[0:5].values[0][0])

#loansData['FICO.Range'] = cleanFICORange
#loansData['FICO.Score'] = loansData['FICO.Range'].values[0][0]
#x = [val[0] for val in loansData['FICO.Range']]

loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x: x.split('-'))
loansData['FICO.Score'] = loansData['FICO.Score'].map(lambda x: int(x[0]))


 # Plot Histogram of FICO Scores
plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()

 # Generate a Scatter Plot matrix
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.show()

#InterestRate = b + a1(FICOScore) + a2(LoanAmount)
intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

 # The dependent variable
y = np.matrix(intrate).transpose()
#print y
 # The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()
#print x1
#print x2

 # Create an input matrix
x = np.column_stack([x1,x2])
#print x

 # Create a linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()
#print f

 # Output the results summary
f.summary()

loansData.to_csv('loansData_clean.csv', header=True, index=False)