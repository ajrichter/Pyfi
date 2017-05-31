
# coding: utf-8

# In[2]:

from quantopian.interactive.data.sentdex import sentiment


# In[3]:

from quantopian.pipeline.filters.morningstar import Q1500US


# In[4]:

type(sentiment)


# In[5]:

dir(sentiment)


# In[6]:

BAC = symbols('BAC').sid
bac_sentiment = sentiment[ (sentiment.sid == BAC) ]


# In[7]:

bac_sentiment.head(20)


# In[8]:

bac_sentiment.peek()


# In[9]:

import blaze


# In[10]:

bac_sentiment = blaze.compute(bac_sentiment)


# In[11]:

type(bac_sentiment)


# In[12]:

bac_sentiment.head()


# In[13]:

bac_sentiment.set_index('asof_date', inplace=True)


# In[14]:

bac_sentiment.head()


# In[15]:

bac_sentiment['sentiment_signal'].plot()


# In[16]:

bac_sentiment = bac_sentiment[ (bac_sentiment.index > '2016-06-01') ]


# In[17]:

bac_sentiment['sentiment_signal'].plot()


# In[18]:

from quantopian.pipeline import Pipeline


# In[19]:

def make_pipeline():
    return Pipeline()


# In[20]:

from quantopian.research import run_pipeline


# In[21]:

result = run_pipeline(make_pipeline(), start_date = '2015-05-05', end_date='2015-05-05')


# In[22]:

type(result)


# In[23]:

result.head()


# In[24]:

len(result)
from quantopian.pipeline.data.sentdex import sentiment


# In[25]:

def make_pipeline():
        sentiment_factor = sentiment.sentiment_signal.latest
        
        universe = (Q1500US() & sentiment_factor.notnull())
        
        pipe = Pipeline(columns={'sentiment': sentiment_factor,
                                                    'longs': (sentiment_factor >= 4),
                                                    'shorts': (sentiment_factor <= -2)},
                                   screen=universe)
        return pipe


# In[26]:

# 2015 is an excellent test year as it is neutral
result = run_pipeline(make_pipeline(), start_date = '2015-01-01', end_date='2016-01-01')


# In[27]:

result.head()


# In[28]:

#6:03 on p18
assets = result.index.levels[1].unique()
len(assets)


# In[30]:

pricing  = get_pricing(assets, start_date = '2014-12-01', end_date='2016-02-01', fields='open_price' )


# In[41]:

import alphalens

alphalens.tears.create_factor_tear_sheet(factor = result['sentiment'],
                                        prices = pricing,
                                        quantiles = 2,
                                        periods = (1,5,10))



# In[ ]:



