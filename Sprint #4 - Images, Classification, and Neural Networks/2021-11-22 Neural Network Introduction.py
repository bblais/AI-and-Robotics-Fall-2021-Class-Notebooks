#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from classy import *


# In[3]:


data_train=double_moon_data(d=-2,N=1000)
data_test=double_moon_data(d=-2,N=200)


# In[4]:


plot2D(data_train)


# In[6]:


C=NumPyNetBackProp({
    'input':2,               # number of features
    'output':(2,'linear'),  # number of classes
    'cost':'mse',
})

# activation functions - linear, tanh (-1 to 1), logistic (0 to 1), relu (min 0, linear)


# In[7]:


C.fit(data_train.vectors,data_train.targets,epochs=3000)


# In[8]:


print((C.predict(data_test.vectors)))
print(("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets)))
print(("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets)))


# In[9]:


plot2D(data_test,classifier=C)


# In[10]:


C=NumPyNetBackProp({
    'input':2,               # number of features
    'hidden':[(15,'logistic'),],
    'output':(2,'logistic'),  # number of classes
    'cost':'mse',
})


# In[11]:


C.fit(data_train.vectors,data_train.targets,epochs=6000)


# In[12]:


print((C.predict(data_test.vectors)))
print(("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets)))
print(("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets)))


# In[13]:


plot2D(data_test,classifier=C)


# In[14]:


C.weights


# In[15]:


set1,set2=C.weights


# In[16]:


set1


# In[18]:


set1.shape


# In[17]:


set2


# ## images

# In[19]:


images=image.load_images('images/digits',verbose=False)
images=remap_targets(images,new_target_names=['0','1','2','3','4','5','6','7','8','9'])
summary(images)


# In[40]:


data=image.images_to_vectors(images)


# In[41]:


data.vectors-=data.vectors.mean()
data.vectors/=data.vectors.std()
summary(data)


# In[42]:


data_train,data_test=split(data)


# In[43]:


# C=NumPyNetBackProp({
#     'input':2,               # number of features
#     'hidden':[(15,'logistic'),],
#     'output':(2,'logistic'),  # number of classes
#     'cost':'mse',
# })


# In[44]:


C=NumPyNetBackProp({
    'input':64,               # number of features
    'hidden':[(20,'logistic'),(13,'logistic'),],
    'output':(10,'logistic'),  # number of classes
    'cost':'mse',
})


# In[45]:


C.fit(data_train.vectors,data_train.targets,epochs=6000)


# In[46]:


print("On the training set: ",C.percent_correct(data_train.vectors,data_train.targets))
print("On the test set: ",C.percent_correct(data_test.vectors,data_test.targets))


# In[47]:


len(C.weights)


# In[ ]:





# In[48]:


weights_ih1,weights_h1h2,weights_h2o=C.weights


# In[49]:


weights_ih1.shape


# In[50]:


weights_h1h2.shape


# In[51]:


weights_h2o.shape


# In[52]:


weights_ih1


# In[53]:


weights_image=weights_ih1[:,0].reshape(8,8)
imshow(weights_image)


# In[54]:


for i in range(20):
    weights_image=weights_ih1[:,i].reshape(8,8)
    subplot(4,5,i+1)
    imshow(weights_image)
    axis('off')


# In[ ]:




