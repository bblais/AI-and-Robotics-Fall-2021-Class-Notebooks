#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# ## Game functions

# In[2]:


def initial_state():
    state=Board(3,3)
    state.pieces=[".","X","O"]
    
    state.board=[1,0,2,1,0,2,0,0,0]
    return state

def show_state(state):
    print(state)
    
def valid_moves(state,player):
    # run through all the spots
    # if it is empty, then append that
    # location to the possible moves
    
    moves=[]
    for location in range(9):
        if state[location]==0:
            moves.append(location)
            
    return moves  

def update_state(state,player,move):
    new_state=state
    
    new_state[move]=player
    return new_state    
    
def win_status(state,player):
    # the state is *after* the move for the player

    #  0  1  2 
    #  3  4  5 
    #  6  7  8   
    
    for start,middle,end in [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6],
                ]:
        
        if state[start]==player and state[middle]==player and state[end]==player:
            return "win"
        
    if player==1:
        other_player=2
    else:
        other_player=1
    
    if not valid_moves(state,other_player):
        return "stalemate"
    


# ## Agent Functions

# In[3]:


def human_move(state,player):
    
    state.show_locations()
    print("Player",player)
    move=int(input("which square to move?"))
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


# ## Skittles Agent

# In[6]:


def skittles_move(state,player,info):
    T=info.T
    last_state=info.last_state
    last_action=info.last_action
    learning=info.learning
    
    if state not in T:
        actions=valid_moves(state,player)
        T[state]=Table()
        for action in actions:
            T[state][action]=2  # initial number of skittles
    
    move=weighted_choice(T[state])
    
    if move is None:  
        
        # learn
        if learning:
            if last_state:
                T[last_state][last_action]-=1 # take away a skittle
                if T[last_state][last_action]<0:
                    T[last_state][last_action]=0
    
        return random_move(state,player)
    else:
        return move


# In[7]:


def skittles_after(status,player,info):
    # not return anything but...
    # will adjust the skittles table if lost the game
    T=info.T
    last_state=info.last_state
    last_action=info.last_action
    learning=info.learning
    
    if learning:
        if status=='lose':  # only learn when you lose
            T[last_state][last_action]-=1 # take away a skittle
            if T[last_state][last_action]<0:
                T[last_state][last_action]=0


# In[8]:


skittles_agent=Agent(skittles_move)
skittles_agent.post=skittles_after
skittles_agent.T=Table()  # makes an empty table
skittles_agent.learning=True


# ## Running the Game

# In[9]:


g=Game()
g.run(random_agent,skittles_agent)


# In[11]:


skittles_agent.T


# In[13]:


SaveTable(skittles_agent.T,"skittles TTT endgame1.json")


# In[14]:


g.run(random_agent,skittles_agent)


# In[15]:


skittles_agent.T


# In[17]:


SaveTable(skittles_agent.T,"skittles TTT endgame2.json")


# In[18]:


g=Game(number_of_games=10)
g.display=False
g.run(random_agent,skittles_agent)


# In[19]:


skittles_agent.T


# In[20]:


SaveTable(skittles_agent.T,"skittles TTT endgame12.json")


# In[21]:


g=Game(number_of_games=20)
g.display=False
g.run(random_agent,skittles_agent)


# In[22]:


skittles_agent.T


# In[23]:


SaveTable(skittles_agent.T,"skittles TTT endgame32.json")


# In[ ]:




