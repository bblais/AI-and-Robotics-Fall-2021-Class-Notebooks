#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


Card(1,'h')


# In[3]:


Card(13,'h')


# In[4]:


c=Card(13,'h')


# In[5]:


c.rank


# In[6]:


c.suit


# In[7]:


deck=makedeck()
deck


# In[8]:


cards=deal(deck,2)
print(cards)
print(len(deck),deck)


# In[11]:


cards=[Card(13,'h'),Card(9,'s')]
cards


# In[14]:


def score(cards):
    
    total=0
    for card in cards:
        
        if card.rank==13:
            total+=10
        else:
            total+=card.rank
        
    return total


# In[15]:


score(cards)


# In[22]:


for r in range(5):
    dice=random.randint(1,6)
    print(dice)


# In[23]:


dice


# if I want to sum them all up

# In[35]:


total=0
for r in range(5):
    dice=random.randint(1,6)
    total+=dice
    print(dice,total)
    if dice==1:
        total=0
        break

print(total)        


# In[40]:


dice=[random.randint(1,6) for i in range(5)]

dice


# In[41]:


if 1 in dice:
    total=0
else:
    total=sum(dice)


# In[42]:


total


# In[39]:


repeat=True
while repeat:

    repeat=False
    dice=random.randint(1,6)
    print(dice)
    if dice==1:
        pass
    elif dice==2:
        pass
    elif dice==3:
        repeat=True
        
    else:
        pass
    


# In[ ]:





# In[ ]:




