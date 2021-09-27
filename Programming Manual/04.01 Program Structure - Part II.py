#!/usr/bin/env python
# coding: utf-8

# # Program Structure - Part II
# 
# Up until this point, everything we have presented is true for
# practically any programming language. They all have a branching
# structure, and a looping structure. They all deal with boolean
# variables, and have some form of function or subroutine structure to
# break up problems into smaller pieces. Now we add lists and dictionaries
# to the mix, and really add a lot of power to our programs.

# ## Lists
# 
# Python supports lists as a basic data structure. For example, you can do

# In[8]:


a=[-4,4,10,-2,20]
print(a)


# In[2]:


a[3]


# In[3]:


a[0]


# In[4]:


a[5]


# Notice that you can access the elements of a list like `a[2]`, and that
# the elements are numbered starting with **0**, not 1. If you try to
# access beyond the length of a list, then an error results.
# 
# When using the multiply operator, `*`, the list gets duplicated. For
# example,

# In[9]:


a=[1]*5
print(a)


# The length of a list is given by the function `len`. This lets you cycle
# through the values of a list easily.

# In[11]:


a=[-4,4,10,-2,20]
for i in range(len(a)):
    if a[i]>0:
        print("The element number ",i," is greater than zero")


# The `for-loop` can more easily be used to loop through the values of the list, rather than looping through the index numbers,

# In[12]:


a=[-4,4,10,-2,20]
for value in a:
    if value>0:
        print("The value ",value," is greater than zero")


# ### A Warning about Copying Lists
# 

# In the way that Python works, if you do:

# In[13]:


a=[1,2,3,4,5]
b=a


# Then `b` is not a copy of `a`, but the **same list** as `a`. Modifying
# `b` also modifies `a`, for example

# In[14]:


a


# In[15]:


b


# In[16]:


b[2]=100


# In[17]:


b


# In[18]:


a


# To avoid this, do the following

# In[20]:


a=[1,2,3,4,5]


# In[21]:


b=a[:]  # make a copy of a


# In[22]:


a


# In[23]:


b


# In[24]:


b[2]=100


# In[25]:


a


# In[26]:


b


# In[ ]:




