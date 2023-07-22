******************FINDING LOWER BOUND USING BINARYSEARCH ***********************************
SAMPLE TESTCASES:
link:https://www.codingninjas.com/studio/problems/lower-bound_8165382?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
code i did:
-------------------------------------------------------------------------------------------------------------------------------------
def lowerBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    low=0
    high=len(arr)-1
    ans=-1
    while low<=high:
        mid=(low+high)//2 
        if arr[mid]==x:
            ans=mid 
            break
        elif arr[mid]>x:
            high=mid-1 
        else:
            low=mid+1 
    if ans==-1:
        if arr[mid]>x:
            return mid
        else:
            return mid+1
    elif mid+1<len(arr)-1:
        return mid 
------------------------------------------------------------------------------------------------------------------------------------------------------
simple code:
-----------------------------------------------------------------------------------------------------------------------------------------------------
def lowerBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    s = 0
    e = n-1

    ans = n
    while s<=e:
        mid = s + (e-s)//2

        if arr[mid]>=x:
            ans = mid
            e = mid-1
        elif arr[mid] < x:
            s = mid + 1
        else:
            e = mid - 1
    return ans
    
    
