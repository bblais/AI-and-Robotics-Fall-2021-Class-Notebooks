#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[5]:


def find_all_pieces(state,player):
    locations=[]
    for i in range(len(state)):
        if state[i]==player:
            locations.append(i)
    return locations


# In[3]:


state=Board(3,4)
state[0]=1
state[1]=1
state[3]=2
len(state)


# In[4]:


state


# In[6]:


def heuristic(state,player):
    
    # return a value between -1 and 1 (not inclusive)
    # which is approximate value of the state
    # positive = good for player
    # negative = bad for player
    
    if player==1:
        other_player=2
    else:
        other_player=1
        
    N_player=len(find_all_pieces(state,player))
    N_other_player=len(find_all_pieces(state,other_player))
    
    value=(N_player-N_other_player)/(N_player+N_other_player)
    return value


# In[7]:


heuristic(state,1)


# In[ ]:




