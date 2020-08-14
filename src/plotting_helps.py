#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def draw_split(var, val, perc, dat):
    """ Draw the split plot. 
    
    var: Categorical variable to check against percentile
    val: Quantitative variable to plot on yaxis of boxplots
    perc: Percentile to break the axis on
    """
        
    # Compute is above
    dat['is_above'] = (
        dat
        .groupby(var)[val]
        .apply(lambda x: is_above(x, perc))
        .values
    )
    
    
    # Draw plot
    g = (
        sns.FacetGrid(dat, row="is_above", 
        height=3, aspect=4, 
        sharex=True, sharey=False,
        row_order=[True, False])
    );
    
    (
        g.map(sns.boxplot, var, val, 
              showfliers=False, 
              order=set(clean[var]))
        .set_titles("Above 75: {row_name}")
    );
    
    dat.drop(columns=['is_above'], inplace=True)

