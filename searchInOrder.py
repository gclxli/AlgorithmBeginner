# -*- coding: utf-8 -*-
"""
Author:Sara Li

This file integrated a series of searching algorithm 
with different interpolation rule


"""
import math 

#find d in lst if d exists, return index; else: return len(lst)+1
#sequently searching
def search(d,lst):
    i = 0
    lst.append(d)
    count = 1
    while(d != lst[i]):
        i = i+1
        count = count + 1 
    lst.pop()
    print("cycle count of sequently Search:{},index:{}".format(count,i))
    return i            

      
#binary search 
def bisearch(d,lst):
    size = len(lst)
    index = size
    left = 0
    count = 1
    
    if(size == 1):
       if(d == lst[0]):return 0
       if(d != lst[0]):return 1       
    elif(size > 1):
        right = size - 1
    else:
        print("Input is empty.")
        return index
    
    middle = math.floor((right-left)*0.5)
    while(left < right): 
        count = count + 1 
        if(d > lst[middle]):
            left = middle
            middle = math.ceil((right+left)*0.5)
        elif(d < lst[middle]):
            right = middle
            middle = math.floor((right+left)*0.5)
        else:
            index = middle
            break
    print("cycle count of binary Search:{},index:{}".format(count,index))
    return index
    
    
#interpolation search
#fit for meanly distributed data
def interpoSearch(d,lst):
    size = len(lst)
    index = size
    left = 0
    count = 1
    if(size == 1):
       if(d == lst[0]):return 0
       if(d != lst[0]):return 1       
    elif(size > 1):
        right = size - 1
    else:
        print("Input is empty.")
        return index
    interp = math.floor(left+(right-left)*(d-lst[left])/(lst[right]-lst[left]))
    while(left < right): 
        count = count + 1 
        if(d > lst[interp]):
            left = interp
            interp = math.ceil(left+(right-left)*(d-lst[left])/(lst[right]-lst[left]))
        elif(d < lst[interp]):
            right = interp
            interp = math.floor(left+(right-left)*(d-lst[left])/(lst[right]-lst[left]))
        else:
            index = interp
            break    
    print("cycle count of interpoSearch:{},index:{}".format(count,index))
    return index  


def Fibonacci(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

#fit for searching data locating in the middle 
def Fibonacci_Search(d,lst):
    size = len(lst)
    index = size
    left = 1
    right = 0
    count = 1
    
    if(size == 1):
       if(d == lst[0]):return 0
       if(d != lst[0]):return 1       
    elif(size > 1):
        right = size - 1
    else:
        print("Input is empty.")
        return index
    
    k = 0
    while(right>Fibonacci(k)):
        k = k + 1
    
    extra = Fibonacci(k) - right
    while(extra != 0):
        lst.append(lst[right])
        extra = extra - 1

    temp = k
    while(left <= Fibonacci(temp) and right >= 0):
        mid = left + Fibonacci(k-1) - 1
        if(d < lst[mid]):
            right = mid - 1
            k = k - 1
        elif(d > lst[mid]):
            left = mid + 1
            k = k - 2
        else:
            if(mid >= size):
                index = size
                break
            else:
                index = mid
                break
        count = count + 1 
    
    extra = Fibonacci(temp) - size + 1
    while(extra != 0):
        lst.pop()
        extra = extra - 1
        
    print("cycle count of FibonacciSearch:{},index:{}".format(count,index))
    return index     

#lst is orderedly arranged    
#lst = [1,4,9,11,25,100]
lst = [0,1,16,24,35,47,59,62,73,88,99]
i = search(62,lst)
bindex = bisearch(62,lst)
index = interpoSearch(62,lst)    
findex = Fibonacci_Search(62,lst)
