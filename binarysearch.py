***BINARY SEARCH**
the main use of binary search is timecomplexity it is the only algo which decrease time to search an ele in array 
*********************************************************
          ****CoDe********
********************************************************
normal approach:
def search(nums: [int], target: int):
    # Your code goes here
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2 
        if nums[mid]==target:
            return mid 
        elif nums[mid]>target:
            high=mid-1 
        else:
            low=mid+1 
    return -1
*************************************************************************************
********************************************************************************************
RECURSION APPROACH:
--------------------------------------------------------------
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary(nums,0,len(nums)-1,target)
    def binary(self,nums,low,high,target):
        if low>high:
            return -1 
        mid=(low+high)//2 
        if nums[mid]==target:
            return mid 
        elif nums[mid]>target:
            return self.binary(nums,low,mid-1,target)
        else:
            return self.binary(nums,mid+1,len(nums)-1,target)
  ------------------------------------------------------------------------------------------------------------------------------------------------
