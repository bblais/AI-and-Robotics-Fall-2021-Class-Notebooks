#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from classy import *


# In[12]:


data_train=double_moon_data(d=-2,N=1000)
data_test=double_moon_data(d=-2,N=200)


# In[13]:


plot2D(data_train)


# In[48]:


C=NumPyNetBackProp({
    'input':2,               # number of features
    'output':(2,'linear'),  # number of classes
    'cost':'mse',
})

# activation functions - linear, tanh (-1 to 1), logistic (0 to 1), relu (min 0, linear)


# In[49]:


C.fit(data_train.vectors,data_train.targets,epochs=3000)


# In[50]:


print((C.predict(data_test.vectors)))
print(("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets)))
print(("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets)))


# In[51]:


plot2D(data_test,classifier=C)


# In[66]:


C=NumPyNetBackProp({
    'input':2,               # number of features
    'hidden':[(15,'logistic'),],
    'output':(2,'logistic'),  # number of classes
    'cost':'mse',
})


# In[ ]:


C.fit(data_train.vectors,data_train.targets,epochs=6000)


# In[65]:


print((C.predict(data_test.vectors)))
print(("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets)))
print(("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets)))


# In[ ]:




