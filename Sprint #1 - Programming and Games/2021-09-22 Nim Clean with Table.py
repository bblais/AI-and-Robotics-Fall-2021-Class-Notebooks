#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# ## Game functions

# In[30]:


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

# In[31]:


def human_move(state,player):
    move=int(input("how many sticks to take (1,2, or 3?"))
    return move
human_agent=Agent(human_move)    


# In[32]:


def random_move(state,player):
    
    move=random.choice(valid_moves(state,player))
    return move


random_agent=Agent(random_move)


# In[33]:


def make_nim_table():
    T=Table()
    
    for state in range(1,25):
        T[state]=Table()
    
        actions=valid_moves(state,1)
        
        for action in actions:
            T[state][action]=-1 # lose most of the time
            
    T[2][1]=1   # 2 sticks, taking one, leads to a win  
    T[4][3]=1   # 4 sticks, taking 3, leads to a win  
    #etc.....
    
    
    return T


# In[34]:


make_nim_table()


# In[35]:


def table_move(state,player):
    T=make_nim_table()
    move=top_choice(T[state])
    return move

table_agent=Agent(table_move)


# ## Running the Game

# In[36]:


g=Game(N=21)
g.run(random_agent,table_agent)


# In[ ]:




