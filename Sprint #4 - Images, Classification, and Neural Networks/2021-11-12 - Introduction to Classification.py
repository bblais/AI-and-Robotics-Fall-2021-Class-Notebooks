#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from classy import *


# In[11]:


data=load_excel('data/iris.xls')


# In[17]:


data=double_moon_data(d=1,N=1000)
plot2D(data)


# In[18]:


data_train=double_moon_data(d=1,N=1000)
data_test=double_moon_data(d=1,N=200)


# In[19]:


summary(data_train)


# In[20]:


plot2D(data_train)


# In[21]:


data_train.vectors


# In[22]:


data_train.vectors.shape


# In[23]:


data_train.targets


# In[24]:


C=NaiveBayes()
C.fit(data_train.vectors,data_train.targets)


# In[26]:


plot2D(data_train,C)
C.plot_centers()


# In[28]:


print("On the training set: ",C.percent_correct(data_train.vectors,data_train.targets))
print("On the test set: ",C.percent_correct(data_test.vectors,data_test.targets))


# ## Naive Bayes

# In[32]:


data_train=double_moon_data(d=-1,N=1000)
data_test=double_moon_data(d=-1,N=200)

C=NaiveBayes()
C.fit(data_train.vectors,data_train.targets)

plot2D(data_train,C)
C.plot_centers()


print("On the training set: ",C.percent_correct(data_train.vectors,data_train.targets))
print("On the test set: ",C.percent_correct(data_test.vectors,data_test.targets))


# ## kNearestNeighbor

# In[33]:


data_train=double_moon_data(d=-1,N=1000)
data_test=double_moon_data(d=-1,N=200)

C=kNearestNeighbor()
C.fit(data_train.vectors,data_train.targets)

plot2D(data_train,C)
#C.plot_centers()


print("On the training set: ",C.percent_correct(data_train.vectors,data_train.targets))
print("On the test set: ",C.percent_correct(data_test.vectors,data_test.targets))


# ## RCE

# In[34]:


data_train=double_moon_data(d=-1,N=1000)
data_test=double_moon_data(d=-1,N=200)

C=RCE()
C.fit(data_train.vectors,data_train.targets)

plot2D(data_train,C)
C.plot_centers()


print("On the training set: ",C.percent_correct(data_train.vectors,data_train.targets))
print("On the test set: ",C.percent_correct(data_test.vectors,data_test.targets))


# ## Images

# In[35]:


images=image.load_images('images/digits')


# In[39]:


images=remap_targets(images,new_target_names=['0','1','2','3','4','5','6','7','8','9'])
summary(images)


# In[40]:


data=image.images_to_vectors(images)


# In[41]:


data.targets


# In[38]:


data.target_names


# In[42]:


data_train,data_test=split(data)


# In[43]:


C=NaiveBayes()
C.fit(data_train.vectors,data_train.targets)



print("On the training set: ",C.percent_correct(data_train.vectors,data_train.targets))
print("On the test set: ",C.percent_correct(data_test.vectors,data_test.targets))


# In[45]:


C.means.shape


# In[49]:


prototype=C.means[4,:]
print(prototype.shape)
prototype


# In[50]:


prototype=prototype.reshape((8,8))


# In[54]:


imshow(prototype,cmap=cm.gray)
colorbar()


# In[ ]:




