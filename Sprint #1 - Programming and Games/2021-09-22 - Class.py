#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


state=Board(4,4)


# In[3]:


state.show_locations()


# In[4]:


def valid_moves(state,player):
    # possible moves are [0,1,2,3]
    
    # only if state[move]==0
    
    moves=[]
    
    if state[0]==0:
        moves.append(0)
        
    return moves


# In[7]:


diagonals=[]
for r in range(3):
    for c in range(4):
        start=state.index_from_rc(r,c)
        end=state.index_from_rc(r+1,c)
        diagonals.append([start,end])


# In[8]:


diagonals


# In[10]:


diagonals=[]
for r in range(4):
    for c in range(4):
        try:
            start=state.index_from_rc(r,c)
            end=state.index_from_rc(r+1,c)
        except IndexError:
            continue
            
        diagonals.append([start,end])


# In[ ]:




