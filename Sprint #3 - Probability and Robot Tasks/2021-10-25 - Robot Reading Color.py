#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from RobotSim373 import *


# In[3]:


def build(robot):
    box1=Box(robot,x=3,y=9.5,name="right")
    box2=Box(robot,x=3,y=11.5,name="left")

    connect(box1,box2,"weld")

    disk1=Disk(robot,x=2,y=10.5,name="center")

    connect(disk1,box1,"distance")
    connect(disk1,box2,"distance")


# In[8]:


def act(t,robot):

    distance=robot['center'].read_distance()
    color=robot['center'].read_color()
    
    if t<0.5:
        robot['right'].F=2
        robot['left'].F=2
    else:
        robot['right'].F=0
        robot['left'].F=0

    robot.storage += t,distance

    robot.message=color


# In[9]:


env=Environment(24,24)
robot=Robot(env)
build(robot)

run_sim(env,act,
        figure_width=6,
       total_time=13,
       dt_display=0.3,  # make this larger for a faster display
       )


# In[12]:


env=Environment(image='images/stripes1.jpg')
robot=Robot(env)
build(robot)

run_sim(env,act,
        figure_width=6,
       total_time=13,
       dt_display=0.3,  # make this larger for a faster display
       )


# In[13]:


env=Environment(image='images/stripes2.jpg')
robot=Robot(env)
build(robot)

run_sim(env,act,
        figure_width=6,
       total_time=13,
       dt_display=0.3,  # make this larger for a faster display
       )


# In[15]:


env=Environment(image='images/stripes3.png')
robot=Robot(env)
build(robot)

run_sim(env,act,
        figure_width=6,
       total_time=13,
       dt_display=0.3,  # make this larger for a faster display
       )


# In[ ]:




