#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *
from RobotSim373 import *


# In[11]:


print("TTT Version: 0.0.3")


# ## Game Functions

# In[3]:


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
    


# In[ ]:


def human_move(state,player):
    
    state.show_locations()
    print("Player",player)
    move=int(input("which square to move?"))
    return move

human_agent=Agent(human_move) 

def random_move(state,player):
    
    move=random.choice(valid_moves(state,player))
    return move


random_agent=Agent(random_move)


# In[10]:


from Game.minimax import *
def minimax_move(state,player):

    values,moves=minimax_values(state,player,display=True)
    return top_choice(moves,values)


# ## Robot Funcs

# In[4]:


def build(robot,name=None):
    R=.5
    r=R/5
    
    
    x=12.5
    y=18
    
    angle=0
    disk_center=Disk(robot,x,y,radius=R,angle=angle,name=f'center NW')

    disks=[]
    for angle in range(0,360,30):
        disk=Disk(robot,
                          x+(R+1.1*r)*cos(radians(angle)),
                          y+(R+1.1*r)*sin(radians(angle)),
                 angle=angle,radius=r,
                 name='disk %d NW' % angle)
        disks.append(disk)

    connect(disk_center,disks,'weld')

    #============
    
    x=17.2
    y=18
    
    angle=0
    disk_center=Disk(robot,x,y,radius=R,angle=angle,name=f'center NE')

    disks=[]
    for angle in range(0,360,30):
        disk=Disk(robot,
                          x+(R+1.1*r)*cos(radians(angle)),
                          y+(R+1.1*r)*sin(radians(angle)),
                 angle=angle,radius=r,
                 name='disk %d NE' % angle)
        disks.append(disk)

    connect(disk_center,disks,'weld')

    #============
    
    x=17.2
    y=13.3
    
    angle=0
    disk_center=Disk(robot,x,y,radius=R,angle=angle,name=f'center SE')

    disks=[]
    for angle in range(0,360,30):
        disk=Disk(robot,
                          x+(R+1.1*r)*cos(radians(angle)),
                          y+(R+1.1*r)*sin(radians(angle)),
                 angle=angle,radius=r,
                 name='disk %d SE' % angle)
        disks.append(disk)

    connect(disk_center,disks,'weld')

    #============
    
    x=12.5
    y=13.3
    
    angle=0
    disk_center=Disk(robot,x,y,radius=R,angle=angle,name=f'center SW')

    disks=[]
    for angle in range(0,360,30):
        disk=Disk(robot,
                          x+(R+1.1*r)*cos(radians(angle)),
                          y+(R+1.1*r)*sin(radians(angle)),
                 angle=angle,radius=r,
                 name='disk %d SW' % angle)
        disks.append(disk)

    connect(disk_center,disks,'weld')

   
    ##  home position
    robot.home_x=3
    robot.home_y=3

    x=robot.home_x
    y=robot.home_y
    
    angle=0
    center=Disk(robot,x,y,radius=R,angle=angle,name=f'center')

    disks=[]
    for angle in range(0,360,30):
        disk=Disk(robot,
                          x+(R+1.1*r)*cos(radians(angle)),
                          y+(R+1.1*r)*sin(radians(angle)),
                 angle=angle,radius=r,
                 name='disk %d' % angle)
        disks.append(disk)

    connect(center,disks,'weld')

    robot.disks=disks
    robot.angles=list(range(0,360,30))
    
    robot.state=None
        


# In[5]:


def pieceX(env,x,y):
    
    boxes=[Box(env,x+.5,y+.5,width=1,height=.2,angle=45,color='blue'),
        Box(env,x-.5,y-.5,width=1,height=.2,angle=45,color='blue'),
        Box(env,x+.5,y-.5,width=1,height=.2,angle=135,color='blue'),
        Box(env,x-.5,y+.5,width=1,height=.2,angle=135,color='blue')
          ]
    
    connect(boxes[0],boxes[1:],"weld")
    
def pieceO(env,x,y):
    
    Disk(env,x=x,y=y,radius=1,color='red')
    


# In[6]:


def north(t,robot):
    robot['disk 90'].F=10
    return True

def south(t,robot):
    robot['disk 90'].F=-10
    return True
    
def east(t,robot):
    robot['disk 0'].F=10
    return True

def west(t,robot):
    robot['disk 0'].F=-10
    return True

def off(t,robot):
    for disk in robot.disks:
        disk.F=0
    return True


def nothing(t,robot):
    return True

def turn_green(t,robot):
    robot.color='g'
    return True

def turn_blue(t,robot):
    robot.color='cyan'
    return True

def turn_orange(t,robot):
    robot.color='orange'
    return True

def turn_red(t,robot):
    robot.color='r'
    return True

def turn_purple(t,robot):
    robot.color='purple'
    return True    


def take_picture(t,robot):
    from time import time
    timestr=str(time()).replace(".","_")
    robot.take_picture(f'images/ttt pics/ttt_robot_{timestr}.jpeg')
    return True    


# In[7]:


def read_state(t,robot):
    
    #angle in range(0,360,30):

    state=Board(3,3)
    
    robot.distances=[]  # for debugging
    for location in range(9):
        
        if location==0:
            sensor='NW'
            angles=range(90,180,30)
        elif location==1:
            sensor='NE'
            angles=range(90,180,30)
        elif location==2:
            sensor='NE'
            angles=range(0,90,30)
        elif location==3:
            sensor='NW'
            angles=range(180,270,30)
        elif location==4:
            sensor='NW'
            angles=range(270,360,30)
        elif location==5:
            sensor='NE' 
            angles=range(270,360,30)
        elif location==6:
            sensor='SW'
            angles=range(180,270,30)
        elif location==7:
            sensor='SW'
            angles=range(270,360,30)
        elif location==8:
            sensor='SE'
            angles=range(270,360,30)
        else:
            raise ValueError("You can't get there from here.")
    
        distances=[]
        for angle in angles:
            name=f'disk {angle} {sensor}'
            distances.append(robot[name].read_distance())

        piece=0
        # check for X
        for d in distances:
            if d>=2 and d<=3:  # any of them between 2 and 3
                piece=1

        if not piece:  #still haven't found which piece
            # check for O
            for d in distances:
                if d<2:
                    piece=2
        
        state[location]=piece
        robot.distances.append(distances)
        
    robot.state=state
    
    return True
        
    
def monitor(t,robot):
    try:
        robot.message=t,robot.move,robot.controller.current_state
    except AttributeError: 
        robot.message=t,None,robot.controller.current_state    
        
    
    


# ## make move state machine actions

# In[8]:


moves=[  
    [(3,27),(10,27),(10,21.5)],  # for move 0
    [(3,27),(14.7,27),(14.7,21.5)],  # for move 1
    [(3,27),(19.5,27),(19.5,21.5)],  # for move 2
]

forward_state_machines=[]
reverse_state_machines=[]

# have to do the reverse ones first, because the forward ones call them

for move in range(3):

    coords=moves[move]
    x0,y0=3,3 # home
    x1,y1=coords[0]
    x2,y2=coords[1]
    x3,y3=coords[2]

    move_reverse=StateMachine(
        ([north,until_xy(x2,y2),turn_purple,off],"west"),
        ([west,until_xy(x1,y2),turn_red,off],"south"),
        ([south,until_xy(x0,x0),turn_orange,off],"_end_simulation"),
    )    

    move_forward=StateMachine(
        ([north,until_xy(x1,y1),turn_purple,off],"east"),
        ([east,until_xy(x2,y2),turn_red,off],"south"),
        ([south,until_xy(x3,y3),turn_orange,off],move_reverse),
    )

    forward_state_machines.append(move_forward)
    reverse_state_machines.append(move_reverse)


move=3
coords=[(3,15.3),(9,15.3)]
x0,y0=3,3 # home
x1,y1=coords[0]
x2,y2=coords[1]

move_reverse=StateMachine(
    ([west,until_xy(x1,y2),turn_red,off],"south"),
    ([south,until_xy(x0,x0),turn_orange,off],"_end_simulation"),
)    

move_forward=StateMachine(
    ([north,until_xy(x1,y1),turn_purple,off],"east"),
    ([east,until_xy(x2,y2),turn_red,off],move_reverse),
)

forward_state_machines.append(move_forward)
reverse_state_machines.append(move_reverse)

# move 4 is an exception
move=4
coords=[(3,15.3),(13.2,15.3)]
x0,y0=3,3 # home
x1,y1=coords[0]
x2,y2=coords[1]

move_reverse=StateMachine(
    ([west,until_xy(x1,y1),turn_red,off],"south"),
    ([south,until_xy(x0,x0),turn_orange,off],"_end_simulation"),
)    

move_forward=StateMachine(
    ([north,until_xy(x1,y1),turn_purple,off],"east"),
    ([east,until_xy(x2,y2),turn_red,off],move_reverse),
)

forward_state_machines.append(move_forward)
reverse_state_machines.append(move_reverse)


def make_block_at_4(t,robot):
    pieceX(robot.env,x=15,y=15.5)
    return True

appear_at_4=StateMachine(
    (make_block_at_4,"_end_simulation"),
)


move=5
coords=[(27,3),(27,15.3),(21,15.3)]
x0,y0=3,3 # home
x1,y1=coords[0]
x2,y2=coords[1]
x3,y3=coords[2]

move_reverse=StateMachine(
    ([east,until_xy(x2,y2),turn_red,off],"south"),
    ([south,until_xy(x1,y1),turn_blue,off],"west"),
    ([west,until_xy(x0,y0),turn_orange,off],"_end_simulation"),
)    

move_forward=StateMachine(
    ([east,until_xy(x1,y1),turn_purple,off],"north"),
    ([north,until_xy(x2,y2),turn_red,off],"west"),
    ([west,until_xy(x3,y3),turn_orange,off],move_reverse),
)

forward_state_machines.append(move_forward)
reverse_state_machines.append(move_reverse)


moves=[  [],[],[],[],[],[],
    [(10,3),(10,9.7)],  # for move 6
    [(14.7,3),(14.7,9.7)],  # for move 7
    [(19.5,3),(19.5,9.7)],  # for move 8
]

for move in range(6,9):

    coords=moves[move]
    x0,y0=3,3 # home
    x1,y1=coords[0]
    x2,y2=coords[1]

    move_reverse=StateMachine(
        ([south,until_xy(x1,y1),turn_purple,off],"west"),
        ([west,until_xy(x0,x0),turn_orange,off],"_end_simulation"),
    )    

    move_forward=StateMachine(
        ([east,until_xy(x1,y1),turn_purple,off],"north"),
        ([north,until_xy(x2,y2),turn_red,off],move_reverse),
    )

    forward_state_machines.append(move_forward)
    reverse_state_machines.append(move_reverse)



# In[9]:


def get_move(t,robot):
    state=robot.state
    # assuming my robot is player 1
    
    #Q=LoadTable("../Sprint #2 - Learning and Simulation/2021-10-18 TTT Q1.json")
    #robot.move=top_choice(Q[state])
    
    robot.move=minimax_move(state,1)
    
    return True

def make_move(t,robot):
    move=robot.move
    
    if move==4 and robot.state[3]:  # something in location 3
        return appear_at_4
    else:
        return forward_state_machines[move]

def monitor(t,robot):
    try:
        robot.message=t,robot.move,robot.controller.current_state
    except AttributeError: 
        robot.message=t,None,robot.controller.current_state    


# In[ ]:


def place_pieces(env):
    x=[10.2,15,19.7,10.2,15,19.7,10.2,15,19.7,]
    y=[20,20,20,15.5,15.5,15.5,11,11,11]



    offset=4
    for i in range(9):
        if i in [0,1,2]:
            pieceX(env,x[i],y[i]+offset)
        elif i in [6,7,8]:
            pieceX(env,x[i],y[i]-offset)
        elif i==3:
            pieceX(env,x[i]-offset,y[i])
        elif i==5:
            pieceX(env,x[i]+offset,y[i])
        elif i==4: # not sure how to deal with the center piece, but I'll solve it later
            pass
        else:
            raise ValueError("You can't get there from here.")


# In[ ]:


def set_up_board(env,state):
    place_pieces(env)


    x=[10.2,15,19.7,10.2,15,19.7,10.2,15,19.7,]
    y=[20,20,20,15.5,15.5,15.5,11,11,11]

    for i in range(9):
        if state[i]==1:
            pieceX(env,x[i],y[i])
        elif state[i]==2:
            pieceO(env,x[i],y[i])
        else:
            pass

