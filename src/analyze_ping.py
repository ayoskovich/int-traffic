#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import re
from statsmodels.tsa import stattools
from IPython.display import HTML
import datetime
import seaborn as sns

pd.set_option('max_colwidth', 1000)

get_ipython().run_line_magic('run', './ping_helps.ipynb')

clean = read_all()

clean['hour'] = clean['tstamp'].apply(lambda x: x.hour)
clean['minute'] = clean['tstamp'].apply(lambda x: x.minute)
clean['second'] = clean['tstamp'].apply(lambda x: x.second)


# In[2]:


sf = clean.groupby('hour')['lat'].describe().rename(columns={'75%':'sf'})['sf']
above_q = clean.merge(sf.to_frame(), how='left', on='hour').query('lat > sf')
clean.groupby('hour')['lat'].describe()


# In[3]:


plt.rc('font', size=20)
plt.figure(figsize=(15,8))
ax = sns.boxplot(x="hour", y="lat", data=clean, showfliers=False);
#plt.title('Internet speed to google.com over time.')
plt.xlabel('');
plt.ylabel('')
ax.set_yticklabels([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_xticks([])
plt.savefig('/home/anthony/personalSite/content/project/internet-traffic/featured.jpg')


# In[4]:


# See docs for whisker ending point (default 1.5 of iqr)
# https://seaborn.pydata.org/generated/seaborn.boxplot.html
plt.rc('font', size=20)
plt.figure(figsize=(15,8))
ax = sns.boxplot(x="hour", y="lat", data=clean, showfliers=False);
plt.title('Internet speed to google.com over time.')
plt.xlabel('Hour');
plt.ylabel('Ping (milliseconds)');


# In[5]:


plt.rc('font', size=20)
plt.figure(figsize=(15,8))
ax = sns.boxplot(x="hour", y="lat", data=above_q, showfliers=False);
plt.title('Top of distribution.')
plt.xlabel('Hour');
plt.ylabel('Ping (milliseconds)');


# In[ ]:




