#!/usr/bin/env python
# coding: utf-8

# ## Rules of Pig

# - moves are either "hold" or "roll"
# - "roll" a die
#     - if 2-6 add to your turn total
#     - if 1 turn total=0, next turn
# - "hold"
#     - turn total gets added to the players total, next turn

# In[7]:


from Game import *


# In[27]:


def valid_moves(state,player):
    return ["hold","roll"]

def initial_state():
    # player 1's total, player 2's total, turn total, last dice roll
    return [0,0,0,0]


# In[28]:


def show_state(state):
    print("Player 1's total is",state[0])
    print("Player 2's total is",state[1])    
    print("Last dice roll as ",state[3])
    print("The turn total is",state[2])


# In[29]:


def update_state(state,player,move):
    new_state=state
    
    total1,total2,turn_total,last_dice=state
    
    if move=="hold":
        # state is [player 1's total, player 2's total, turn total]
        
        if player==1:
            new_state[0]+=turn_total
        else:
            new_state[1]+=turn_total
            
        new_state[2]=0  # turn total back to zero
        
        state[3]=0
    else:  # roll
    
        dice=random.randint(1,6)  # generates a random number between 1 and 6
        
        if dice==1:
            
            new_state[2]=0  # turn total back to zero
            
        else:
            
            new_state[2]+=dice  # turn total 
    
    
        state[3]=dice
    return new_state
    


# In[30]:


def win_status(state,player):
    
    max_score=21
    total1,total2,turn_total,last_dice=state
    
    if player==1:        
        if total1+turn_total>=max_score:
            return "win"
    else:
        if total2+turn_total>=max_score:
            return "win"
    


# In[31]:


def repeat_move(state,player,move):
    total1,total2,turn_total,last_dice=state
    
    if turn_total>0:
        return True
    else:
        return False
    


# In[32]:


def human_move(state,player):
    print("Player",player)
    s=input("hold or roll?")
    
    if s[0]=='h':
        return "hold"
    elif s[0]=='r':
        return "roll"
    
human_agent=Agent(human_move)


# In[33]:


def random_move(state,player):
    move=random.choice(valid_moves(state,player))
    return move

random_agent=Agent(random_move)


# In[ ]:


g=Game()
g.run(human_agent,random_agent)


# In[ ]:





# In[ ]:




