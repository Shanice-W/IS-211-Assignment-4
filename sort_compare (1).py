#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import random


# In[36]:


def insertion_sort(a_list): 
    for index in range(1, len(a_list)):
        start = time.time()
        current_value = a_list[index] 
        position = index

        while position > 0 and a_list[position - 1] > current_value: 
            a_list[position] = a_list[position - 1] 
            position = position - 1
            a_list[position] = current_value
            end = time.time()
        return end-start, a_list


# In[30]:


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        pos = i
        
        while pos >= gap and a_list[pos - gap] > current_value:
            a_list[pos] = a_list[pos - gap]
            pos = pos - gap
            a_list[pos] = current_value


# In[31]:


def shell_sort(a_list):
    start = time.time()
    sublist_count = len(a_list) // 2 
    
    while sublist_count > 0: 
        for start_position in range(sublist_count): 
            gap_insertion_sort(a_list, start_position, sublist_count)
            end = time.time()
    return end-start, a_list


# In[32]:


def python_sort(a_list):
    start = time.time()
    a_list = a_list.sort()
    end = time.time()
    return end-start, a_list


# In[33]:


def random_list(maxval):
     test_list = []
    
for item in range(maxval):
    test_list.append(random.test_list(1,maxval))
return test_list


# In[34]:


test_numbers = [500,1000,10000]
for items in test_numbers:
    counter = 100
    result = [0,0,0]
    
    while counter > 0:
            test_list = random_list(items)
            result=result
            result[0] += insertion_sort(test_list)[0]
            result[1] += shell_sort(test_list)[0]
            result[2] += python_sort(test_list)[0]
            counter -= 1


# In[ ]:




