#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
from mplturtle import *


# ## If-Then

# ![image.png](attachment:18f7d0f4-3350-49f9-a02b-6d9a88ca0506.png)

# In[53]:


def square(size):
    for i in range(4):
        forward(size)
        right(90)
        
def move_over(size):
    penup()
    forward(size)
    pendown()
    
def move_back(size):
    penup()
    backward(size)
    pendown()
    
    
def move_up_row(size):
    right(180)
    move_over(size*5)
    left(180)

    left(90)
    move_over(size)
    right(90)  
    
def draw_row(size,color='black'):
    
    
    for row in range(5):
        pencolor(color)
        square(size)
        move_over(size+5)    
        
        if color=='black':
            color='red'
        else:
            color='black'


# In[21]:


reset()

color='black'
for i in range(5):
    draw_row(20,color)
    move_up_row(25)
    
    if color=='black':
        color='red'
    else:
        color='black'    


# ## Loops

# ![image.png](attachment:72ca77f8-c47d-46fd-91a4-4593d1512e35.png)

# In[24]:


reset()
angle=1
for i in range(90//angle):
    forward(80)
    backward(80)
    left(angle)


# In[25]:


reset()
angle=1
for i in range(270//angle):
    forward(80)
    backward(80)
    right(angle)


# In[26]:


reset()

color="black"

pencolor(color)
angle=1
for i in range(90//angle):
    forward(80)
    backward(80)
    left(angle)
    
color="red"

pencolor(color)
angle=1
for i in range(90//angle):
    forward(80)
    backward(80)
    left(angle)
    


# In[27]:


reset()

color="black"

for color in ["black","red","blue","green"]:
    pencolor(color)
    angle=1
    for i in range(90//angle):
        forward(80)
        backward(80)
        left(angle)
    


# In[28]:


reset()

color="black"
right(30)
for color in ["black","red","blue"]:
    pencolor(color)
    angle=1
    for i in range(120//angle):
        forward(80)
        backward(80)
        left(angle)
    


# ![image.png](attachment:647dad64-185a-438d-9a92-0a8e4f6460ef.png)

# In[29]:


reset()
for i in range(5):
    left(90)
    forward(25)
    right(90)
    forward(25)


# ![image.png](attachment:d5adeca2-9c86-4032-bb65-b7a298f7e1b8.png)

# In[32]:


reset()
square(20)

left(90)
move_over(5)
left(90)
move_over(5)
right(180)

square(30)

left(90)
move_over(5)
left(90)
move_over(5)
right(180)

square(40)


# In[34]:


reset()

for i in range(15):
    # i=0 ==> square(20)
    # i=1 ==> square(30)
    # i=2 ==> square(40)
    
    size=10*i+20
    square(size)

    left(90)
    move_over(5)
    left(90)
    move_over(5)
    right(180)


# In[41]:


reset()

for i in range(15):
    size=10*i+20
    circle(size)

    right(90)
    move_over(5)
    left(90)



# In[ ]:





# ## nested loops

# ![image.png](attachment:8892840a-c240-49bd-82bd-57271d4db122.png)

# In[51]:


def pentagon(size,color):
    pencolor(color)
    for i in range(5):
        forward(size)
        right(72)


# In[58]:


reset()
colors=['blue','red','yellow','green','orange']
distances=[80,60,40,20,10]

for j in range(5):
    color=colors[j]
    distance=distances[j]

    for i in range(90//5*4):
        move_over(distance)
        pentagon(20,color)
        move_back(distance)
        left(5)


# ![image.png](attachment:59716270-b626-4786-b705-bb550013de6c.png)

# In[68]:


reset()

for number_of_blocks in range(12,0,-1):

    for i in range(number_of_blocks):
        square(20)
        move_over(20)

    move_back(20*number_of_blocks)
    move_over(20//2)    
    left(90)
    move_over(20)
    right(90)


# In[67]:


for i in range(12,0,-1):
    print(i)


# In[ ]:




