# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 23:05:26 2018

@author: maref
"""

balance = 3329
annualInterestRate = 0.2
minimumFixedMonthlyPayment = 10
monthlyInterestRate = annualInterestRate/12.0
updatedMonthlyBalance = 3329
finalBalance = 3329


while (finalBalance > 0):
    updatedMonthlyBalance = balance
    for month in range(12):
        unpaidBalance = updatedMonthlyBalance - minimumFixedMonthlyPayment
        interest = unpaidBalance * monthlyInterestRate
        updatedMonthlyBalance = unpaidBalance + interest
    finalbalance = updatedMonthlyBalance
print (minimumFixedMonthlyPayment)