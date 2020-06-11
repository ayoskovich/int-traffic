#!/usr/bin/env python
# coding: utf-8

# In[99]:


import pandas as pd
import csv
from functools import reduce


def is_norm(tr):
    """ Checks if traceroute was parsed normally. """
    return len(tr) == 19

def makeDict(x):
    """ Create a dictionary from a list"""
    if len(x) > 2: raise Exception('Was only expecting 2 elements')
    i = iter(x)
    b = dict(zip(i, i))
    
    return b


with open('FT.TXT') as f:
    reader = csv.reader(f, delimiter='\n')
    dat = []
    a = []
    for row in reader:
        if row != []:
            a.extend(row)
        elif row == []:
            dat.append(a)
            a = []

r1 = dat[0]
dat[0]


# In[100]:


if is_norm(r1):
    START, END = r1[0], r1[18]
    WHERE_TO = r1[1]
    CHUNK = r1[2:18]
    print('Start: {}, \nEnd: {}, \nDestination: {}'.format(START, END, WHERE_TO))
CHUNK


# In[101]:


split_up = [x.split('   ') for x in CHUNK]
result_dict = reduce(lambda a, b: {**a, **b}, [makeDict(x) for x in split_up])
result_dict


# In[ ]:




