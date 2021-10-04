#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# ## Game functions

# In[2]:


def initial_state():
    state=Board(3,3)
    state.pieces=[".","X","O"]
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


# In[10]:


g=Game(number_of_games=20)
g.display=False
g.run(random_agent,skittles_agent)


# In[26]:


get_ipython().run_cell_magic('time', '', 'N_train=500\nN_test=100\niteration_count=0\n\nskittles_agent.T=Table()  # makes an empty table\n\npercentage_won_player1=[]\npercentage_won_player2=[]\npercentage_tie=[]\nnumber_of_iterations=[]\n\nfor i in range(200):\n\n    skittles_agent.learning=True\n    g=Game(number_of_games=N_train)\n    g.display=False\n    result=g.run(random_agent,skittles_agent)\n\n\n    # turn learning off to test\n    skittles_agent.learning=False\n    g=Game(number_of_games=N_test)\n    g.display=False\n    result=g.run(random_agent,skittles_agent)\n    iteration_count+=N_train\n\n    percentage_won_player1.append(result.count(1)/N_test*100)\n    percentage_won_player2.append(result.count(2)/N_test*100)\n    percentage_tie.append(result.count(0)/N_test*100)\n    number_of_iterations.append(iteration_count)')


# In[ ]:





# In[29]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import plot,xlabel,ylabel,legend,figure


# In[30]:


figure(figsize=(12,10))
plot(number_of_iterations,percentage_won_player1,'-o',label='Player 1')
plot(number_of_iterations,percentage_won_player2,'-x',label='Player 2')
plot(number_of_iterations,percentage_tie,'-s',label='Tie')
legend()
xlabel('Number of Games')
ylabel('Percentage Won')


# In[ ]:




