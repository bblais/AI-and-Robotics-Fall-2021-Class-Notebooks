#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from mplturtle import *


# In[3]:


def draw_square(size):
    for i in range(4):
        forward(size)
        right(90)
    
def move_over(size):
    penup()
    forward(size)  # move over
    pendown()


# In[4]:


reset(figsize=(5,5))  # for the class notebooks, including figsize

draw_square(80)

move_over(200)

draw_square(30)


# In[6]:


animate()


# In[9]:


for i in range(5):
    print("here")
    print(i)


# In[10]:


for bob in range(5):
    print("here")
    print(bob)


# In[ ]:




