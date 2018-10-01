#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 19:37:14 2018

@author: mariannetine
"""

balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate/12.0

initialBalance = balance

#Bisection search parameters

lowerBound = balance/12
upperBound = (balance*(1+monthlyInterestRate)**12)/12.0
epsilon = 0.01

guess = (lowerBound + upperBound)/2

while True:
   for month in range(12):
      balance = balance - guess
      balance = balance + (monthlyInterestRate*balance)

   if (balance > epsilon):
      lowerBound = guess
      balance = initialBalance
   elif (balance < -epsilon):
      upperBound = guess
      balance = initialBalance
   else:
      print('Lowest payment: ',str(round(guess,2)))
      break

   guess = (lowerBound + upperBound)/2