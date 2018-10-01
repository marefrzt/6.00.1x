# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 19:17:40 2018

@author: maref
"""

countBob = 0
s = "azcbobobegghakl"
for i in range(len(s)):
    substring = s[i:i+3]
    if substring == 'bob' :
         countBob += 1
print('Number of times bob occurs is:',countBob) 