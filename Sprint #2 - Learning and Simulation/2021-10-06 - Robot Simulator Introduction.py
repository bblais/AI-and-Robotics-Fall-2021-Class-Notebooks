#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from RobotSim373 import *


# * Physics is simulated in two dimensions
# * Everything is made up of rectangles (Box) or circular disks (Disk)
# * There are objects associated with the robot and objects which just exist in the world
# * Objects can be connected in different ways:
#     1. "weld" - objects are hard-connected together
#     2. "distance" - objects are constrained to be at a constant distance but can otherwise move independently
#     3. "revolve" - objects are kept at a constant relative position, but can spin freely
# * Robot objects can have a force applied to them, always in the direction they face
# * Gravity is assumed to be zero, unless otherwise specified

# ## Minimum functions

# In[3]:


def build(robot):
    Box(robot,x=5,y=8,width=2,height=1,name="bob")

def act(t,robot):
    robot['bob'].F=3


# ## Making an Environment and Running

# In[5]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
build(robot)

run_sim(env,act,
        figure_width=6,
        total_time=20,  # seconds
        dt_display=.1,  # make this larger for a faster display
       )


# In[9]:


def build(robot):
    Box(robot,x=5,y=8,width=2,height=1,name="bob")
    Box(robot,x=5,y=15,width=1,height=1,name="sally")

def act(t,robot):
    robot['bob'].F=1
    robot['sally'].F=1


# In[16]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
build(robot)


Box(env,x=15,y=10,height=15,width=.1)

run_sim(env,act,
        figure_width=6,
        total_time=20,  # seconds
        dt_display=.1,  # make this larger for a faster display
       )


# In[30]:


def build(robot):
    bob=Box(robot,x=5,y=8,width=2,height=1,name="bob")
    sally=Box(robot,x=5,y=15,width=1,height=1,name="sally")
    fred=Disk(robot,x=5,y=10,radius=.3,name="fred")
    #connect(bob,sally,"weld")
    connect(bob,sally,"distance")
    connect(fred,sally,"weld")
    
    
def act(t,robot):
    robot['bob'].F=1
    robot['sally'].F=3
    robot['fred'].F=-2


# In[31]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
build(robot)


Box(env,x=15,y=10,height=15,width=.1)

run_sim(env,act,
        figure_width=6,
        total_time=10,  # seconds
        dt_display=.1,  # make this larger for a faster display
       )


# In[44]:


def build(robot):
    bob=Box(robot,x=5,y=8,width=2,height=1,name="bob")
    
    
def act(t,robot):
    
    if robot['bob'].x<11:
        robot['bob'].F=1
    else:
        robot['bob'].F=-1

    robot.message='%.2f' % robot['bob'].vx


# In[45]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
build(robot)


#Box(env,x=15,y=10,height=15,width=.1)

run_sim(env,act,
        figure_width=6,
        total_time=60,  # seconds
        dt_display=.1,  # make this larger for a faster display
       )


# ## ".F" is a force - linear motion, ".τ" is a torque - rotational motion
# 
# - type \tau and hit TAB

# In[48]:


def build(robot):
    bob=Box(robot,x=5,y=8,width=2,height=1,name="bob")
    
    
def act(t,robot):
    
    robot['bob'].τ=.1

    robot.message='%.2f' % robot['bob'].vx


# In[49]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
build(robot)


#Box(env,x=15,y=10,height=15,width=.1)

run_sim(env,act,
        figure_width=6,
        total_time=60,  # seconds
        dt_display=.1,  # make this larger for a faster display
       )


# In[50]:


def build(robot):
    bob=Box(robot,x=5,y=8,width=2,height=1,name="bob")
    
    
def act(t,robot):
    
    bob=robot['bob']
    
    bob.F=.1

    distance=bob.read_distance()
    robot.message='%.2f' % distance


# In[52]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
build(robot)


Box(env,x=15,y=10,height=15,width=.1)

run_sim(env,act,
        figure_width=6,
        total_time=60,  # seconds
        dt_display=.1,  # make this larger for a faster display
       )


# In[55]:


def build(robot):
    bob=Box(robot,x=5,y=8,width=2,height=1,name="bob")
    
    
def act(t,robot):
    
    bob=robot['bob']
    
    bob.F=.1

    distance=bob.read_distance()
    
    if distance<2:
        bob.F=-4
    
    robot.message='%.2f' % distance


# In[56]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
build(robot)


Box(env,x=15,y=10,height=15,width=.1)

run_sim(env,act,
        figure_width=6,
        total_time=60,  # seconds
        dt_display=.1,  # make this larger for a faster display
       )


# In[ ]:




