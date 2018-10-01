# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 23:52:55 2018

@author: maref
"""
varA = 1
varB = 1


if type(varA) is str or type(varB) is str:
    print("string involved")
elif varA > varB:
    print("bigger")
elif varA == varB:
    print("equal")
else:
    print("smaller")