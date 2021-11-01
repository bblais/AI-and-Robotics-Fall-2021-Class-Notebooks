#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[3]:


get_ipython().run_line_magic('pinfo', 'Card')


# In[10]:


Card(1,'h')


# In[11]:


Card(13,'h')


# In[12]:


c=Card(13,'h')


# In[13]:


c.rank


# In[14]:


c.suit


# In[16]:


deck=makedeck()
deck


# In[17]:


cards=deal(deck,2)
print(cards)
print(len(deck),deck)


# In[18]:


def score(cards):
    
    total=0
    for card in cards:
        total+=card.rank
        
    return total


# In[19]:


score(cards)


# In[ ]:




