#!/usr/bin/env python
# coding: utf-8

# ![image.png](attachment:57c7b0a5-d392-48cf-9c7c-2d98acb5c462.png)
# 
# ![image.png](attachment:252d723f-0eb1-46fc-b109-b1010d3e20b6.png)

# - data: $z_1=4, z_2=1$

# ## Sequentially
# 
# 
# ### first the $z_1=4$

# $$
# \begin{align}
# P(\text{open}|z_1=4) &\sim P(z_1=4|\text{open})\cdot P(\text{open})\\
# P(\text{closed}|z_1=4) &\sim P(z_1=4|\text{closed})\cdot P(\text{closed})
# \end{align}
# $$
# 
# pluging in the priors and the values from the graph above
# 
# $$
# \begin{align}
# P(\text{open}|z_1=4) &\sim 0.2\cdot 0.5  = 0.1\\
# P(\text{closed}|z_1=4) &\sim 0.05 \cdot 0.5 = 0.025
# \end{align}
# $$

# In[4]:


numerator1=0.2*0.5
numerator2=0.05*0.5

numerator1,numerator2


# In[5]:


T=numerator1+numerator2
T


# In[7]:


P_open_given_z1_eq_4=numerator1/T
P_closed_given_z1_eq_4=numerator2/T

P_open_given_z1_eq_4,P_closed_given_z1_eq_4


# $$
# \begin{align}
# P(\text{open}|z_1=4) &= 0.2\cdot 0.5/0.125=0.8 \\
# P(\text{closed}|z_1=4) &= 0.05 \cdot 0.5//0.125 = 0.2
# \end{align}
# $$

# ### Now the second reading, $z_2=1$

# $$
# \begin{align}
# P(\text{open}|z_1=4,z_2=1) &\sim P(z_2=1|\text{open},z_1=4)\cdot P(\text{open}|z_1=4)\\
# P(\text{closed}|z_1=4,z_2=1) &\sim P(z_2=1|\text{closed},z_1=4)\cdot P(\text{closed}|z_1=4)
# \end{align}
# $$
# 
# pluging in the priors (which are the posteriors from the previous calculation) and the values from the graph above
# 
# $$
# \begin{align}
# P(\text{open}|z_1=4,z_2=1) &\sim 0.5 \cdot 0.8 = 0.4\\
# P(\text{closed}|z_1=4,z_2=1) &\sim 0.1 \cdot 0.2 = 0.02
# \end{align}
# $$

# In[8]:


numerator1=0.5*0.8
numerator2=0.1*0.2

numerator1,numerator2


# In[9]:


T=numerator1+numerator2
T


# In[10]:


P_open_given_z1_eq_4_z2_eq_1=numerator1/T
P_closed_given_z1_eq_4_z2_eq_1=numerator2/T

P_open_given_z1_eq_4_z2_eq_1,P_closed_given_z1_eq_4_z2_eq_1


# $$
# \begin{align}
# P(\text{open}|z_1=4,z_2=1) &=  0.5 \cdot 0.8 /0.42=0.952 \\
# P(\text{closed}|z_1=4,z_2=1) &= 0.1 \cdot 0.2/0.42=0.048
# \end{align}
# $$

# # Non-sequentially (or all-at-once)

# $$
# \begin{align}
# P(\text{open}|z_1=4,z_2=1) &\sim P(z_2=1|\text{open},z_1=4)\cdot P(\text{open}|z_1=4) ~ P(z_2=1|\text{open},z_1=4)\cdot P(z_1=4|\text{open})P(\text{open})\\
# P(\text{closed}|z_1=4,z_2=1) &\sim P(z_2=1|\text{closed},z_1=4)\cdot P(\text{closed}|z_1=4)~ P(z_2=1|\text{closed},z_1=4)\cdot P(z_1=4|\text{closed})P(\text{closed})
# \end{align}
# $$
# 
# pluging in the priors  and the values from the graph above
# 
# $$
# \begin{align}
# P(\text{open}|z_1=4,z_2=1) &\sim 0.5 \cdot 0.2 \cdot 0.5  = 0.05\\
# P(\text{closed}|z_1=4,z_2=1) &\sim 0.1 \cdot 0.05 \cdot 0.5 = 0.0025
# \end{align}
# $$

# In[11]:


numerator1=0.5*0.2*.5
numerator2=0.1*0.05*0.5

numerator1,numerator2


# In[12]:


T=numerator1+numerator2
T


# $$
# \begin{align}
# P(\text{open}|z_1=4,z_2=1) &= 0.5 \cdot 0.2 \cdot 0.5/0.0525  = 0.0952\\
# P(\text{closed}|z_1=4,z_2=1) &= 0.1 \cdot 0.05 \cdot 0.5/0.0525 = 0.048
# \end{align}
# $$

# In[13]:


numerator1/T


# In[14]:


numerator2/T


# In[ ]:




