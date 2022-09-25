#!/usr/bin/env python
# coding: utf-8

# In[12]:


data=[8,6,1,10,5,3,9,2,7,4]
def quicksort(data,left,right):
    if left>=right:
        return
    i=left
    j=right
    key=data[left]
    while(i!=j):
        while data[j]>key and i<j:
            j-=1
        while data[i]<=key and i<j:
            i+=1
        
        if i<j:
            data[i],data[j]=data[j],data[i]
    data[left]=data[i]
    data[i]=key
    
    quicksort(data,left,i-1)
    quicksort(data,i+1,right)
    
quicksort(data,0,len(data)-1)
print(data)

        


# In[ ]:




