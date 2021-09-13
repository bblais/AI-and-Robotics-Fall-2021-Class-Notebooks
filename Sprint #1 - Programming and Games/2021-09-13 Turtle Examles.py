#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


plot(rand(500))


# In[6]:


pwd


# In[2]:


from mplturtle import *


# In[3]:


reset(figsize=(5,5))
forward(50)
right(90)
forward(70)
left(30)
forward(90)


# # Square

# In[4]:


reset(figsize=(5,5))

forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)


# In[5]:


reset(figsize=(5,5))  # for the class notebooks, including figsize
size=80
forward(size)
right(90)
forward(size)
right(90)
forward(size)
right(90)
forward(size)
right(90)


# In[6]:


reset(figsize=(5,5))  # for the class notebooks, including figsize
size=80

print("start")
for i in range(4):
    forward(size)
    right(90)
    print("here")
print("end")


# In[7]:


reset(figsize=(5,5))  # for the class notebooks, including figsize

size=80

print("start")
for i in range(4):
    forward(size)
    right(90)
    print("here")
print("end")

penup()
forward(200)  # move over
pendown()

size=30
print("start")
for i in range(4):
    forward(size)
    right(90)
    print("here")
print("end")


# In[8]:


def draw_square(size):
    for i in range(4):
        forward(size)
        right(90)
    
def move_over(size):
    penup()
    forward(size)  # move over
    pendown()


# In[13]:


reset(figsize=(5,5))  # for the class notebooks, including figsize

draw_square(80)

move_over(200)

draw_square(30)


# In[14]:


animate()


# In[ ]:




