#!/usr/bin/env python
# coding: utf-8

# In[36]:


import time
import random


# In[37]:


def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    While pos <len (a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos +1
    end = time.time()
    return found, end-start


# In[38]:


def ordered_sequential_search(a_list, item):
    a_list.sort()
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
        else:
            pos = pos+1

    end = time.time()
    return found, end-start


# In[39]:


def binary_search_iterative(a_list, item):
    a_list.sort()
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found + True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
        else:
            first = midpoint + 1

    end = time.time()
    return found, end-start


# In[40]:


def another_list(maxval):
    another_list = ((xrange(1,maxval + 1)), maxval)

    return another_list


# In[41]:


def main():
    test_list = [500, 1000, 10000]
    for test in test_list:
        counter = 100
        result = [0,0,0,0]
        while counter >0:
            random_list = random_list(test)
            result[0] += sequential_search(random_list, -1)[0]
            result [1] += ordered_sequantial_search(random_list, -1)[0]
            result [2] += binary_search_iterative(random_list, -1)[0]
            result [3] += binary_search_recursive(random_list, -1)[0]
            counter -= 1


# In[42]:


print (For the list of []).format(test)
print (Sequential search took %10.7f seconds to run, on average) % (result[0] / 100)
print (Ordered sequential search took %10.7f seconds to run, on average) % (result[1] / 100)
print (Iterative binary search took %10.7f seconds to run, on average) % (result[2] / 100)
print (Recursive binary search took %10.7f seconds to run, on average) % (result[3] / 100)


# In[ ]:





# In[ ]:




