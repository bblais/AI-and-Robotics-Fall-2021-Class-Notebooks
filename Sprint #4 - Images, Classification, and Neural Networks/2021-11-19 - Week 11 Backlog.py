#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('pylab', 'inline')


# In[3]:


from Game import *
from RobotSim373 import *


# In[4]:


from TTT import *


# ## take at least 20 pics of your board in various mid-game positions.

# In[32]:


def take_picture(t,robot):
    from time import time
    timestr=str(time()).replace(".","_")
    image_filename=f'images/ttt pics/ttt_robot_{timestr}.jpeg'
    robot.take_picture(image_filename)
    robot.image_filename=image_filename  # save the last name
    
    return True    


def random_TTT_game_state():
    Q=LoadTable('../Sprint #2 - Learning and Simulation/2021-10-18 TTT Q1.json')    
    keys=list(Q.keys())
    state=Board(3,3)
    state.board=random.choice(keys)
    return state
    
state_machine=StateMachine(
    (take_picture,"_end_simulation"),
)
    


# In[33]:


env=FrictionEnvironment(30,30,image='images/Tic Tac Toe Board With Border.png')
robot=Robot(env)
build(robot)
robot.controller=Controller(state_machine)
robot.controller.monitor=monitor

state=random_TTT_game_state()
set_up_board(env,state)

run_sim(env,robot.controller, 
        figure_width=6,
       total_time=100,
       dt_display=0.1,  # make this larger for a faster display
       )


# In[11]:


for i in range(30):
    env=FrictionEnvironment(30,30,image='images/Tic Tac Toe Board With Border.png')
    robot=Robot(env)
    build(robot)
    robot.controller=Controller(state_machine)
    robot.controller.monitor=monitor

    state=random_TTT_game_state()
    set_up_board(env,state)

    run_sim(env,robot.controller, 
            figure_width=6,
           total_time=100,
           dt_display=0.1,  # make this larger for a faster display
           )

    


# ## show how to slice the image into its individual playing squares

# In[34]:


fname='images/ttt pics/random board pics/ttt_robot_1637076443_4151511.jpeg'


# In[35]:


im=imread(fname)
imshow(im)
im.shape


# ### select the board out of this

# In[17]:


board_im=im[55:375,65:375]
imshow(board_im)


# ### select sub-squares

# In[31]:


start_row=77
start_col=79
sub_image_rows=50
sub_image_cols=50


count=1
for r in range(3):
    for c in range(3):
        sub_image=board_im[ (start_row+sub_image_rows*r):(start_row+sub_image_rows*(r+1)) , 
                      (start_col+sub_image_cols*c):(start_col+sub_image_cols*(c+1))  ,
                      :]  # all the channels
        
        subplot(3,3,count)
        imshow(sub_image)
        count+=1


# ## write a function which takes a board image and the row,col of a square and returns the sub-image of that square

# In[36]:


def board_square_image(im,r,c):
    if isinstance(im,str):
        im=imread(im)
        
    board_im=im[55:375,65:375]    
    
    
    start_row=77
    start_col=79
    sub_image_rows=50
    sub_image_cols=50

    sub_image=board_im[ (start_row+sub_image_rows*r):(start_row+sub_image_rows*(r+1)) , 
                  (start_col+sub_image_cols*c):(start_col+sub_image_cols*(c+1))  ,
                  :]  # all the channels
    
    
    return sub_image


# In[38]:


count=1
for r in range(3):
    for c in range(3):
        sub_image=board_square_image(im,r,c)
        
        subplot(3,3,count)
        imshow(sub_image)
        count+=1


# In[39]:


from glob import glob


# In[40]:


board_pics=glob('images/ttt pics/random board pics/*.jpeg')
print(len(board_pics))


# In[41]:


im=imread(random.choice(board_pics))
imshow(im)


# In[42]:


count=1
for r in range(3):
    for c in range(3):
        sub_image=board_square_image(im,r,c)
        
        subplot(3,3,count)
        imshow(sub_image)
        count+=1


# ## make a folder of sample square images from your board images for "blank", "piece 1" and "piece 2"
# 
# I'll reuse the random state board code here.  I don't need to save in different filenames, so redo the take picture too.

# In[43]:


def take_picture(t,robot):
    image_filename=f'images/ttt pics/board.jpeg'
    robot.take_picture(image_filename)
    robot.image_filename=image_filename  # save the last name
    
    return True    


state_machine=StateMachine(
    (take_picture,"_end_simulation"),
)
    


# In[50]:


folders=[
    'images/ttt pics/training pieces/_',
    'images/ttt pics/training pieces/X',
    'images/ttt pics/training pieces/O',
        ]


# In[57]:


count=0
for i in range(11):
    env=FrictionEnvironment(30,30,image='images/Tic Tac Toe Board With Border.png')
    robot=Robot(env)
    build(robot)
    robot.controller=Controller(state_machine)
    robot.controller.monitor=monitor

    state=random_TTT_game_state()
    set_up_board(env,state)

    run_sim(env,robot.controller, 
            figure_width=6,
           total_time=100,
           dt_display=0.1,  # make this larger for a faster display
           )

    
    im=imread(robot.image_filename)    
    
    for r in range(3):
        for c in range(3):
            sub_image=board_square_image(im,r,c)
    
            folder=folders[state[r,c]]
            filename=folder+f"/square{count}.jpeg"
            imsave(filename,sub_image)
            print(filename)
            count+=1
    


# ## run a classification algorithm on your square images to determine what the square contains

# In[1]:


from classy import *


# In[60]:


images=image.load_images('images/ttt pics/training pieces')
images=remap_targets(images,new_target_names=['_','X','O'])
summary(images)


# In[61]:


data=image.images_to_vectors(images)


# In[62]:


C=NaiveBayes()
C.fit(data.vectors,data.targets)


# ### make a random board, slice it, and classify each piece

# In[68]:


env=FrictionEnvironment(30,30,image='images/Tic Tac Toe Board With Border.png')
robot=Robot(env)
build(robot)
robot.controller=Controller(state_machine)
robot.controller.monitor=monitor

state=random_TTT_game_state()
set_up_board(env,state)

run_sim(env,robot.controller, 
        figure_width=6,
       total_time=100,
       dt_display=0.1,  # make this larger for a faster display
       )


im=imread(robot.image_filename)    

count=1
for r in range(3):
    for c in range(3):
        sub_image=board_square_image(im,r,c)
        vector=atleast_2d(sub_image.ravel())
        prediction=C.predict(vector)
        subplot(3,3,count)
        imshow(sub_image)
        title(prediction)
        axis('off')
        count+=1


# In[ ]:




