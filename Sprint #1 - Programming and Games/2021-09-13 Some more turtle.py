#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from mplturtle import *


# In[3]:


reset()
size=50
for i in range(4):
    forward(size)
    right(90)


# In[9]:


animate(0,4)  # zero delay, and skip every 4 steps to make it faster


# In[ ]:





# In[15]:


def draw_square(size):
    for i in range(4):
        forward(size)
        right(90)
    
def move_over(size):
    penup()
    forward(size)  # move over
    pendown()


# In[16]:


reset(figsize=(5,5))  # for the class notebooks, including figsize

draw_square(80)

move_over(200)

draw_square(30)


# In[17]:


reset(figsize=(5,5))  # for the class notebooks, including figsize

draw_square(80)

penup()
left(90)
forward(50)
right(90)
pendown()

draw_square(20)


# In[18]:


def up(distance):
    penup()
    left(90)
    forward(distance)
    right(90)
    pendown()    


# In[20]:


reset(figsize=(5,5))  # for the class notebooks, including figsize

draw_square(80)

up(50)

pencolor("red")
draw_square(20)


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


# In[21]:


draw_shape(30,"square")


# In[22]:


def myfunction(one,two):
    print(one)
    print(two)


# In[25]:


myfunction(5,"hello")


# In[24]:


myfunction(5)


# In[26]:


def myfunction(one,two):
    print(one)
    if two=="hello":
        print("yay!")
    else:
        print("nay!")


# In[27]:


myfunction(5,"hello")


# In[28]:


myfunction(5,"bob")


# In[ ]:




