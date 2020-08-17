#!/usr/bin/env python
# coding: utf-8

# In[1]:


def group_block(df, g_var, x_var, bins):
    """
    params:
        g_var (string or list of strings): Grouping variable
        x_var (string): Target variable to bin
        bins (np.arange): Bins to group x_var into
        
    returns (Series):
        
    """
    return (
        df.groupby(g_var)[x_var]
             .apply(lambda x: 
                     pd.cut(x, bins=bins)
                       .value_counts(sort=False, normalize=True)
                     )
    )

