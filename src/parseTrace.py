#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import csv
from functools import reduce
from datetime import datetime

get_ipython().run_line_magic('run', './trace_helps.ipynb')

with open('FT2.TXT') as f:
    reader = csv.reader(f, delimiter='\n')
    dat = []
    a = []
    for row in reader:
        if row != []:
            a.extend(row)
        elif row == []:
            dat.append(a)
            a = []

al = []
for i, x in enumerate(dat):
    if is_norm(x):
        al.append(clean_dat(x, i))

full = pd.concat(al)
full


# In[ ]:




