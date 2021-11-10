#!/usr/bin/env python
# coding: utf-8

# In[3]:


def factorial(N):
    if N==0:
        return 1
    
    print(f"{N} x factorial({N-1})")
    return N*factorial(N-1)


# In[4]:


factorial(5)


# In[ ]:




