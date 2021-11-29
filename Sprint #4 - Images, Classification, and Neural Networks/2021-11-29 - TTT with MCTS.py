#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from TTT import *


# In[3]:


from Game.mcts import *
def mcts_move(state,player,info):
    T=info.T
    values,moves=mcts_values(state,player,T,info.seconds)
    return top_choice(moves,values)

mcts_agent=Agent(mcts_move)
mcts_agent.T=LoadTable(filename='mcts_data_TTT.json')
mcts_agent.seconds=1


# In[4]:


g=Game()
g.display=True
wins=g.run(mcts_agent,random_agent)
g.report()

SaveTable(mcts_agent.T,filename='mcts_data_TTT.json')


# In[5]:


mcts_agent.T


# In[ ]:




