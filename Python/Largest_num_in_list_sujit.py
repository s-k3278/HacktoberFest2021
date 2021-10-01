#!/usr/bin/env python
# coding: utf-8

# In[9]:


myList = list()
n = int(input("Enter the size of list"))
for i in range(n):
    a = int(input("enter numbers for the list: "))
    myList.append(a)

a = max(myList)
print("biggest number in the list is:", a)


# In[ ]:




