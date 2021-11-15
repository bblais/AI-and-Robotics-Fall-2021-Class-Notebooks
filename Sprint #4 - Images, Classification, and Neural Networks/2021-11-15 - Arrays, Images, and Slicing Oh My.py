#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[40]:


im=imread('images/cats.jpeg')


# https://www.theverge.com/2021/4/12/22379880/artificial-intelligence-cat-photos-gan
# 
# https://thiscatdoesnotexist.com/
# 
# https://thispersondoesnotexist.com/

# In[41]:


imshow(im)


# In[42]:


im.shape


# In[43]:


arr=(rand(10)*100).round()


# In[21]:


arr


# In[22]:


arr.shape


# In[23]:


arr[3:7]


# In[24]:


arr[0:3]


# In[26]:


arr=(rand(10,4)*100).round()
arr


# In[27]:


arr[3:8,1:3]


# In[28]:


arr[2:5,:]


# In[31]:


imshow(im)


# In[35]:


sub_image=im[400:800,750:1001]


# In[36]:


sub_image.shape


# In[ ]:





# In[34]:


imshow(sub_image)


# select the red channel, I want all rows, cols, and the zeroeth channel

# In[50]:


red=sub_image[:,:,0]
green=sub_image[:,:,1]
blue=sub_image[:,:,2]


# In[51]:


red.shape


# In[54]:


for cat in [red,green,blue]:
    figure()
    imshow(cat)
    colorbar()


# In[55]:


imshow(im)


# In[57]:


sub_im=im[0:400,275:700,:]
sub_im.shape


# In[58]:


imshow(sub_im)


# In[59]:


sub_im=im[0:400,300:700,:]
sub_im.shape


# In[60]:


imshow(sub_im)


# In[62]:


imsave("images/one cat.jpeg",sub_im)


# In[63]:


imshow(im)


# In[79]:


# board coordinates
r=2
c=1


# In[80]:


sub_image_rows=400
sub_image_cols=400


# In[81]:


# image coordinates
start_row=0
start_col=300


# In[82]:


sub_image=im[ start_row:(start_row+sub_image_rows*r) , 
              start_col:(start_col+sub_image_cols*c) ,
              :]  # all the channels
sub_image.shape


# In[83]:


sub_image=im[ (start_row+sub_image_rows*r):(start_row+sub_image_rows*(r+1)) , 
              (start_col+sub_image_cols*c):(start_col+sub_image_cols*(c+1))  ,
              :]  # all the channels
sub_image.shape


# In[84]:


imshow(sub_image)


# In[85]:


sc=start_col
sr=start_row
W=sub_image_cols
H=sub_image_rows


# In[86]:


sub_image=im[ (sr+H*r):(sr+H*(r+1)) , 
              (sc+W*c):(sc+W*(c+1))  ,
              :]  # all the channels
sub_image.shape


# In[87]:


imshow(sub_image)


# saving the cat

# In[88]:


for r in range(3):
    for c in range(3):
        sub_image=im[ (start_row+sub_image_rows*r):(start_row+sub_image_rows*(r+1)) , 
              (start_col+sub_image_cols*c):(start_col+sub_image_cols*(c+1))  ,
              :]  # all the channels
        filename=f"images/cat {r} {c}.jpeg"
        imsave(filename,sub_image)


# In[90]:



count=0
for image_filename in ['images/cats.jpeg','images/cats copy.jpeg','images/cats copy 2.jpeg']:
    im=imread(image_filename)
    print(image_filename)
    for r in range(3):
        for c in range(3):
            sub_image=im[ (start_row+sub_image_rows*r):(start_row+sub_image_rows*(r+1)) , 
                  (start_col+sub_image_cols*c):(start_col+sub_image_cols*(c+1))  ,
                  :]  # all the channels
            filename=f"images/cat {count}.jpeg"
            print("\t",filename)
            
            imsave(filename,sub_image)    
            count+=1


# In[ ]:




