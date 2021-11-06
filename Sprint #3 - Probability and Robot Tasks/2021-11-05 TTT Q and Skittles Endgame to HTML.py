#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# ## Game functions

# In[2]:


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

    values,moves=minimax_values(state,player,display=False)
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
    status=None
    
    if move is None:  
        
        is_random_move=True
        move=random_move(state,player)
        
        if learning:  # don't save for test cases
            info.saved.append( 
                [deepcopy(T),deepcopy(last_state),deepcopy(last_action),deepcopy(state),is_random_move,move,None,status]
                )
        
        
        # learn
        if learning:
            if last_state:
                T[last_state][last_action]-=1 # take away a skittle
                if T[last_state][last_action]<0:
                    T[last_state][last_action]=0
    
        return move
    else:
        
        if learning:  # don't save for test cases
            info.saved.append( 
                [deepcopy(T),deepcopy(last_state),deepcopy(last_action),deepcopy(state),is_random_move,move,None,status]
                )        
        
        
        return move


# In[7]:


def skittles_after(status,player,info):
    # not return anything but...
    # will adjust the skittles table if lost the game
    T=info.T
    last_state=info.last_state
    last_action=info.last_action
    learning=info.learning
    
    if learning:  # don't save for test cases
        info.saved.append( 
            [deepcopy(T),deepcopy(last_state),deepcopy(last_action),None,False,None,None,status]
            )        
    
    
    if learning:
        if status=='lose':  # only learn when you lose
            T[last_state][last_action]-=1 # take away a skittle
            if T[last_state][last_action]<0:
                T[last_state][last_action]=0
                
    if learning:  # don't save for test cases
        info.saved.append( 
            [deepcopy(T),deepcopy(last_state),deepcopy(last_action),None,False,None,None,status]
            )        
                


# In[8]:


skittles1_agent=Agent(skittles_move)
skittles1_agent.post=skittles_after
skittles1_agent.T=Table()  # makes an empty table
skittles1_agent.learning=True
skittles1_agent.saved=[]

skittles2_agent=Agent(skittles_move)
skittles2_agent.post=skittles_after
skittles2_agent.T=Table()  # makes an empty table
skittles2_agent.learning=True
skittles2_agent.saved=[]


# In[9]:


from copy import deepcopy


# In[10]:


def Q_move(state,player,info):
    Q=info.Q
    last_state=info.last_state
    last_action=info.last_action
    learning=info.learning
    
    
    α=info.α  # learning rate
    ϵ=info.ϵ  # how often to take a random move
    γ=info.γ  # memory constant -- how quickly does the table update back in time (earlier in the game)
    
    if not learning:
        α=0.0  # don't update the weights
        ϵ=0.0  # don't do random moves when testing
    
    # \alpha <hit tab>    α
    # \epsilon <hit tab>  ϵ
    # \gamma <hit tab>    γ
    
    if state not in Q:
        actions=valid_moves(state,player)
        Q[state]=Table()
        for action in actions:
            Q[state][action]=0  # initial value of table
    
    
    is_random_move=False
    if random.random()<ϵ:  # take a random move occasionally to explore the environment
        move=random_move(state,player)
        is_random_move=True
        assert learning
        
    else:
        move=top_choice(Q[state])
    
    
    reward=0
    status=None
    if learning:  # don't save for test cases
        info.saved.append( 
            [deepcopy(Q),deepcopy(last_state),deepcopy(last_action),deepcopy(state),is_random_move,move,reward,status]
            )
    
    if not last_action is None:  # not the first move
        Q[last_state][last_action]+=α*(reward +
                    γ*max([Q[state][a] for a in Q[state]]) - Q[last_state][last_action])
                    
    
    return move


# In[11]:


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
        
    is_random_move=move=None        
    
    if learning:  # don't save for test cases
        info.saved.append( 
            [deepcopy(Q),deepcopy(last_state),deepcopy(last_action),None,is_random_move,move,reward,status]
            )
    
    if learning:
        Q[last_state][last_action]+=α*(reward - Q[last_state][last_action])
        
    if learning:  # don't save for test cases
        info.saved.append( 
            [deepcopy(Q),deepcopy(last_state),deepcopy(last_action),None,is_random_move,move,reward,status]
            )


# In[12]:


Q1_agent=Agent(Q_move)
Q1_agent.post=Q_after
Q1_agent.Q=Table()  # makes an empty table
Q1_agent.learning=True
Q1_agent.saved=[]

Q1_agent.α=0.3  # learning rate
Q1_agent.ϵ=0.5  # how often to take a random move
Q1_agent.γ=0.9  # memory constant -- how quickly does the table update back in time (earlier in the game)

Q2_agent=Agent(Q_move)
Q2_agent.post=Q_after
Q2_agent.Q=Table()  # makes an empty table
Q2_agent.learning=True
Q1_agent.saved=[]

Q2_agent.α=Q1_agent.α  # learning rate
Q2_agent.ϵ=Q1_agent.ϵ  # how often to take a random move
Q2_agent.γ=Q1_agent.γ  # memory constant -- how quickly does the table update back in time (earlier in the game)


# ## Running the Game

# In[13]:


from tqdm import tqdm


# In[14]:


agent1=Q1_agent
agent2=minimax_agent


# In[15]:


N_train=1
N_test=100
number_of_epochs=50
agent1_test=None
agent2_test=None


# In[16]:



iteration_count=0
percentage_won_player1=[]
percentage_won_player2=[]
percentage_tie=[]
number_of_iterations=[]

try:

    for i in tqdm(range(number_of_epochs)):

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

except KeyboardInterrupt:
    pass


# In[17]:


print(percentage_won_player1)


# In[18]:


Q1_agent.Q


# ## Export to HTML

# In[19]:


def state2rowmap(Q,player=1):
    states=list(Q.keys())
    state_rowmap={}
    if isinstance(states[0],int):   # use the state as a row
        for state in states:
            state_rowmap[state]=state
            
    else:    
        for i,state in enumerate(Q):
            state_rowmap[state]=i
            
    action_rowmap={}
            
    all_actions=[]
    for i,state in enumerate(Q):
        actions=valid_moves(state,player)
        
        if isinstance(actions[0],int):  # use action as column
            for action in actions:
                action_rowmap[action]=action
                
        else:
            for action in actions:
                if action in rowmap:
                    continue
                action_rowmap[action]=len(action_rowmap)
            
            
    return state_rowmap,action_rowmap
        
    
def state2str(state):
    b=initial_state()
    b.board=state
    
    s=str(b).rstrip()
    
    return s
    


# In[20]:


def learning2html(agent,player,filename):
    from numpy import ones
    from numpy import nan
    from pandas import DataFrame
    
    if '.html' not in filename:
        raise ValueError(f"Needs to be an html file not '{filename}'")
        
    try:
        Q=agent.Q
        table_name='Q'
    except AttributeError:
        Q=agent.T
        table_name='T'
        
    state_rowmap,action_rowmap=state2rowmap(Q,player)
    
    action_row_indices=[action_rowmap[a] for a in action_rowmap]
    all_possible_moves=list(range(max(action_row_indices)+1))
    Qmat=nan*ones((len(agent.Q),len(all_possible_moves)))

    
    if table_name=='Q':
        with open(filename,'w') as fid:

            fid.write("<h1>State Rows</h1>\n")    

            for state in Q1_agent.Q:
                fid.write("<p><strong>Row %d:</strong></p>\n" % state_rowmap[state])
                fid.write(f"<pre>{state2str(state)}</pre>\n")

            Qmat=nan*ones((len(Q1_agent.Q),len(all_possible_moves)))
            df = DataFrame(Qmat, columns=all_possible_moves, index=range(len(Q1_agent.Q)))
            df.index.name = "State #"
            df.columns.name="Actions"            

            s=df.to_html()
            fid.write("<p><strong>Q Table</strong></p>\n")    
            fid.write(s)

            fid.write("\n<hr>\n")       

            count=0
            game=1

            fid.write(f"<p>{Q1_agent.ϵ*100:.2f} percent random moves.<p>\n")
            for Q,last_state,last_action,state,is_random_move,move,reward,status in Q1_agent.saved:

                if state is None:
                    if flag:
                        r_ls=state_rowmap[tuple(last_state)]
                        r_la=action_rowmap[last_action]


                        # Q[last_state][last_action]+=α*(reward - Q[last_state][last_action])

                        fid.write(f"<p>'{status}' Last State {r_ls} Last Action {r_la} Reward {reward}</p>\n")
                        fid.write(f"<p style='text-indent:40px'>Q[{r_ls}][{r_la}]=Q[{r_ls}][{r_la}]+{Q1_agent.α:.2f}*({reward} - Q[{r_ls}][{r_la}])</p>")
                        fid.write(f"<p style='text-indent:50px'>       ={Q[last_state][last_action]:.2g} + {Q1_agent.α:.2f}*({reward}-{Q[last_state][last_action]:.2g})</p>")
                        fid.write(f"<p style='text-indent:50px'>={Q[last_state][last_action] + Q1_agent.α*(reward -Q[last_state][last_action])}</p>\n")

                        flag=False
                    else:
                        newQ=Q


                        Qmat=nan*ones((len(Q1_agent.Q),len(all_possible_moves)))

                        for state in Q:
                            for action in Q[state]:
                                r_s=state_rowmap[tuple(state)]
                                r_m=action_rowmap[action]

                                Qmat[r_s,r_m]=Q[state][action]

                        df = DataFrame(Qmat, columns=all_possible_moves, index=range(len(Q1_agent.Q)))
                        df.index.name = "State #"
                        df.columns.name="Actions"            

                        s=df.to_html()
                        fid.write("<p><strong>Q Table</strong></p>\n")    
                        fid.write(s)
                        fid.write("\n<hr>\n")       



                else:   
                    flag=True

                    if is_random_move:
                        rm="(Random) "
                    else:
                        rm=""



                    if last_state:
                        r_ls=state_rowmap[tuple(last_state)]
                        r_s=state_rowmap[tuple(state)]
                        r_m=action_rowmap[move]
                        r_la=action_rowmap[last_action]


                        fid.write(f"<p>Last State {r_ls} Last Action {r_la} State {r_s} {rm}Move {r_m} Reward {reward}</p>\n")

            #                     Q[last_state][last_action]+=α*(reward +
            #                     γ*max([Q[state][a] for a in Q[state]]) - Q[last_state][last_action])

                        fid.write(f"<p style='text-indent:40px'>Q[{r_ls}][{r_la}]=Q[{r_ls}][{r_la}]+{Q1_agent.α:.2f}*({reward} + {Q1_agent.γ:.2f}*(max(Q[{r_s}]: {[Q[state][a] for a in Q[state]]}) - Q[{r_ls}][{r_la}]))</p>\n")
                        fid.write(f"<p style='text-indent:50px'>={Q[last_state][last_action]:.2g} + {Q1_agent.α:.2f}*({reward} + {Q1_agent.γ:.2f}*({max([Q[state][a] for a in Q[state]])}-{Q[last_state][last_action]:.2g}))</p>\n")
                        fid.write(f"<p style='text-indent:50px'>={Q[last_state][last_action] + Q1_agent.α*(reward + Q1_agent.γ*(max([Q[state][a] for a in Q[state]])-Q[last_state][last_action]))}")
                    else:
                        fid.write("<h1>Game %d</h1>\n" % game)
                        game+=1

                        fid.write(f"<p>State {state_rowmap[tuple(state)]} {rm}Move {action_rowmap[move]}</p>\n")

        print(f"Saved {game} Games to {filename}.")

    else:
        raise ValueError("Skittles not implemented yet.")



# In[21]:


learning2html(Q1_agent,1,'TTT Q Example.html')


# In[ ]:




