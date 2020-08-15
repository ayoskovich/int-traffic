#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from statsmodels.tsa import stattools
from IPython.display import HTML
import datetime
import seaborn as sns

pd.set_option('max_colwidth', 1000)

get_ipython().run_line_magic('run', './ping_helps.ipynb')
get_ipython().run_line_magic('run', './plotting_helps.ipynb')

clean = read_all()

clean['hour'] = clean['tstamp'].apply(lambda x: x.hour)
clean['day'] =  clean['tstamp'].apply(lambda x: x.isoweekday())  # 1 is Monday


# In[2]:


# plt.rc('font', size=20)
# plt.figure(figsize=(15,8))
# ax = sns.boxplot(x="hour", y="lat", data=clean, showfliers=False);
# #plt.title('Internet speed to google.com over time.')
# plt.xlabel('');
# plt.ylabel('')
# ax.set_yticklabels([])
# ax.set_yticks([])
# ax.set_xticklabels([])
# ax.set_xticks([])
# plt.savefig('/home/anthony/personalSite/content/project/internet-traffic/featured.jpg')


# In[62]:


clean['dec'] = (
    clean.groupby('hour')['lat']
    #.apply(lambda x: pd.cut(x, bins=np.arange(0, 1100, 100)))
    .apply(lambda x: pd.cut(x, bins=np.arange(0, 1100, 50)))
    .astype('interval')
)

rels = clean.groupby('hour')['dec'].apply(lambda x: x.value_counts(sort=False, normalize=True))


# In[67]:


# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure
(
    rels[rels.index.get_level_values(None) == pd.Interval(0, 50)]
    .plot(use_index=False,
          title='Percentage of observations between 0 and 100 ms')
);
plt.ylabel('Percentage from 0 - 100');
plt.xlabel('Hour of the Day');
plt.xticks(np.arange(24), rels.index.levels[0]);
plt.ylim((0, 1));
plt.yticks(np.arange(0, 1, .1));
plt.gcf().set_figheight(5);
plt.gcf().set_figwidth(10);


# In[10]:


import math
clean['log'] = clean['lat'].apply(lambda x: math.log(x))
g = sns.FacetGrid(clean, col='hour', col_wrap=3, sharex=False, sharey=False, aspect=3);
g.map(plt.hist, 'lat');

