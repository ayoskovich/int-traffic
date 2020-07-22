#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import matplotlib.pyplot as plt
import re
from statsmodels.tsa import stattools
from IPython.display import HTML
import datetime

pd.set_option('max_colwidth', 1000)

get_ipython().run_line_magic('run', './ping_helps.ipynb')

clean = read_all()

clean['hour'] = clean['tstamp'].apply(lambda x: x.hour)
clean['minute'] = clean['tstamp'].apply(lambda x: x.minute)
clean['second'] = clean['tstamp'].apply(lambda x: x.second)


# In[43]:


clean.groupby('hour')['lat'].describe()


# In[ ]:




