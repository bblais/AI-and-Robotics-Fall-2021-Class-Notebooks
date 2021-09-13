#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


plot(rand(500))


# In[6]:


pwd


# In[3]:


from mplturtle import *


# In[5]:


reset(figsize=(5,5))
forward(50)
right(90)
forward(70)
left(30)
forward(90)


# # Square

# In[7]:


reset(figsize=(5,5))

forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)


# In[11]:


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


# In[12]:


reset(figsize=(5,5))  # for the class notebooks, including figsize
size=80

print("start")
for i in range(4):
    forward(size)
    right(90)
    print("here")
print("end")


# In[14]:


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


# In[ ]:




