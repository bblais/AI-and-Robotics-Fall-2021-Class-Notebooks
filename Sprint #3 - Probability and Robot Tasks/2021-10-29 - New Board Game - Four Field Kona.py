#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# https://en.wikipedia.org/wiki/Four_Field_Kono
# 
# The goal of each player is to capture the other player's pieces and reduce it to one. This is because with only one piece, a player can no longer execute a capture. Another way to win is for a player to immobilize the other player's pieces so that they cannot move or capture.
# 
# The game is played according to these rules.[1]
# 
# 1. Players decide what color marbles to play, and who goes first.
# 2. The board is completely filled with the 16 marbles in the beginning. Each player's marbles are set up on their half of the board.
# 3. Since the board is filled up in the beginning and hence no vacant holes, the first move by the first player will be a capturing move.
# 4. A capturing move requires a player's marble to jump over one of his own adjacent marbles orthogonally (not diagonally), and to land onto an enemy marble which is then removed from the board and replaced with the player's marble. Only one marble can be used to capture or move per turn. Multiple captures are not allowed. Once a marble has captured one enemy marble, the turn is completed. Captures are not compulsory.
# 5. A marble can move orthogonally (not diagonally) one space per turn onto a vacant hole.
# 6. Players alternate their turns throughout the game.
# 
# 
# 
# <img src="images/2019-09-24 07.21.03 am.png" width=100>
# 
# 
# <img src="images/2019-09-24 07.24.27 am.png" width=400>
# 

# ## Game functions

# In[2]:


def initial_state():
    state=Board(4,4)
    
    for r in range(4):
        for c in range(2):
            state[r,c]=1
            state[r,c+2]=2
    return state


# In[3]:


state=initial_state()
state.show_locations()
state


# In[4]:


def show_state(state):
    print(state)
    
def update_state(state,player,move):
    # a move is a start and an end
    start,end=move
    new_state=state
    new_state[start]=0
    new_state[end]=player
    return new_state


# In[5]:


def win_status(state,player):
    if player==1:
        other_player=2
    else:
        other_player=1
        
    if not valid_moves(state,other_player):
        return 'win'
    
    # count the pieces of the other player
    count=0
    for i in range(16):
        if state[i]==other_player:
            count+=1
    if count==1:
        return 'win'
    
    return None  # middle of the game


# In[6]:


def valid_moves(state,player):
    
    #  0  1  2  3 
    #  4  5  6  7 
    #  8  9 10 11 
    # 12 13 14 15     
    if player==1:
        other_player=2
    else:
        other_player=1
    
    moves=[]
    # right/left-moving capture
    for start in [0,1,4,5,8,9,12,13]:
        middle=start+1
        end=start+2
        
        # right jump
        if state[start]==player and state[middle]==player and state[end]==other_player:
            moves.append([start,end])
        # left jump
        if state[end]==player and state[middle]==player and state[start]==other_player:
            moves.append([start,end])
    
    # up/down-moving capture
    for start in [0,1,2,3,4,5,6,7]:
        middle=start+4
        end=start+8
        
        # down jump
        if state[start]==player and state[middle]==player and state[end]==other_player:
            moves.append([start,end])
        # up jump
        if state[end]==player and state[middle]==player and state[start]==other_player:
            moves.append([start,end])
        
    # right/left moves
    for r in range(4):
        # right
        for c in range(3):
            if state[r,c]==player and state[r,c+1]==0:
                moves.append([
                        state.index_from_rc(r,c),
                        state.index_from_rc(r,c+1)
                ])
                
        for c in range(1,4):
            if state[r,c]==player and state[r,c-1]==0:
                moves.append([state.index_from_rc(r,c),state.index_from_rc(r,c-1)])                
                
    # up/down moves
    for c in range(4):
        # up
        for r in range(3):
            if state[r,c]==player and state[r+1,c]==0:
                moves.append([state.index_from_rc(r,c),state.index_from_rc(r+1,c)])
        # down     
        for r in range(1,4):
            if state[r,c]==player and state[r-1,c]==0:
                moves.append([state.index_from_rc(r,c),state.index_from_rc(r-1,c)])                

    return moves


# In[7]:


state=initial_state()
show_state(state)
state.show_locations()

print(valid_moves(state,1))


# In[8]:


state=initial_state()
state[4]=0
show_state(state)
state.show_locations()

print(valid_moves(state,1))


# ## Agents

# In[9]:


def human_move(state,player):
    print("Player ",player)
    state.show_locations()
    
    start=int(input("What location to start?"))
    end=int(input("What location to end?"))
    move=[start,end]
    
    return move

human_agent=Agent(human_move)


# In[10]:


def random_move(state,player):
    
    move=random.choice(valid_moves(state,player))
    return move


random_agent=Agent(random_move)


# In[11]:


from Game.minimax import *
def minimax_move(state,player):

    values,moves=minimax_values(state,player,display=True)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[12]:


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


# In[13]:


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


# In[14]:


skittles1_agent=Agent(skittles_move)
skittles1_agent.post=skittles_after
skittles1_agent.T=Table()  # makes an empty table
skittles1_agent.learning=True

skittles2_agent=Agent(skittles_move)
skittles2_agent.post=skittles_after
skittles2_agent.T=Table()  # makes an empty table
skittles2_agent.learning=True


# In[15]:


def Q_move(state,player,info):
    Q=info.Q
    last_state=info.last_state
    last_action=info.last_action
    learning=info.learning
    
    α=info.α  # learning rate
    ϵ=info.ϵ  # how often to take a random move
    γ=info.γ  # memory constant -- how quickly does the table update back in time (earlier in the game)
    
    # \alpha <hit tab>    α
    # \epsilon <hit tab>  ϵ
    # \gamma <hit tab>    γ
    
    if state not in Q:
        actions=valid_moves(state,player)
        Q[state]=Table()
        for action in actions:
            Q[state][action]=0  # initial value of table
    
    
    if random.random()<ϵ:  # take a random move occasionally to explore the environment
        move=random_move(state,player)
    else:
        move=top_choice(Q[state])
    
    if not last_action is None:  # not the first move
        reward=0
        
        # learn
        if learning:
            Q[last_state][last_action]+=α*(reward +
                        γ*max([Q[state][a] for a in Q[state]]) - Q[last_state][last_action])
    
    return move


# In[16]:


def Q_after(status,player,info):
    Q=info.Q
    last_state=info.last_state
    last_action=info.last_action
    learning=info.learning
    
    α=info.α  # learning rate
    ϵ=info.ϵ  # how often to take a random move
    γ=info.γ  # memory constant -- how quickly does the table update back in time (earlier in the game)
    
    # \alpha <hit tab>    α
    # \epsilon <hit tab>  ϵ
    # \gamma <hit tab>    γ

    if status=='lose':
        reward=-1
    elif status=='win':
        reward=1
    elif status=='stalemate':
        reward=.5 # value stalemate a little closer to a win
    else:
        reward=0
    
    
    if learning:
        Q[last_state][last_action]+=α*(reward - Q[last_state][last_action])
        


# In[17]:


Q1_agent=Agent(Q_move)
Q1_agent.post=Q_after
Q1_agent.Q=Table()  # makes an empty table
Q1_agent.learning=True

Q1_agent.α=0.3  # learning rate
Q1_agent.ϵ=0.1  # how often to take a random move
Q1_agent.γ=0.9  # memory constant -- how quickly does the table update back in time (earlier in the game)

Q2_agent=Agent(Q_move)
Q2_agent.post=Q_after
Q2_agent.Q=Table()  # makes an empty table
Q2_agent.learning=True

Q2_agent.α=0.3  # learning rate
Q2_agent.ϵ=0.1  # how often to take a random move
Q2_agent.γ=0.9  # memory constant -- how quickly does the table update back in time (earlier in the game)


# ## Running the Game

# super slow game...not sure why but I think the game tree is pretty big.

# In[33]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[34]:


from IPython.display import clear_output


# In[35]:


agent1=skittles1_agent
agent2=random_agent


# In[36]:


N_train=2
N_test=100
number_of_epochs=200
agent1_test=None
agent2_test=None


# In[37]:



iteration_count=0
percentage_won_player1=[]
percentage_won_player2=[]
percentage_tie=[]
number_of_iterations=[]



fig=plt.figure(figsize=(12,10))
for i in range(number_of_epochs):
    clear_output(wait=True)
    
    agent1.learning=True
    agent2.learning=True

    g=Game(number_of_games=N_train)
    g.display=False
    result=g.run(agent1,agent2)


    if agent1_test is None:
        agent1_test=agent1
    if agent2_test is None:
        agent2_test=agent2

    # turn learning off to test
    agent1.learning=False
    agent2.learning=False

    g=Game(number_of_games=N_test)
    g.display=False
    result=g.run(agent1_test,agent2_test)
    iteration_count+=N_train

    percentage_won_player1.append(result.count(1)/N_test*100)
    percentage_won_player2.append(result.count(2)/N_test*100)
    percentage_tie.append(result.count(0)/N_test*100)
    number_of_iterations.append(iteration_count)

    h1=plt.plot(number_of_iterations,percentage_won_player1,'-o',label='Player 1')
    h2=plt.plot(number_of_iterations,percentage_won_player2,'-x',label='Player 2')
    h3=plt.plot(number_of_iterations,percentage_tie,'-s',label='Tie')
    plt.legend()
    plt.xlabel('Number of Games')
    plt.ylabel('Percentage Won')    
    plt.show()


# In[ ]:




