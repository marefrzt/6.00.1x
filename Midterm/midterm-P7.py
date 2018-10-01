# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 21:21:57 2018

@author: maref
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    
    def valorX(x):
        soma = 0
        for index in range(0,len(L)):
            K = (len(L)-1) - index
            soma += (L[index] * (x**K))
        return soma
    return valorX

print(general_poly([1, 2, 3, 4])(10))
            
    
    
    
    







# K é o len da lista ou K = len(L)   
            