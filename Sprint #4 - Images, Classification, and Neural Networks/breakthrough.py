from Game import *
from Game.minimax import *

def initial_state(N=3):
    state=Board(N,N)
    state.pieces=['.','^','v']
    
    for col in range(N):
        state[0,col]=2
        state[N-1,col]=1
        
    return state

def update_state(state,player,move):
    new_state=state
    start,end=move
    new_state[end]=player
    new_state[start]=0
    return new_state

def win_status(state,player):
    N=state.shape[0]
    
    if player==1:
        other_player=2
        goal_row=0
    else:
        other_player=1
        goal_row=N-1
        
    if not valid_moves(state,other_player):
        return 'win'
    

    for col in range(N):
        if state[goal_row,col]==player:
            return 'win'
    
    
def valid_moves(state,player):

    if player==1:
        return state.moves(1,'n,xne,xnw')
    else:
        return state.moves(2,'s,xse,xsw')
    
    return moves

def show_state(state):
    print(state)


def random_move(state,player):
    moves=valid_moves(state,player)
    return random.choice(moves)

def human_move(state,player):
    print("Locations:")
    print("    0 | 1 | 2")
    print("    ---------")
    print("    3 | 4 | 5")
    print("    ---------")
    print("    6 | 7 | 8")
    
    while True:
        
        move=input('What square do you want to move to?')
        move=int(move)

        if move in valid_moves(state,player):
            break
        else:
            print("You messed up!")
    
    return move

human_agent=Agent(human_move)
random_agent=Agent(random_move)

def minimax_move(state,player,info):

    T=info.T
    
    if not state in T:
        values,moves=minimax_values(state,player,display=False)
        move=top_choice(moves,values)
        T[state]=move
    else:    
        move=T[state]
        
    return move


minimax_agent=Agent(minimax_move)
minimax_agent.T=Table()
