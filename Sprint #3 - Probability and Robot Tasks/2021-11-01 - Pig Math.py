#!/usr/bin/env python
# coding: utf-8

# ![image.png](attachment:c9e6e507-f00d-4ab3-8e1c-031502657bbd.png)

# In[39]:


from functools import lru_cache
import sys
sys.setrecursionlimit(25000)


# In[49]:


@lru_cache(maxsize=None)
def P(i,j,k,action=None):
    # i = player's score
    # j = opponent's score
    # k = turn score
    # action = "roll", "hold", None
    
    progressive=True
    goal=100
    
    if action is None:
        if i+k>=goal:
            return 1.0  # certain I've won
        
        if j>=goal:
            return 0.0  # certain I've lost
        
        return max(P(i,j,k,"roll"),P(i,j,k,"hold"))
    
    if action == "hold":  # may have to do "progressive Pig" here
        if k==0 and progressive:  # progressive pig
            k=1
            
        return 1-P(j,i+k,0)
    elif action == "roll":
        prob=1/6*P(i,j,k+2) + 1/6*P(i,j,k+3) + 1/6*P(i,j,k+4) + 1/6*P(i,j,k+5) + 1/6*P(i,j,k+6)
        
        if progressive:  # progressive pig
            add=1
        else:
            add=0

        prob+= 1/6*(1-P(j,i+add,0))  # progressive pig
        return prob
        
    else:
        raise ValueError("You can't get there from here.  "+str(action))
    


# In[50]:


P(99,99,0)


# In[51]:


get_ipython().run_line_magic('pylab', 'inline')


# In[53]:


im=zeros((100,100))


# In[55]:


for i in range(100):
    for j in range(100):
        im[i,j]=P(i,j,0)


# In[57]:


imshow(im)
colorbar()


# In[59]:


from Game import Storage


# In[58]:


P(0,0,0)


# In[70]:


S=Storage()
for k in range(30):
    S+=k,P(0,0,k,"roll"),P(0,0,k,"hold")
    
k,Pr,Ph=S.arrays()


# In[72]:


plot(k,Pr,'-o',label="roll")
plot(k,Ph,'-s',label="hold")
xlabel("turn total")
ylabel('probability of a win with 0,0')
legend()


# In[73]:


S=Storage()
for k in range(30):
    S+=k,P(90,90,k,"roll"),P(90,90,k,"hold")
    
k,Pr,Ph=S.arrays()


# In[74]:


plot(k,Pr,'-o',label="roll")
plot(k,Ph,'-s',label="hold")
xlabel("turn total")
ylabel('probability of a win with 90,90')
legend()


# In[ ]:




