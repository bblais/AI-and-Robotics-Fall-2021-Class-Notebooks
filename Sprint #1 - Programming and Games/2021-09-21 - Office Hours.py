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


# In[15]:


from Game import *


# In[24]:


state=Board(4,5)
for location in range(20):
    print(location)
    state[location]=1
    print(state)
    
state


# In[23]:


for x in ['bob','fred',5,'sally']:
    print("---")
    print(x)
    print("here")
    print("----")
    print()


# In[21]:


list(range(5))


# In[31]:


for c in range(2,5):
    print(c)
    for r in range(1,4):
        print("\t",r)


# In[29]:


for c in range(2,5):
    print(c)
for r in range(1,4):
    print("\t",r)


# In[27]:


state=Board(4,5)

for c in range(2,5):
    for r in range(1,40):

        print(r,c)
        state[r,c]=1
        print(state)
    
state


# In[33]:


state=Board(4,5)

for c in range(5):
    for r in range(4):

        state[r,c]=1
    
state


# In[34]:


update_state(state,1,10)


# In[ ]:




