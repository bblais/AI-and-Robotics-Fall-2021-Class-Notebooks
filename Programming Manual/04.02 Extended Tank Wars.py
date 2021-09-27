#!/usr/bin/env python
# coding: utf-8

# ## Extended Example: Tank Wars with N Players
# 
# If we wanted to extend our previous tank wars example from 2 players to
# any amount of players, we would have to make some organizational changes
# to reflect multiple players. In this version, the wind speed will be set
# randomly each turn, not just at the beginning of the game.

# - Get Number of Players 
# - Get The Tank Positions 
# - While No One Has Won
#     - Set Wind Speed 
#     - Display The Tank Positions and Wind Speed 
#     - For Each Surviving Player... 
#         - Get Their Angle and Speed 
#         - Get Where Each Shot Landed 
#     - Display Where Each Shot Landed 
#     - Determine Who Has Been Destroyed, If Anyone 
#     - Determine Who Has Won, If Anyone 
# - Display Who Won
# 
# Almost all of the structure will be the same as the 2 player game. To
# get the number of players, we can use the same structure as we used
# before for getting values typed in by the user
# 

# In[6]:


def get_number_of_players():
    N=int(input('How many players? '))

    if N<=1:
        raise ValueError('Illegal number of players')

    return N


# To get the tank positions, we choose random numbers from 0 to 1000. We
# need `N` of them, so we want to make a list of length `N` (using the
# ` *` operator), and then filling in the values using `random()`
# to make a random values containing values from 0 to 1. We can then
# multiply by 1000 to get the positions.

# In[7]:


def get_tank_positions(N):
    from random import random
    
    pos=[0]*N   # make a list of length N, with zeros

    # fill in all the values with random numbers
    for i in range(N):
        pos[i]=random()*1000.0

    return pos


# In[8]:


get_tank_positions(5)


# Next we must write out how we do For Each Surviving Player. Somehow we
# need to keep track of which players are dead, and only ask for input
# from non-dead players. To do this, let's make another list, called
# `isdead`, which is `False` for all alive players and `True` for all dead
# players. Then

# - While No One Has Won 
#     - Set Wind Speed 
#     - Display The Tank Positions and Wind Speed 
#     - For Each Surviving Player... 
#         - Get Their Angle and Speed
#         - Get Where Each Shot Landed 
#     - Display Where Each Shot Landed 
#     - Determine Who Has Been Destroyed, If Anyone 
#     - Determine Who Has Won, If Anyone
# - Display Who Won 
# 
# Changes to 
# 
# - Initialize `isdead` List to all Zeros
# - While No One Has Won 
#     - Set Wind Speed 
#     - Display The Tank Positions and Wind Speed 
#     - For Each Player... 
#         - If the Player is Not Dead... 
#             - Get Their Angle and Speed 
#         - Get Where Each Shot Landed 
#     - Display Where Each Shot Landed 
#     - Determine Who Has Been Destroyed, If Anyone 
#     - For all of those destroyed, set `isdead` to `True` 
#     - Determine Who Has Won, If Anyone 
# - Display Who Won

# The statement Get Where Each Shot Landed in this case will be translated
# to Make a List of Positions of Where Each Player's Shot Landed. This is
# the sum of the previously written function `get_shot_distance` and the
# current tank position. The inner-most loop now becomes

# ```python
# for player in range(N):
#             
#     # get all of the angles and speeds
# 
#     if not isdead[player]:
#         [angle,speed]=get_angle_and_speed(player)
# 
#         distance=get_shot_distance(angle,speed,wind_speed)
# 
#         # make a list with all of the places the shots landed
#         shot_pos[player]=tank_pos[player]+distance
# ``` 

# We have to update the `get_angle_and_speed` function to accept angles
# from 0 to 180, instead of from 0 to 90, so the tanks can fire both to
# the right and to the left. In that function
# 
# ```python
# if (angle<0) or (angle>90): # illegal angles
# ```
# 
# becomes
# 
# ```python
# if (angle<0) or (angle>180): # illegal angles
# ```
# 
# 

# To Determine Who Has Been Destroyed, If Anyone, we must go through all
# players (the same type of loop), and check to see if any of the shots
# were within range. We should make a function, called `isdestroyed`, to
# return `True` if the tank is destroyed. What information does this
# function need? It certainly needs to know which tank we are testing to
# see if it is destroyed, the positions of the tanks, the positions of the
# shots, and which tanks are dead. Thus, it's syntax should be something
# like ` isdestroyed(player,tank_pos,shot_pos,isdead)`. A dead tank should
# return `False`.

# In[10]:


def isdestroyed(current_player,tank_pos,shot_pos,isdead):

    if isdead[current_player]:
        return False # a dead one cannot be destroyed

    N=len(tank_pos)

    for player in range(N):  # players numbered from 0 to N-1
        if not isdead[player]:  # did the player's shot hit the current player?
            if abs(shot_pos[player]-tank_pos[current_player])<10: # a hit
                return True


    # if you've gotten this far past the loop, then you're not destroyed

    return False


# Notice how we obtained the value for `N` in the function. Since we can't
# use `N` without assigning it a value, we could have passed the value of
# `N` as a parameter. Instead (just to make one less parameter) we
# determined `N` from the properties of the other parameters, namely the
# length of the tank position list. This saves us one more parameter to
# pass, and makes the code a bit cleaner.
# 
# To print out the tank positions, what we need to do is to go through all
# of the players, print one message for the ones which are dead
# (` isdead(player)`), and another for those that are still surviving.
# 

# In[11]:


def print_tank_positions(pos,isdead):
    N=len(pos)

    for player in range(N):
        if isdead[player]:
            print('Player ',player,' is dead.')
        else:
            print('Player ',player,' is at position ',pos[player],'.')


# A very similar function for printing the shot positions, except we don't
# have to write anything for those dead tanks, only the ones that are not
# dead.

# In[12]:


def print_shot_positions(pos,isdead):

    N=len(pos)

    for player in range(N):
        if not isdead[player]:
            print('Shot for player ',player,' landed at position ',pos[player],'.')


# How do we determine if there is a winner? Logically, it means that there
# is only one survivor. How do we determine this from the variables we
# have? If we could count the number of `True` values in the `isdead`
# list, that would be the number of tanks killed. `N` minus this number is
# the number of survivors. We may want to also keep track of *which* tank
# is alive, if any.
# 

# ```python
# # find out who has been destroyed
# dead_count=0
# last_alive=-1  # keep track of a live one
# for player in range(N):
#     if isdestroyed(player,tank_pos,shot_pos,isdead):
#         print 'Player ',player,' has been destroyed.'
#         isdead[player]=True
# 
#     if isdead[player]:
#         dead_count=dead_count+1
#     else:
#         last_alive=player
# 
# number_alive=N-dead_count
# 
# if number_alive<2:
#     no_one_has_won=False  # break out of loop
# ```

# Finally, we have all of the pieces together, and the complete program is

# In[13]:


import math
import random

def get_number_of_players():
    N=int(input('How many players? '))
  
    if N<=1:
        raise ValueError('Illegal number of players')

    return N

def get_tank_positions(N):

    pos=[0]*N   # make a list of length N, with zeros
    
    # fill in all the values with random numbers
    for i in range(N):
        pos[i]=random.random()*1000.0

    return pos

def isdestroyed(current_player,tank_pos,shot_pos,isdead):
  
    if isdead[current_player]:
        return False # a dead one cannot be destroyed
  
    N=len(tank_pos)
    
    for player in range(N):  # players numbered from 0 to N-1
        if not isdead[player]:  # did the player's shot hit the current player?
            if abs(shot_pos[player]-tank_pos[current_player])<10: # a hit
                return True

            
    # if you've gotten this far past the loop, then you're not destroyed
    
    return False

def print_shot_positions(pos,isdead):
    
    N=len(pos)
    
    for player in range(N):
        if not isdead[player]:
            print('Shot for player ',player,' landed at position ',pos[player],'.')
    
def print_tank_positions(pos,isdead):
    N=len(pos)
    
    for player in range(N):
        if isdead[player]:
            print('Player ',player,' is dead.')
        else:
            print('Player ',player,' is at position ',pos[player],'.')
            
def get_angle_and_speed(player_number):

    print('Player ',player_number)
    angle=float(input('  Enter your Angle of Elevation: '))
    
    if (angle<0) or (angle>90): # illegal angles
        raise ValueError("Illegal Angle Given")

    speed=float(input('  Enter your Angle of Speed: '))
    
    if speed<0:
        raise ValueError("Illegal Speed Given")
        
    
    return angle,speed


def radians(d):
    r=d*3.1415926535897932/180
    return r

def get_shot_distance(angle,shot_speed,wind_speed):

    angle=radians(angle)
    distance=(shot_speed**2*math.sin(2.0*angle)+
              2.0*wind_speed*shot_speed*math.sin(angle))/10.0;


    return distance


# In[14]:


N=get_number_of_players()
  
tank_pos=get_tank_positions(N)
  
# no one starts out dead (0 is the same as false)
isdead=[False]*N
  
# shot positions start off as zero
shot_pos=[0]*N
  
no_one_has_won=True
while no_one_has_won:
    
    wind_speed=(random.random()*20)-10;  #random speed from -10 to 10
    print('The wind speed is ',wind_speed)
    print_tank_positions(tank_pos,isdead)
    
    for player in range(N):
        
        # get all of the angles and speeds
      
        if not isdead[player]:
            [angle,speed]=get_angle_and_speed(player)
        
            distance=get_shot_distance(angle,speed,wind_speed)
        
            # make a vector with all of the places the shots landed
            shot_pos[player]=tank_pos[player]+distance
    
    print_shot_positions(shot_pos,isdead)
    
    # find out who has been destroyed
    dead_count=0
    last_alive=-1
    for player in range(N):
        if isdestroyed(player,tank_pos,shot_pos,isdead):
            print('Player ',player,' has been destroyed.')
            isdead[player]=True
      
        if isdead[player]:
            dead_count=dead_count+1
        else:
            last_alive=player
            
    number_alive=N-dead_count
    
    if number_alive<2:
        no_one_has_won=False  # break out of loop

        
        
if number_alive==0:
    print('Everyone is dead. Stalemate.')
else:
    print('Player ',last_alive,' has won!')
  


# In[ ]:




