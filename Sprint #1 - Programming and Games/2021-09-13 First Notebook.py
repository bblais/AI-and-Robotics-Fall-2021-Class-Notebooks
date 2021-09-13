#!/usr/bin/env python
# coding: utf-8

# In[2]:


5+5


# this is markdown, for notes.  https://www.markdownguide.org/basic-syntax
# 
# # heading
# 
# ## subheading
# 
# - a
# - bulleted
# - list
# 
# some **bold** and *italic*

# # Variables

# In[5]:


a=5
bob=678.5


# In[6]:


bob


# In[7]:


Bob


# In[4]:


a*bob


# In[4]:


checker_board=5


# In[5]:


a


# In[6]:


a=a+2


# In[8]:


a


# In[9]:


sin(30)


# In[13]:


from math import sin,radians


# In[14]:


sin(90)


# In[15]:


sin(3.141592653589793235/2)


# In[16]:


sin(radians(90))


# In[17]:


from math import *


# In[18]:


cos(radians(90))


# In[19]:


def sin(x):
    return 5


# In[20]:


sin(radians(90))


# In[ ]:





# In[ ]:





# In[ ]:





# In[21]:


x=87
y=32



a=656


# In[22]:


import math


# In[23]:


math.__file__


# In[24]:


get_ipython().run_line_magic('pinfo', 'math')


# In[25]:


get_ipython().run_line_magic('pinfo', 'sin')


# # Loops

# In[8]:


for bob in range(5):
    print("here")
    print(bob)


# In[9]:


print('this is outside of the loop')
for bob in range(5):
    print("here in the loop")
    print(bob)
    
print("this is outside of the loop again")


# In[10]:


for j in range(3):
    print("another")
    
print('this is outside of the loop')
for bob in range(5):
    print("here in the loop")
    print(bob)
    
print("this is outside of the loop again")    


# In[11]:


for j in range(3):
    print("another")
    
    print('this is outside of the loop')
    for bob in range(5):
        print("here in the loop")
        print(bob)

    print("this is outside of the loop again")    


# In[12]:


for j in range(3):
    print("another")
    
    print('this is outside of the loop')
for bob in range(5):
    print("here in the loop")
    print(bob)
    
print("this is outside of the loop again")    


# In[ ]:




