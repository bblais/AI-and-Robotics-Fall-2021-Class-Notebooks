#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


def initial_state():
    state=Board(3,3)  # empty
    
    # set up some initial pieces
    state[0]=1
    state[1]=1
    state[3]=2
    
    
    return state
    


# In[12]:


def initial_state():
    state=Board(3,3)  # empty
    
    for i in range(9):
        state[i]=1
    
    return state
    


# In[13]:


initial_state()


# In[14]:


def initial_state():
    state=Board(3,3)  # empty

    for i in range(9):
        state[i]=random.choice([0,1,2])
    
    
    return state
    


# In[15]:


state=initial_state()
state


# In[16]:


def find_all_pieces(state,player):
    locations=[]
    for location in range(9):
        if state[location]==player:
            locations.append(location)    
            
    return locations


# In[17]:


find_all_pieces(state,1)


# In[18]:


find_all_pieces(state,2)


# In[ ]:





# In[9]:


def update_state(state,player,move):
    # a move is a start and end location
    
    start,end=move
    new_state=state
    
    # ttt
    #new_state[move]=player
    
    new_state[start]=0
    new_state[end]=player
    
    
    
    return new_state
    
    


# In[5]:


move=[0,2]
start,end=move
start


# In[6]:


end


# In[7]:


state=Board(5,3)
state.show_locations()


# In[8]:


state[3]=state[7]=1
state[10]=2
state


# In[10]:


update_state(state,1,[3,4])


# In[11]:


update_state(state,1,[4,7])


# In[ ]:




