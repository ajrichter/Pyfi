
# coding: utf-8

# In[1]:

from quantopian.interactive.data.sentdex import sentiment


# In[2]:

from quantopian.pipeline.filters.morningstar import Q1500US


# In[3]:

type(sentiment)


# In[4]:

dir(sentiment)


# In[5]:

BAC = symbols('BAC').sid
bac_sentiment = sentiment[ (sentiment.sid == BAC) ]


# In[7]:

bac_sentiment.head(20)


# In[9]:

bac_sentiment.peek()


# In[10]:

import blaze


# In[11]:

bac_sentiment = blaze.compute(bac_sentiment)


# In[12]:

type(bac_sentiment)


# In[13]:

bac_sentiment.head()


# In[15]:

bac_sentiment.set_index('asof_date', inplace=True)


# In[16]:

bac_sentiment.head()


# In[17]:

bac_sentiment['sentiment_signal'].plot()


# In[18]:

bac_sentiment = bac_sentiment[ (bac_sentiment.index > '2016-06-01') ]


# In[19]:

bac_sentiment['sentiment_signal'].plot()


# In[ ]:



