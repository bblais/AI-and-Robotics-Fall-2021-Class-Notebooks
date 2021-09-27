#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[8]:


import Game


# In[9]:


Game.__file__


# In[11]:


import this


# ## Game functions

# In[12]:


def initial_state(N=21):
    return N

def show_state(state):
    print("There are ",state,"sticks")
    
def valid_moves(state,player):
    if state==2:
        return [1,2]
    elif state==1:
        return [1]
    else:
        return [1,2,3]
    
def update_state(state,player,move):
    new_state=state-move
    return new_state

def win_status(state,player):
    # the state is *after* the move for the player
    if state==1:
        return "win"
    
    if state==0:
        return "lose"
    
    return None # mid-game


# ## Agent Functions

# In[13]:


def human_move(state,player):
    move=int(input("how many sticks to take (1,2, or 3?"))
    return move
human_agent=Agent(human_move)    


# In[14]:


def random_move(state,player):
    
    move=random.choice(valid_moves(state,player))
    return move


random_agent=Agent(random_move)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[15]:


from Game.minimax import *
def minimax_move(state,player):

    values,moves=minimax_values(state,player,display=True)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[16]:


minimax_values(5,1)


# In[17]:


minimax_values(6,1)


# In[ ]:


minimax_values(21,1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Running the Game

# In[36]:


g=Game(N=21)
g.run(random_agent,table_agent)


# In[ ]:




