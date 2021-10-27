#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('pylab', 'inline')


# In[ ]:


from RobotSim373 import *


# In[ ]:


from RobotSim373.utils import pptx2build


# In[58]:


pptx2build('test robot drawing.pptx')


# In[55]:


def build(robot):
    box1=Box(robot,x=2.90,y=8.57,angle=311.24,width=1.29,height=3.28,name="box1")
    disk2=Disk(robot,x=4.06,y=6.40,angle=0.00,radius=0.86,name="disk2")
    box3=Box(robot,x=7.32,y=10.14,angle=311.24,width=1.29,height=3.28,name="box3")
    box4=Box(robot,x=5.72,y=4.91,angle=311.24,width=1.29,height=3.28,name="box4")

    connect(disk2,box3,'weld')


# In[59]:


def act(t,robot):
    robot['box1'].F=.1


# In[ ]:





# In[60]:


env=Environment(24,24)
robot=Robot(env)
build(robot)


# In[61]:


run_sim(env,act,
        total_time=1000,  # seconds
        dt=1/60,
        dt_display=1,  # make this larger for a faster display
       )


# In[ ]:




