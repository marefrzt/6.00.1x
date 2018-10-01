# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 18:54:09 2018

@author: maref
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    prod = []
    for i in range(len(listA)):
        prod.append(listA[i]*listB[i])
    soma = sum(prod)
    return(soma)

listA = [1, 2, 3]
listB = [4, 5, 6]
    
dotProduct(listA, listB)
