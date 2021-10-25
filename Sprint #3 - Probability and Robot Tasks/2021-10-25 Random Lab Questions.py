#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[3]:


state=Board(4,4)
state[2]=state[4]=1
state[5]=state[10]=2
state[3]=state[7]=3
state[11]=state[12]=4
state


# In[4]:


state.pieces=['.','X','O','K','R']


# In[5]:


state


# In[ ]:




