# -*- coding: utf-8 -*-
"""
Created on Tue Dec 01 10:26:09 2015

@author: Administrator
"""

import pandas as pd
import statsmodels.api as sm
import numpy as np

 # load the data
loansData = pd.read_csv('loansData_clean.csv')

#print loansData['Interest.Rate'][0:5]

 # Derived binary column contain logical 1 or 0
ir = loansData['Interest.Rate']
ir = [1 if x < 0.12 else 0 for x in ir]
loansData['IR_TF'] = ir

#print loansData['IR_TF'][0:5]
#print loansData[loansData['Interest.Rate'] == 10].head()
#print loansData[loansData['Interest.Rate'] == 13].head()

 # Create an intercept for statsmodels
loansData['Intercept'] = 1

ind_vars = ['Intercept', 'FICO.Score', 'Amount.Requested']

 # define logistic model
logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])

 # Fit the model
result = logit.fit()

 # get the fitted coefficients
coeff = result.params
#print coeff

"""
Intercept          -60.125045
FICO.Score           0.087423
Amount.Requested    -0.000174
"""

 # Logistic function
def logistic_function(FicoScore, LoanAmount, coeff):
    """ p(x) = 1/(1 + e^(intercept + 0.087423(FicoScore) − 0.000174(LoanAmount)) """
    p = 1 / (1 + np.exp(-(coeff[0] + (coeff[1]*FicoScore) + (coeff[2]*LoanAmount))))
    return p


def pred(FicoScore, LoanAmount, coeff):
    p = logistic_function(FicoScore, LoanAmount, coeff)
    if p >= 0.7:
        print "You will get the loan!"
    else:
        print "Sorry, please pay off current loans first!"
        
pred(850, 60000, coeff)