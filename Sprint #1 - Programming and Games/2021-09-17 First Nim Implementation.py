#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# def initial_state(): 
# """ returns  - The initial state of the game"""
# 
# def valid_moves(state,player):
# """returns  - a list of the valid moves for the state and player"""
# 
# def show_state(state):
# """prints or shows the current state"""
# 
# def update_state(state,player,move):
# """returns  - the new state after the move for the player"""
# 
# def win_status(state,player):
# """    returns  - 'win'  if the state is a winning state for the player, 
#            'lose' if the state is a losing state for the player,
#            'stalemate' for a stalemate
#            None otherwise
# """
# 
# 
# - Nim game
#     1. start with 21 sticks
#     2. each player can take 1, 2, or 3 sticks (no more or fewer)
#     3. whomever **takes the last stick loses**

# In[2]:


def initial_state():
    return 21


# In[3]:


initial_state()


# In[4]:


def show_state(state):
    print(state)


# In[5]:


state=initial_state()
show_state(state)


# In[9]:


def valid_moves(state,player):
    if state==2:
        return [1,2]
    elif state==1:
        return [1]
    else:
        return [1,2,3]


# In[10]:


valid_moves(21,1)


# In[11]:


valid_moves(2,1)


# In[12]:


def update_state(state,player,move):
    new_state=state-move
    return new_state


# In[ ]:




