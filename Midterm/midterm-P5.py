# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:41:01 2018

@author: maref
"""

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
    inverse = {}
    for key,value in d.items():
        if not value in inverse:
            inverse[value] = []
        inverse[value].append(key)
        inverse.get(value).sort()
    
    return inverse

d = {8: 6, 2: 6, 4: 6, 6: 6}
print(dict_invert(d))
