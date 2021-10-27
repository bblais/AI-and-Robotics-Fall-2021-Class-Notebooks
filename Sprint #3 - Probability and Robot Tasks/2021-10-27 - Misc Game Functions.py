#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[10]:


state=Board(5,5)
state[1]=state[3]=2
state[21]=state[23]=1
state[17]=2


# In[11]:


state.show_locations()


# In[12]:


state


# In[13]:


state.moves(1,'ne','nw')


# In[15]:


state.moves(1,'ne','nw','jne','jnw')


# In[16]:


state.moves(3,'se','ne','nw','jne','jnw')


# In[ ]:




