#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from Game import *
from RobotSim373 import *


# In[3]:


from TTT import *


# In[4]:




state_machine=StateMachine(
(read_state,"_end_simulation"),
)


# In[5]:


env=FrictionEnvironment(30,30,image='images/Tic Tac Toe Board With Border.png')
robot=Robot(env)
build(robot)
robot.controller=Controller(state_machine)
robot.controller.monitor=monitor

pieceX(env,10.2,11)
pieceX(env,15,11)
pieceX(env,19.7,11)
pieceX(env,19.7,15.5)
pieceX(env,19.7,20)

pieceO(env,15,20)

run_sim(env,robot.controller, 
        figure_width=6,
       total_time=100,
       dt_display=0.1,  # make this larger for a faster display
       )

robot.state


# In[6]:


state_machine=StateMachine(
    ([read_state,get_move],"make_move"),
    (make_move,"_end_simulation"),
)


# In[7]:


#state=random.choice(list(Q1.keys()))
state=initial_state()

print(state)
# _=input("Pause....hit return to continue, any other key to break.")
# if _:
#     raise ValueError


# In[10]:


env=FrictionEnvironment(30,30,image='images/Tic Tac Toe Board With Border.png')
robot=Robot(env)
build(robot)

robot.controller=Controller(state_machine)
robot.controller.monitor=monitor

set_up_board(env,state)


run_sim(env,robot.controller, 
        figure_width=6,
       total_time=100,
       dt_display=1,  # make this larger for a faster display
       )


# In[ ]:


state=update_state(robot.state,1,robot.move)
show_state(state)

status=win_status(state,1)
if status=='win':
    print("The robot won")
elif status=='lose':
    print("The robot lost")    
elif status=='stalemate':
    print("stalemate")
else:
    pass
    
# human move

if not status:

    move=human_move(state,2)
    state=update_state(state,2,move)

    status=win_status(state,1)
    if status=='win':
        print("The human won")
    elif status=='lose':
        print("The human lost")    
    elif status=='stalemate':
        print("stalemate")
    else:
        pass

    show_state(state)    


# In[ ]:




