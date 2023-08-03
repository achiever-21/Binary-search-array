You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.
input:Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Approach 1: we can simply use for loop and compare elements and we can check but time compelxiy :O(N)
Approach2 :by using Xor .xor of to same numbers is  0. xor of 0 and num == num .by using technique we can traverse the array find xor of all elemnet eturn the xor which gives single ele present in it 
Approach 3: we know that array indexing start from even.if even pos ele == odd pos ele then we can say that 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
code:
------
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        elif nums[0]!=nums[1]:
            return nums[0]
        elif nums[-1]!=nums[-2]:
            return nums[-1]
        low=0
        high=len(nums)-2
        while low<=high:
            mid=(low+high)//2 
            if nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]:
                return nums[mid]
            elif mid % 2==0 and nums[mid]==nums[mid+1] or (mid-1)%2==0 and nums[mid]==nums[mid-1]:
                low=mid+1 
            elif mid%2==1 and nums[mid]==nums[mid+1] or (mid-1)%2==1 and nums[mid]==nums[mid-1] :
                high=mid-1 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
code:
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                right = mid
            else:
                left = mid + 2
        return nums[left]
