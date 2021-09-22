#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


def initial_state():
    state=Board(3,3)
    return state


# In[3]:


initial_state()


# ## diversion about Boards

# In[4]:


state=Board(5,3)


# In[5]:


state


# In[6]:


state[1]=5


# In[7]:


state


# In[8]:


state.show_locations()


# In[9]:


state[1,2]=11


# In[10]:


state


# In[11]:


state[0,1]


# ## back to TTT

# In[12]:


def show_state(state):
    print(state)


# In[13]:


state=initial_state()
show_state(state)


# In[34]:


def valid_moves(state,player):
    # run through all the spots
    # if it is empty, then append that
    # location to the possible moves
    
    moves=[]
    for location in range(9):
        if state[location]==0:
            moves.append(location)
            
    return moves


# In[35]:


state=initial_state()
valid_moves(state,1)


# In[36]:


state[2]=1
state[5]=2
state


# In[39]:


valid_moves(state,1)


# In[18]:


def update_state(state,player,move):
    new_state=state
    
    new_state[move]=player
    return new_state    
    


# In[19]:


state=initial_state()
state


# In[20]:


update_state(state,1,5)


# In[21]:


state.show_locations()


# In[22]:


state=Board(3,3)
state[5]=1
state[2]=2
state[4]=1


# In[23]:


state


# In[24]:


valid_moves(state,2)


# In[25]:


update_state(state,2,6)


# In[26]:


def win_status(state,player):
    # the state is *after* the move for the player

    #  0  1  2 
    #  3  4  5 
    #  6  7  8   
    
    # rows
    if state[0]==player and state[1]==player and state[2]==player:
        return "win"
    if state[3]==player and state[4]==player and state[5]==player:
        return "win"
    if state[6]==player and state[7]==player and state[8]==player:
        return "win"
    
    # columns
    if state[0]==player and state[3]==player and state[6]==player:
        return "win"
    if state[1]==player and state[4]==player and state[7]==player:
        return "win"
    if state[2]==player and state[5]==player and state[8]==player:
        return "win"
    
    # diagonals
    if state[0]==player and state[4]==player and state[8]==player:
        return "win"
    if state[2]==player and state[4]==player and state[6]==player:
        return "win"
    
    
    if player==1:
        other_player=2
    else:
        other_player=1
        
    # hack, unreadable, but works.  other_player=3-player
    
    
    if not valid_moves(state,other_player):
        return "stalemate"
    
    
    
    


# In[27]:


player=2

if player==1:
    other_player=2
else:
    other_player=1

other_player


# In[28]:


def human_move(state,player):
    
    state.show_locations()
    print("Player",player)
    move=int(input("which square to move?"))
    
    
    return move
    


# In[ ]:


state=initial_state()
#human_move(state,1)


# In[32]:


human_agent=Agent(human_move)


# In[33]:


def random_move(state,player):
    
    move=random.choice(valid_moves(state,player))
    return move


random_agent=Agent(random_move)


# In[ ]:





# In[ ]:





# In[39]:


g=Game()
g.run(human_agent,human_agent)


# In[ ]:




