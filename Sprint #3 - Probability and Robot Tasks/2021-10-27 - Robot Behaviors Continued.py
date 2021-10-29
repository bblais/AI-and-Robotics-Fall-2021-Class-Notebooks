#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from RobotSim373 import *


# Let's say we have a track like:
# 
# <img src="images/track.png" width=30%>
# 
# and I want to start by moving until I am inside, and then once inside stay inside.  I can think of this in terms of two behaviors:
# 
# 1. approach to get inside the track
# 2. wander, but keep in the track
# 
# But these can br broken up into smaller pieces
# 
# 1. approach to get inside the track
#     1. go forward
#     2. look for black
#     3. once I see black switch to looking for white
#     4. once I see white I'm inside, so do the wander task
# 2. wander, but keep in the track
#     1. go forward
#     2. look for black
#     3. once I see black, do avoidance behavior, then back to go forward
#     
# where the avoidance behavior might be:
# 
# 1. switch to moving back for a short time/distance
# 2. rotate randomly for a short time/distance
# 
# 

# In[3]:


def build(robot):
    box=Box(robot,x=3,y=12,name="sally")


# In[4]:


def act(t,robot):
    pass


# ## Do the finite state machine
# 
# ### test each piece individually -- start with a couple of the tasks for the approach behavior

# In[5]:


def forward(t,robot):
    robot['sally'].F=10
    return True


# In[6]:


def until_black(t,robot):
    color=robot['sally'].read_color()
    
    r,g,b,a=color
    
    if r<0.2 and g<0.2 and b<0.2:
        return True
    else:
        return False


# In[ ]:





# In[ ]:





# In[22]:


def monitor(t,robot):
    r,g,b,a=robot['sally'].read_color()
    robot.message='%.2f %.2f %.2f %.2f' % (r,g,b,a)


# In[23]:


state_machine_approach=StateMachine(
    (forward,'until_black'),
    (until_black,'_end_simulation'),
)


# In[ ]:





# In[9]:


env=FrictionEnvironment(image="images/track.png")
robot=Robot(env)
build(robot)
robot.controller=Controller(state_machine_approach)
robot.controller.monitor=monitor


run_sim(env,robot.controller,
        figure_width=6,
       total_time=13,
       dt_display=0.3,  # make this larger for a faster display
       )


# ### Do a few more behaviors

# In[10]:


def until_white(t,robot):
    color=robot['sally'].read_color()
    
    r,g,b,a=color
    
    if r>0.5 and g>0.5 and b>0.5:
        return True
    else:
        return False


# In[ ]:





# In[11]:


state_machine_approach=StateMachine(
    (forward,'until_black'),
    (until_black,'until_white'),
    (until_white,'_end_simulation'),
    
)


# In[12]:


env=FrictionEnvironment(image="images/track.png")
robot=Robot(env)
build(robot)
robot.controller=Controller(state_machine_approach)
robot.controller.monitor=monitor


run_sim(env,robot.controller,
        figure_width=6,
       total_time=13,
       dt_display=0.3,  # make this larger for a faster display
       )


# ### now the wander behavior
# 
# Make sure we start inside the track to test this one, so I modify the build function

# In[13]:


def build(robot):
    box=Box(robot,x=8,y=12,name="sally")


# In[19]:


def reverse_for_a_bit(t,robot):
    robot['sally'].F=-5
    if t>1:
        robot['sally'].F=0
        return True
    
def turn_for_a_bit(t,robot):
    robot['sally'].τ=1
    if t>1:
        robot['sally'].τ=0
        return True    


# In[24]:


state_machine_wander=StateMachine(
    (forward,'until_black'),
    (until_black,'reverse_for_a_bit'),
    (reverse_for_a_bit,'turn_for_a_bit'),
    (turn_for_a_bit,'forward'),
)


# In[25]:


env=FrictionEnvironment(image="images/track.png")
robot=Robot(env)
build(robot)
robot.controller=Controller(state_machine_wander)
robot.controller.monitor=monitor


run_sim(env,robot.controller,
        figure_width=6,
       total_time=13,
       dt_display=0.3,  # make this larger for a faster display
       )


# ### Putting it together
# 
# back to the original location

# In[26]:


def build(robot):
    box=Box(robot,x=3,y=12,name="sally")


# In[30]:


state_machine_wander=StateMachine(
    (forward,'until_black'),
    (until_black,'reverse_for_a_bit'),
    (reverse_for_a_bit,'turn_for_a_bit'),
    (turn_for_a_bit,'forward'),
)



state_machine_approach=StateMachine(
    (forward,'until_black'),
    (until_black,'until_white'),
    (until_white,'state_machine_wander'),)
    
)


# In[ ]:




