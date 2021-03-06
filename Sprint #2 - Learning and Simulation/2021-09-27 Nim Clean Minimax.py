#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# ## Game functions

# In[2]:


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

# In[3]:


def human_move(state,player):
    move=int(input("how many sticks to take (1,2, or 3?"))
    return move
human_agent=Agent(human_move)    


# In[4]:


def random_move(state,player):
    
    move=random.choice(valid_moves(state,player))
    return move


random_agent=Agent(random_move)


# In[5]:


from Game.minimax import *
def minimax_move(state,player):

    values,moves=minimax_values(state,player,display=True)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# ## Running the Game

# In[6]:


g=Game(N=31)
g.run(random_agent,minimax_agent)


# ## Long games -- set maxdepth and use heuristic

# In[7]:


from Game.minimax import *
def minimax_move(state,player):

    values,moves=minimax_values(state,player,maxdepth=4,display=True)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[8]:


def heuristic(state,player):
    
    # return a value between -1 and 1 (not inclusive)
    # which is approximate value of the state
    # positive = good for player
    # negative = bad for player
    
    # odd numbers are generally bad for them
    
    if state%2 == 0:
        value=-0.3
    else:
        value=0.3
    
    return value


# In[9]:


g=Game(N=31)
g.run(random_agent,minimax_agent)


# In[ ]:




