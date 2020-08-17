#!/usr/bin/env python
# coding: utf-8

# In[1]:


def bucket_dist(g_var, x_var, all_bins, tar_bin, label, df):
    """ Buckets and filters values.
    
    params:
        g_var (string): grouping variable
        x_var (string): variable to put in buckets
        all_bins (np.arange): Bins
        tar_bin (pd.Interval): Interval to grab
        label (string): Name for group assignment
        df (pd.DataFrame): Input dataframe
        
    returns (pd.DataFrame)
    """
    return (
        df.groupby(g_var)[x_var]
        .value_counts(normalize=True, bins=all_bins)
        [:, tar_bin]
        .to_frame()
        .assign(lev = label)
    )

