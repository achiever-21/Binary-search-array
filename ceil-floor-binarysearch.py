from os import *
from sys import *
from collections import *
from math import *

def ceilingInSortedArray(n, x, arr):
    # Write your code here.
    floor=-1
    ceil=-1
    arr.sort()
    low=0
    high=len(arr)-1 
    while low<=high:
        mid=(low+high)//2 
        if arr[mid]==x:
            ceil=arr[mid] 
            floor=arr[mid]
            break
        elif arr[mid]>x:
            ceil=arr[mid]
            high=mid-1
        else:
            low=mid+1
            floor=arr[mid]
    print(floor,end=" ")
    return ceil
    
