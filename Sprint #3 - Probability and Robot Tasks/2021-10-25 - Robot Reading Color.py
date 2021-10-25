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


# In[10]:


def act(t,robot):

    color=robot['center'].read_color()
    
    if t<0.5:
        robot['right'].F=2
        robot['left'].F=2
    else:
        robot['right'].F=0
        robot['left'].F=0

    robot.message=color


# In[11]:


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


# In[8]:


env=Environment(image='images/stripes2.jpg')
robot=Robot(env)
build(robot)

run_sim(env,act,
        figure_width=6,
       total_time=13,
       dt_display=0.3,  # make this larger for a faster display
       )


# In[16]:


env=Environment(image='images/stripes3.png')
robot=Robot(env)
build(robot)

run_sim(env,act,
        figure_width=6,
       total_time=13,
       dt_display=0.3,  # make this larger for a faster display
       )


# In[17]:


color=robot['center'].read_color()


# In[18]:


color


# In[19]:


r,g,b,a=color


# In[20]:


r


# In[23]:


g


# In[24]:


b


# In[25]:


a


# In[26]:


if b>.75 and g<0.1 and r<.1:
    print("blue!")


# In[ ]:





# In[38]:


def act(t,robot):

    color=robot['center'].read_color()
    r,g,b,a=color  # assuming I'm reading a png
    
    if b>.75 and g<0.4 and r<.3:  # blue!
        robot['right'].F=-1
        robot['left'].F=-1
    else:
        robot['right'].F=.2
        robot['left'].F=.2


    robot.message=color


# In[39]:


env=Environment(image='images/colors.png')
robot=Robot(env)
build(robot)

run_sim(env,act,
        figure_width=6,
       total_time=50,
       dt_display=0.3,  # make this larger for a faster display
       )


# In[ ]:




