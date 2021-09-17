#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


def initial_state():
    return Board(3,3)


# In[3]:


initial_state()


# ## diversion about Boards

# In[20]:


state=Board(5,3)


# In[21]:


state


# In[22]:


state[1]=5


# In[23]:


state


# In[24]:


state.show_locations()


# In[25]:


state[1,2]=11


# In[26]:


state


# In[27]:


state[0,1]


# ## back to TTT

# In[28]:


def show_state(state):
    print(state)


# In[29]:


state=initial_state()
show_state(state)


# In[30]:


def valid_moves(state,player):
    # run through all the spots
    # if it is empty, then append that
    # location to the possible moves
    
    moves=[]
    for location in range(9):
        if state[location]==0:
            moves.append(location)
            
    return moves


# In[31]:


state=Board(3,3)
valid_moves(state,1)


# In[32]:


state[2]=1
state[5]=2
state


# In[33]:


valid_moves(state,1)


# In[34]:


def update_state(state,player,move):
    new_state=state
    
    new_state[move]=player
    return new_state    
    


# In[ ]:




