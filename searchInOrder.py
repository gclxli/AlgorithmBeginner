# -*- coding: utf-8 -*-
"""
Author:Sara Li

This file integrated a series of searching algorithm


"""
import math 

#find d in lst if d exists, return index; else: return len(lst)+1
#sequently searching
def search(d,lst):
    i = 0
    lst.append(d) #guard
    while(d != lst[i]):
        i = i+1
    
    return i            
      
#binary search 
def bisearch(d,lst):
    size = len(lst)
    index = size + 1
    left = 0
    if (size > 0):
        right = size-1
    else:
        print("Input is empty.")
        return index
    middle = math.floor((right-left)*0.5)
    while(left+1 != right):        
        if(d > lst[middle]):
            left = middle
            middle = math.ceil((right+left)*0.5)
        elif(d < lst[middle]):
            right = middle
            middle = math.floor((right+left)*0.5)
        else:
            index = middle
            break
    return index
    
    
    
    
    
lst = [1,4,9,11,25,100]
i = search(11,lst)
index = bisearch(24,lst)