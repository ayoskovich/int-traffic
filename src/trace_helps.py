#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def is_norm(tr):
    """ Checks if traceroute was parsed normally. """
    return len(tr) == 19


def make_dict(x):
    """ Create a dictionary from a list """
    if len(x) > 2: raise Exception('Was only expecting 2 elements')

    i = iter(x)
    b = dict(zip(i, i))
    
    return b


def strip_time(time):
    """ Parses the time string from the traceroute log"""
    return datetime.strptime(time, "%m/%d/%y %H:%M:%S")


def get_secs(start, end):
    """ Convert time into seconds. """
    return (end - start) / np.timedelta64(1, 's')

    
def has_asty(trace_line):
    """ Lines with asterisks need special care. """
    return "*" in trace_line


def parse_entry(ent, wuw):
    """ Parse a single line of a traceroute.
    
    Example of a good one:
        '192.168.1.254 1.225ms 6.106ms 1.608ms'
        
    Examples of a bad one:
        '*  *  *'
        
    Params:
        ent (string): the entry
        wuw (string): [ip or times] which part to pull out
    """
    if has_asty(ent):
        pass  # Entry has * * * and is messed up
    else:
        BODY = ent.split(' ')
        times = [float(x.replace('ms', '')) for x in BODY if 'ms' in x]
        ip = BODY[0]
        ret = {'ip': ip, 'times': times}
        return ret[wuw]


def clean_dat(dat, i):
    """ Parse the entry of traceroute
    
    Params:
        dat (string): entire entry of traceroute 
        i (int): ID for traceroute 
    """
    START = strip_time(dat[0].replace('start: ', ''))
    END = strip_time(dat[18].replace('end: ', ''))
    
    WHERE_TO = dat[1] # 'Destination: traceroute to google.com (216.58.194.142) 64 hops max'
    
    CHUNK = dat[2:18]  # Inner block of the trace
    
    split_up = [x.split('   ') for x in CHUNK]
    result_dict = reduce(lambda a, b: {**a, **b}, [make_dict(x) for x in split_up])
    
    df = pd.DataFrame.from_dict(result_dict, orient='index').reset_index()
    df['start'] = START
    df['end'] = END
    df['whereto'] = WHERE_TO
    df.rename(columns={'index':'trace_line', 0:'trace_entry'}, inplace=True)

    cleaned = (
        df
        .assign(ip = df['trace_entry'].apply(lambda x: parse_entry(x, 'ip')))
        .assign(times = df['trace_entry'].apply(lambda x: parse_entry(x, 'times')))  
    )
    cleaned['trace_id'] = i
    
    return cleaned


def post_process(df):
    """ Clean up data types and compute some variables once
    individual traceroutes are stacked.
    """
    df = df.explode('times')
    
    df['times'] = df['times'].astype(float)
    
    df['n_seconds'] = (df['end'] - df['start']) /  np.timedelta64(1, 's')
    
    return df

