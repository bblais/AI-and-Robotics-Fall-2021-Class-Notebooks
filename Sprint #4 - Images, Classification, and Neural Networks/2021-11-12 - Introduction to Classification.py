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

# In[3]:


images=image.load_images('images/digits')


# In[4]:


images=remap_targets(images,new_target_names=['0','1','2','3','4','5','6','7','8','9'])
summary(images)


# In[5]:


data=image.images_to_vectors(images)


# In[6]:


data.targets


# In[7]:


data.target_names


# In[8]:


data_train,data_test=split(data)


# In[9]:


C=NaiveBayes()
C.fit(data_train.vectors,data_train.targets)



print("On the training set: ",C.percent_correct(data_train.vectors,data_train.targets))
print("On the test set: ",C.percent_correct(data_test.vectors,data_test.targets))


# In[10]:


C.means.shape


# In[11]:


prototype=C.means[4,:]
print(prototype.shape)
prototype


# In[12]:


prototype=prototype.reshape((8,8))


# In[13]:


imshow(prototype,cmap=cm.gray)
colorbar()


# ## making a prediction

# In[15]:


new_image=imread('images/digits/6/1734.png')
imshow(new_image)


# In[16]:


new_image.shape


# In[18]:


new_vector=new_image.reshape(1,64)
new_vector.shape


# In[19]:


C.predict(new_vector)


# In[23]:


target_number=C.predict(new_vector)[0]
target_name=data_train.target_names[target_number]
target_name


# In[24]:


new_vector


# In[26]:


data_train.vectors


# yikes!   the data_train are between 0 and 255, and the vector is from 0 to 1!  No wonder it screwed up.

# solution - rescale either the data, or the new vector

# In[27]:


new_vector=new_vector*255


# In[28]:


target_number=C.predict(new_vector)[0]
target_name=data_train.target_names[target_number]
target_name


# In[ ]:




