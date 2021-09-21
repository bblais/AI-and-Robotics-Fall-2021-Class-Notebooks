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


# In[34]:


def initial_state():
    state=Board(3,3)  # empty

    for i in range(9):
        state[i]=random.choice([0,1,2])
    
    
    return state
    


# In[35]:


state=initial_state()
state


# In[16]:


def find_all_pieces(state,player):
    locations=[]
    for location in range(9):
        if state[location]==player:
            locations.append(location)    
            
    return locations


# In[36]:


find_all_pieces(state,1)


# In[37]:


find_all_pieces(state,2)


# In[38]:


find_all_pieces(state,3)


# In[ ]:


if not find_all_pieces(state,player):
    return "win"


# In[ ]:





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


# In[19]:


state=Board(5,3)
state.show_locations()


# In[20]:


state.rc_from_index(10)


# In[21]:


state.index_from_rc(3,1)


# In[ ]:


start,end = 1,2

for start,end in [ 
    [1,2], [3,4], [5,10], [2,-1]
                ]:

    if end>=0:
        if state[start]==player and state[end]==0:
            moves.append( [start,end] )
    else:
        if state[start]==player:
            moves.append( [start,end] )
        


# In[ ]:


start,end = 1,2
moves=[]
for start,end in [ 
    [1,2], [3,4], [5,10], 
                ]:

    if state[start]==player and state[end]==0:
        moves.append( [start,end] )
        


# In[22]:


moves=[]


# In[25]:


moves


# In[29]:


moves.append([2,3,4])
moves


# In[ ]:


def valid_moves(state,player):
    moves=[]
    
    if player==1:
        
        pass
    
    else:
        
        pass
    
    return moves
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[8]:


state[3]=state[7]=1
state[10]=2
state


# In[10]:


update_state(state,1,[3,4])


# In[11]:


update_state(state,1,[4,7])


# In[ ]:




