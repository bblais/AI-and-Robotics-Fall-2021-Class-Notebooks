#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[3]:


from RobotSim373 import *
from RobotSim373.utils import pptx2build


# In[8]:


pptx2build('robot motion test.pptx')


# In[9]:


def build(robot):
    disk1=Disk(robot,x=2.27,y=3.35,angle=0.00,radius=0.50,name="disk1")
    box2=Box(robot,x=2.95,y=7.37,angle=329.39,width=0.54,height=3.90,name="box2")
    box3=Box(robot,x=4.94,y=4.20,angle=275.17,width=0.61,height=4.42,name="box3")


# In[11]:


def act(t,robot):
    pass


# In[16]:


env=FrictionEnvironment(image="images/track.png")
robot=Robot(env)
build(robot)


Box(env,x=10,y=10,width=1,height=1)

robot.object_x=10
robot.object_y=10


# In[17]:


run_sim(env,act,
        figure_width=6,
       total_time=30,
       dt_display=0.3,  # make this larger for a faster display
       )


# In[ ]:




