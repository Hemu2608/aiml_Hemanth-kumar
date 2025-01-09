#!/usr/bin/env python
# coding: utf-8

# In[1]:


def mean_value(*n):
    sum = 0
    counter = 0
    for x in n:
        counter = counter +1
        sum += x
    mean = sum/counter
    return mean


# In[2]:


mean_value(3,4,5,6,7,8,1,2)

