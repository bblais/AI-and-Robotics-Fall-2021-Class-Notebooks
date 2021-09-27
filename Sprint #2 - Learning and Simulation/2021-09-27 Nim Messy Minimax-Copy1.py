#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Game


# In[2]:


Game.__file__


# In[3]:


from Game import *


# In[4]:


import this


# ## Game functions

# In[5]:


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

# In[6]:


def human_move(state,player):
    move=int(input("how many sticks to take (1,2, or 3?"))
    return move
human_agent=Agent(human_move)    


# In[7]:


def random_move(state,player):
    
    move=random.choice(valid_moves(state,player))
    return move


random_agent=Agent(random_move)


# In[8]:


from Game.minimax import *
def minimax_move(state,player):

    values,moves=minimax_values(state,player,display=True)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[9]:


minimax_values(5,1)


# In[10]:


minimax_values(6,1)


# In[11]:


minimax_values(31,1)


# ## Running the Game

# In[12]:


g=Game(N=21)
g.run(random_agent,minimax_agent)


# ## what happens if the game is too long?

# In[13]:


g=Game(N=31)
g.run(random_agent,minimax_agent)


# In[16]:


from Game.minimax import *
def minimax_move(state,player):

    values,moves=minimax_values(state,player,maxdepth=4,display=True)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[19]:


def findall(state,player):
    locations=[]
    for i in range(len(state)):
        if state[i]==player:
            locations.append(i)
    return locations


# In[21]:


state=Board(3,4)
state[0]=1
state[1]=1
state[3]=2
len(state)


# In[22]:


state


# In[25]:


def heuristic(state,player):
    
    # return a value between -1 and 1 (not inclusive)
    # which is approximate value of the state
    # positive = good for player
    # negative = bad for player
    
    if player==1:
        other_player=2
    else:
        other_player=1
        
    N_player=len(findall(state,player))
    N_other_player=len(findall(state,other_player))
    
    value=(N_player-N_other_player)/(N_player+N_other_player)
    return value


# In[26]:


heuristic(state,1)


# In[ ]:





# In[ ]:





# In[17]:


g=Game(N=31)
g.run(random_agent,minimax_agent)


# In[ ]:




