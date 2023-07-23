=>intially take first=-1 and last=-1
=> first find first occurence after 
=>second step find last occurence of an element 
=>third subtract lastoccurence -first occurence 
=>if first and last==-1 no element
=>if first==last one lement 
=>else last-first+1 
  ----------------------------------------------------------*code*-----------------------------------------------------------------------------------------------------------
   # Your code goes here
    first=-1
    last=-1
    low=0
    high=n-1 
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            first=mid 
            high=mid-1 
        elif arr[mid]>x:
            high=mid-1 
        else:
            low=mid+1 
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            last=mid 
            low=mid+1 
        elif arr[mid]>x:
            high=mid-1 
        else:
            low=mid+1 
    if first==-1 and last==-1:
        return 0 
    elif first==last:
        return 1
    else:
        return last-first+1
                     
