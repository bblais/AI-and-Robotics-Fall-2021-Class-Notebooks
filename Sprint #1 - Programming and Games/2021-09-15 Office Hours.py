#!/usr/bin/env python
# coding: utf-8

# In[1]:


def bob():
    print("Bob")
    
def sally():
    print("Sally")


# In[2]:


def do_something(name):
    if name=='bob':
        bob()
    elif name=="sally":
        sally()
    else:
        print("Bad.")


# In[3]:


do_something("bob")


# In[ ]:




