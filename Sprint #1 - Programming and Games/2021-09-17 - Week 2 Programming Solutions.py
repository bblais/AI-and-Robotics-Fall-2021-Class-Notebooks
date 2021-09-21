#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
from mplturtle import *


# ## Squares

# ![image.png](attachment:2a12ab44-754c-413c-82c3-25ac6fc88df2.png)

# In[16]:


def square(size):
    for i in range(4):
        forward(size)
        right(90)


# In[19]:


reset()
square(95)


# In[20]:


reset()
square(50)


# ## Houses

# ![image.png](attachment:f4f7d225-af72-407e-9e21-fe2ae6615051.png)

# In[25]:


def house():
    square(50)

    left(60)
    forward(50)
    right(120)
    forward(50)

    left(60)    


# In[27]:


reset()


for i in range(3):
    house()

    penup()
    forward(75)
    pendown()



# In[40]:


def draw_row():
    for i in range(4):
        house()

        penup()
        forward(75)
        pendown()
        
def draw_row_skip():
    for i in range(4):
        
        if i==1:
            penup()
            forward(50)
            pendown()
        elif i==2:
            penup()
            forward(50)
            pendown()            
        else:
            house()

        penup()
        forward(75)
        pendown()
        
def draw_row_skip():
    for i in range(4):
        
        if i==1 or i==2:
            penup()
            forward(50)
            pendown()
        else:
            house()

        penup()
        forward(75)
        pendown()
        
        
def return_left():
    # returns to the left
    left(180)
    forward(4*50+4*75)
    right(180)
    
def next_row():
    # go to the next row
    right(90)
    forward(150)
    left(90)
    pendown()
    


# In[41]:


reset()

draw_row()

penup()
return_left()
next_row()
pendown()

draw_row_skip()

penup()
return_left()
next_row()
pendown()

draw_row()


# ## Shape functions

# ![image.png](attachment:73ee9954-90b4-4ec9-966e-93b07c6b71f6.png)

# In[79]:


def triangle(size):
    for i in range(3):
        forward(size)
        left(180-60)
        
def square(size):
    for i in range(4):
        forward(size)
        left(180-90)   


def polygon(n=5,size=70):
    interior_angle=180-360/n
    for i in range(n):
        forward(size)
        left(180-interior_angle)                    
    
        
def star(size=70):
    n=5
    for i in range(n):
        forward(size)
        left(180-180//n)                


# In[81]:


reset()
polygon(6,70)


# In[70]:


reset()
triangle(70)

square(95)


# In[72]:


reset()
star(70)


# In[82]:


def draw_shape(shape_name,size):
    
    if shape_name=="triangle":
        triangle(size)
    elif shape_name=="square":
        square(size)
    elif shape_name=="star":
        star(size)
    elif shape_name=="pentagon":
        polygon(5,size)
    else:
        print("Bad!")


# In[83]:


reset()
draw_shape("pentagon",30)


# In[ ]:




