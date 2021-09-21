#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[3]:


from mplturtle import *


# In[5]:


def back(length):
    right(180)
    forward(length)
    left(180)


# In[14]:


reset()
for i in range(91):
    forward(50)
    back(50)
    left(10)
    
pencolor('red')
for i in range(91):
    forward(50)
    back(50)
    left(1)    


# In[9]:


def square(size):
    for i in range(4):
        forward(size)
        right(90)


# In[12]:


reset()
for i in range(45):
    
    penup()
    forward(50)
    
    pendown()
    square(10)
    penup()
    back(50)
    
    left(2)


# In[ ]:




