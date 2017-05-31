
# coding: utf-8

# In[12]:

from quantopian.interactive.data.sentdex import sentiment


# In[13]:

from quantopian.pipeline.filters.morningstar import Q1500US


# In[14]:

type(sentiment)


# In[15]:

dir(sentiment)


# In[16]:

BAC = symbols('BAC').sid
bac_sentiment = sentiment[ (sentiment.sid == BAC) ]


# In[17]:

bac_sentiment.head(20)


# In[18]:

bac_sentiment.peek()


# In[19]:

import blaze


# In[20]:

bac_sentiment = blaze.compute(bac_sentiment)


# In[21]:

type(bac_sentiment)


# In[22]:

bac_sentiment.head()


# In[23]:

bac_sentiment.set_index('asof_date', inplace=True)


# In[24]:

bac_sentiment.head()


# In[25]:

bac_sentiment['sentiment_signal'].plot()


# In[26]:

bac_sentiment = bac_sentiment[ (bac_sentiment.index > '2016-06-01') ]


# In[27]:

bac_sentiment['sentiment_signal'].plot()


# In[28]:

from quantopian.pipeline import Pipeline


# In[29]:

def make_pipeline():
    return Pipeline()


# In[30]:

from quantopian.research import run_pipeline


# In[31]:

result = run_pipeline(make_pipeline(), start_date = '2015-05-05', end_date='2015-05-05')


# In[32]:

type(result)


# In[33]:

result.head()


# In[37]:

len(result)
from quantopian.pipeline.data.sentdex import sentiment


# In[38]:

def make_pipeline():
        sentiment_factor = sentiment.sentiment_signal.latest
        
        universe = (Q1500US() & sentiment_factor.notnull())
        
        pipe = Pipeline(columns={'sentiment': sentiment_factor,
                                                    'longs': (sentiment_factor >= 4),
                                                    'shorts': (sentiment_factor <= -2)},
                                   screen=universe)
        return pipe


# In[39]:

# 2015 is an excellent test year as it is neutral
result = run_pipeline(make_pipeline(), start_date = '2015-01-01', end_date='2016-01-01')


# In[40]:

result.head()


# In[ ]:



