#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def remove_headers(df):
    """ Remove the records when the ping command starts. """
    return df[df['a'].apply(lambda x: x[:4] != 'PING')]


def clean_time(time):
    """ Get to the right of time=, replace whitespace. """
    return float(re.sub('[\s|m|s]', '', time.split('time=')[1]))


def clean_ts(time):
    """Input is a string, cleaning. 
    
    >>> clean_ts('[1591899674.439142]')
    datetime.datetime(2020, 6, 11, 14, 21, 14, 439142)
    """
    return datetime.datetime.fromtimestamp(float(re.sub('[\[\]]', '', time)))


def parse_time(df):
    """ Grab the time of the ping and the amount of time 
    the ping took"""
    return (
        df
        .assign(tstamp = df.a.apply(lambda x: clean_ts(x[:19])))
        .assign(lat = df.b.apply(clean_time))
    )


def read_cleaned(n=100):
    return (
        pd.read_fwf('~/PING_LOG.txt', header=None, names=['a', 'b']).tail(n)
            .pipe(remove_headers)
            .pipe(parse_time)
            .drop(labels=['a', 'b'], axis=1)
    )

