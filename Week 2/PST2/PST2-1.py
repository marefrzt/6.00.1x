# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 21:29:39 2018

@author: maref
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate/12.0


 
for month in range(12):
    minimumPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - minimumPayment
    interest = unpaidBalance * monthlyInterestRate
    balance = unpaidBalance + interest
    balance = round(balance, 2)
    
print ("Remaining balance: ", balance) 