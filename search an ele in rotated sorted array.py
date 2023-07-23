brute force:linearsearch
optimised approach:
we know this is a half sorted array means half part and half part sorted
=>first step by using same binary search but here we have to first find sorted part and check the key is present in it or not else then we change our lowor high positions
=>if first part is not sorted then come to second part and check it is sorted or not if it is then key is present in it or not else find it another
=>if key is not in that again change the postions of low and high 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
code:
------------------------------------------------------
from os import *
from sys import *
from collections import *
from math import *

def search(arr, n, k):
	low=0
	high=n-1
	while low<=high:
		mid=(low+high)//2
		if arr[mid]==k:
			return mid 
		elif arr[low]<=arr[mid]:
			if arr[low]<=k and arr[mid]>=k:
				high=mid-1
			else:
				low=mid+1 
		else:
			if arr[mid]<=k and arr[high]>=k:
				low=mid+1
			else:
				high=mid-1 
	return -1

	
