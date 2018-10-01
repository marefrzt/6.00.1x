# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 21:59:12 2018

@author: maref
"""



balance = 3926
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12.0
minimumFixedMonthlyPayment = 0
initialBalance = balance
 
while (balance > 0):
    balance = initialBalance
    minimumFixedMonthlyPayment = minimumFixedMonthlyPayment + 10
    for month in range(12):
       unpaidBalance = balance - minimumFixedMonthlyPayment
       interest = unpaidBalance * monthlyInterestRate
       balance = unpaidBalance + interest
       balance = round(balance, 2)
        
print ("Lowest Payment: ", minimumFixedMonthlyPayment) 