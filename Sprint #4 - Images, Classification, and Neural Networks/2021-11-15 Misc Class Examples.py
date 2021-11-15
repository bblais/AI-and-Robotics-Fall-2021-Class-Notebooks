#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from Game import *


# In[3]:


state=Board(5,7)
for i in range(35):
    if rand()<0.5:
        state[i]=1
        
state


# In[4]:


from RobotSim373 import *


# In[13]:


def build(robot,x=1,y=2,name=None):
    R=1
    disk_center=Disk(robot,x,y,radius=R,name=f'center')
    
    
def monitor(t,robot):
    pass


# In[14]:


def nothing(t,robot):
    return True


# In[15]:


state_machine=StateMachine(
    (nothing,"_end_simulation"),
)


# In[29]:


def random_game_state():
    state=Board(5,7)
    for i in range(35):
        if rand()<0.5:
            state[i]=1
    return state


# In[30]:


env=FrictionEnvironment(30,30)
robot=Robot(env)
build(robot)
robot.controller=Controller(state_machine)
robot.controller.monitor=monitor

state=random_game_state()
for row in range(5):
    for col in range(7):
        x=col*2.5+10
        y=30-row*2.5-10
        print(x,y)
        if state[row,col]:
            Box(env,x=x,y=y,width=1,height=1)


run_sim(env,robot.controller, 
        figure_width=6,
       total_time=100,
       dt_display=.1,  # make this larger for a faster display
       )

print(state)


# In[ ]:




