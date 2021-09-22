#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


state=Board(4,4)


# In[4]:


state.show_locations()


# In[ ]:


def valid_moves(state,player):
    # possible moves are [0,1,2,3]
    
    # only if state[move]==0
    
    moves=[]
    
    if state[0]==0:
        moves.append(0)
        
    return moves

