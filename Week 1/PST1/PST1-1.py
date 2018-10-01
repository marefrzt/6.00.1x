# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 00:04:02 2018

@author: maref
"""
s = 'mlkgvkuvxfoexofupimotaa'

vowelsCount = 0
letter_list = list(s)
for letter in letter_list:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
       vowelsCount = vowelsCount + 1 
print('Number of vowels:',vowelsCount) 