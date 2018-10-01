# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 00:05:27 2018

@author: maref
"""
s = 'slivajuzirzoxt'


maxString = s[0]
tempString = s[0]
for i in range(1,len(s)):
    if s[i] >= tempString[-1]:
        tempString += s[i]
        if len(tempString) > len(maxString):
            maxString = tempString
    else:
        tempString = s[i]
print("Longest substring in alphabetical order is: {}".format(maxString))