#!/usr/bin/env python
# coding: utf-8

# # More Features of Python
# 
# ## Strings
# 
# Strings refer to strings of characters, like

# In[1]:


a='hello there'

b="both types of quotes work"

c=a+b

print(c)


# ## File Input/Output
# 
# ## Tid-bits
# 
# In this section I am placing a number of useful techniques which don't
# fall easily into any other categories.
# 
# ### Swapping Two Values
# 
# If I want to swap the values of two variables, it is easiest done by the
# one-liner

# In[2]:


a=4 
b=5
print("a=",a)
print("b=",b)

a,b=b,a

print("a=",a)
print("b=",b)


# ### Looping through List Elements
# 
# One is often in the position of having to go through all of the elements
# of a list, to find the maximum or minimum, or perhaps a certain value.
# The straightforward way of doing it is a for-loop.

# In[3]:


def find3(l):
    # find all of the elements that are equal to 3
    idx=[];  # start the index list equal to empty
    for i in range(len(l)):
        
        if l[i]==3:
            idx.append(i) # tack on the value i to the index vector

    return idx


# used like

# In[4]:


l=[1,3,6,2,5,7,3,5]
find3(l)


# Remember that indices start with 0!
# 
# ### Sorting
# 
# There are a number of ways of sorting a list of numbers. Some algorithms
# are very quick, but are more abstract to implement. A common algorithm
# which is not particularly fast, but is very easy to remember, is called
# the *bubble sort*. To sort in decreasing order, the bubble sort looks
# like:
# 
# The code would look like

# In[5]:


def sortit(x):
    # bubble sort
    y=x[:]  # make a copy of the list
    N=len(y)
    
    swapped=True
    while swapped:
        swapped=False

        for i in range(N-1):
            if y[i]>y[i+1]:
                y[i],y[i+1]=y[i+1],y[i]  # swap
                swapped=True

    return y


# and run like

# In[6]:


l=[1,3,6,2,5,7,3,5]
m=sortit(l)
m


# Of course, there is already a function called `sort` which does just
# that.

# In[7]:


m=l[:]  # copy the list
m.sort()
m


# In[ ]:




