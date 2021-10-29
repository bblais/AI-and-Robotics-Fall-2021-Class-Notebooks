#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


def printQ(Q):
    print("=== Q ===")
    b=initial_state()
    
    for state in Q:
        b.board=state
        
        s=str(b).rstrip().split('\n')
        idx=int(round(len(s)/2))

        for i,line in enumerate(s):
            if i==idx-1:
                print(line,end="")
                for action in Q[state]:
                    print(f"  {action}: {Q[state][action]:.2g}",end="")
                print("")
            else:
                print(line) 
        print()
                
    print("=========")


# ## Game functions

# In[3]:


def initial_state():
    state=Board(3,3)
    state.pieces=[".","X","O"]
    
    state[0]=state[3]=1
    state[1]=state[4]=2
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
    


# In[4]:


initial_state()


# ## Agent Functions

# In[5]:


def human_move(state,player):
    
    state.show_locations()
    print("Player",player)
    move=int(input("which square to move?"))
    return move

human_agent=Agent(human_move)     


# In[6]:


def random_move(state,player):
    
    move=random.choice(valid_moves(state,player))
    return move


random_agent=Agent(random_move)


# In[7]:


from Game.minimax import *
def minimax_move(state,player):

    values,moves=minimax_values(state,player,display=True)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# ## Skittles Agent

# In[8]:


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


# In[9]:


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


# In[10]:


skittles1_agent=Agent(skittles_move)
skittles1_agent.post=skittles_after
skittles1_agent.T=Table()  # makes an empty table
skittles1_agent.learning=True

skittles2_agent=Agent(skittles_move)
skittles2_agent.post=skittles_after
skittles2_agent.T=Table()  # makes an empty table
skittles2_agent.learning=True


# In[11]:


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
    
    print("State\n",state)
    
    r=random.random()
    
    print(f"Random number: {r:.2f}")
    if r<ϵ:  # take a random move occasionally to explore the environment
        move=random_move(state,player)
        print(f"  Random Move {move}")
    else:
        move=top_choice(Q[state])
        print(f"Top Move {move} out of ")
        for action in Q[state]:
            print(f"    Q[state][{action}]={Q[state][action]}")

    
    if not last_action is None:  # not the first move
        reward=0
        
        print(f"Reward={reward}")
        print("Last State\n",last_state)
        print("Last Action\n",last_action)
        # learn
        if learning:
            
            print(f"    Old Q[last_state][{last_action}]={Q[last_state][last_action]}")
            print("Max Q = {max([Q[state][a] for a in Q[state]])} out of ")
            for action in Q[state]:
                print(f"    Q[state][{action}]={Q[state][action]}")
            
            print(f"    New Q[last_state][{last_action}] = {Q[last_state][last_action]:.2g} + {α:.2f}*({reward} + {γ}*{max([Q[state][a] for a in Q[state]])} - {Q[last_state][last_action]:.2g})=",end="")
            
            Q[last_state][last_action]+=α*(reward +
                        γ*max([Q[state][a] for a in Q[state]]) - Q[last_state][last_action])
            
            print(f"{Q[last_state][last_action]:.2g}")
            
            
    else:
        print("First Move No Update")
        
    printQ(Q)
    
    return move


# In[12]:


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
        
        print(f"Reward={reward}")
        print("Last State\n",last_state)
        print("Last Action\n",last_action)
        
        print(f"    Old Q[last_state][{last_action}]={Q[last_state][last_action]}")
        print(f"    New Q[last_state][{last_action}] = {Q[last_state][last_action]:.2g} +{α:.2f}*({reward} - {Q[last_state][last_action]:.2g})=",end="")

        
        Q[last_state][last_action]+=α*(reward - Q[last_state][last_action])
        print(f"{Q[last_state][last_action]:.2g}")
        
    printQ(Q)

    print("\n\n======\n\n")


# In[13]:


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

# In[14]:


agent1=Q1_agent
agent2=minimax_agent


# In[15]:


N_train=10
number_of_epochs=1
agent1_test=None
agent2_test=None


# In[16]:



iteration_count=0
percentage_won_player1=[]
percentage_won_player2=[]
percentage_tie=[]
number_of_iterations=[]

for i in range(number_of_epochs):

    agent1.learning=True
    agent2.learning=True

    g=Game(number_of_games=N_train)
    g.display=True
    result=g.run(agent1,agent2)


# In[181]:


Q1_agent.Q


# In[ ]:




