#!/usr/bin/env python
# coding: utf-8

# # Program Structure - Part I
# 
# ## The Turtle
# 

# A very nice way to introduce program is using the `turtle` module. 
# I make a custom version of this module, but it requires a few extra steps.

# In[16]:


# make all of the diagrams appear in the notebook, not in an external window
get_ipython().run_line_magic('pylab', 'inline')
from mplturtle import *


# 
# This
# module is a graphics module that lets you instruct a so-called "turtle",
# giving it instructions to go forward, turn right, go backward, etc\...
# while using a pen to draw its path. It's easiest explained with an
# example.  
# 
# 

# In[9]:


reset()  # this line is needed in every cell

forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

animate()  # you can omit this line if you don't want to see the animation


# The directions tell the turtle to go forward for 50 pixels, turn right
# 90 degrees, go forward 50 pixels, etc\... All the while the pen is
# down, so that the turtle draws. We can extend this example, by lifting
# the pen, moving over a little (without drawing), dropping the pen down,
# and drawing another square.

# In[10]:


reset()  # this line is needed in every cell

forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)

penup()
backward(20)
right(90)
forward(20)
pendown()

forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)

animate()  # you can omit this line if you don't want to see the animation


# > **Excercise**:  Make the turtle draw triangles, instead of squares, in the figure above.

# ### Want to know more about turtle?

# Some of the more useful
# commands are:
# 
# 
# - `forward(distance)` - Move the turtle forward by the specified
# `distance`, in the direction the turtle is headed. 
# - `backward(distance)` Move the turtle backward by distance, opposite to the direction the
# turtle is headed. Do not change the turtle's heading. 
# - `right(angle)` -
# Turn turtle right by angle units. (Units are by default degrees)
# 
# - `left(angle)` - Turn turtle left by angle units. (Units are by default
# degrees) 
# - `setheading(to_angle)` - Set the orientation of the turtle to
# `to_angle`. 
# - `goto(x, y)` - Move turtle to an absolute position. If the
# pen is down, draw line. Do not change the turtle's orientation.
# 
# - `position()` - Return the current x,y coordinates of the turtle
# 
# - `reset()` - Reset the
# screen and the turtle position. Used at the beginning of a script to
# make sure that running it again won't overlap the drawings.
# 
# - `circle(radius)` - Draw a circle of given `radius`, in a
# counter-clockwise direction from the current turtle heading. *The turtle
# is **not** the center of the circle.* To get a circle with the center at
# the turtle, you'll need to move the turtle over by radius units, draw
# the circle, and then move back.
# 
# 
# - `pencolor(color)` - Set the pen color 
# - `pencolor(colorstring)` - Set
# pencolor to colorstring such as \"red\", \"yellow\", or \"\#33cc8c\".
# 
# - `pencolor(r, g, b)` - Set pencolor to the RGB color represented by r,
# g, and b. Each of r, g, and b must be in the range 0..1.
# 

# In[11]:


reset()

# draw a series of circles

pencolor("green")
circle(100)

pencolor("red")
circle(50)

pencolor("blue")
circle(25)


# In[13]:


reset()

# draw a series of circles centered at 0,0
penup()
right(90)
forward(50)
left(90)
pendown()

circle(100)

penup()
left(90)
forward(25)
right(90)
pendown()

circle(50)

penup()
left(90)
forward(12.5)
right(90)
pendown()

circle(25)


# ## Variables 
# 
# All data in a program is stored in *variables*, which are just memory
# blocks with names. The names can be any sequence of letters, underscores
# (\_), or numbers as long as the name starts with a letter. `bob`,
# ` frank4`, and `a_5_b` are all legitimate variable names. Usually you
# choose names that make sense for your particular application, like
# ` mysum`, `total`, or `chicken3`. In Python, everything is
# *case-sensitive*. This means that `bob` is a *different variable* than
# `Bob`, `BoB`, or `boB` (which are all different from each other).
# 
# To assign a value (or values, as we shall see later) into a variable one
# uses the assignment operator, namely the "=" sign.
# 

# In[3]:


a=5


# In[4]:


a*600


# In the last line I used `a` (which was defined to be `5` in the previous
# line) in an expression. Variables can be used just as numbers in any
# expression in Python.
# 

# In[5]:


a=30
b=40
import math   # import the math functions
c=math.sqrt(a**2+b**2)
print(c)


# where `math.sqrt` is a function that takes the square root of the
# numbers.
# 
# One can even use a variable in an expression which sets its own value.
# 

# In[6]:


a=6
b=7


# In[7]:


a=a+b
print(a)


# 
# This demonstrates the meaning of the symbol `=` in Python. It does *not*
# mean the same thing that it means in standard algebra. It does not mean
# equivalence, it means *assign*. `a=5` means take the right side (` 5`)
# and assign it to the variable on the left side (`a`). With `a=6` and
# `b=7`, then the statement `a=a+b` means take the right side (` a+b`
# which evaluates to 13) and assign it to the variable on the left side
# (`a`). Now `a` has the new value of 13.
# 
# Some of the uses of variables is for convenience, readability,
# consistency, and calculation. Let's consider our square program from
# Listing [\[list:square\]](#list:square){reference-type="ref"
# reference="list:square"} on page . There are two obvious issues with it.
# One is that we've repeated ourselves several times. There is an easier
# way to make use of that, which we'll discuss later. The other issue is
# that the same number, the side of the square, is used four times. If we
# wanted to draw a square of a different size we'd have to change all four
# numbers. Because we have to make four changes, instead of one, it leads
# to more possible errors (i.e. typos). A variable can change that.
# 
# ### Comments 
# 
# In the code, notice the use of *comments* following the `#` character.
# Python ignores anything following this characters, which allows us to
# document the code making it easier for others to read. Get in the habit
# of putting in comments now, because the biggest use of comments is to
# remind *yourself* about how a piece of code works, several weeks after
# it has been written.

# ### Drawing square with variables

# In[14]:


reset()

size=90

# draw the square
forward(size)
right(90)
forward(size)
right(90)
forward(size)
right(90)
forward(size)


# In[ ]:





# In[ ]:





# ## User Input
# 
# Any good program asks for input from the user. The `input` function gets input from
# the keyboard, asked at the command line. This lets the user type in
# values, which can be different each time the program is run. There will
# be many cases where these values may be inappropriate, and possibly
# cause the program to crash. Good program writing will include taking
# care of these cases as well. The following example lets the user enter
# the size of a square to draw. One thing to note is that the `input` function returns a *string* (like "hello") and needs to be converted to a number to be used an a calculation.

# In[16]:


reset()

size=input('What size do you want the square?')
size=int(size)


# draw the square
forward(size)
right(90)
forward(size)
right(90)
forward(size)
right(90)
forward(size)


# > **Exercise:**  Write a program to ask the user for the size, and the x and y coordinates of the center of a circle, and draw it.

# 
# 
# The following example lets the computer determine a number you have
# chosen, given the answers to a couple of simple questions.

# In[20]:


# simple guess the number game
# 

import time   # the time module includes the sleep function

print('Please think of a number between 10 and 99.')

sum_digits=input('What is the sum of the digits of your number? ')
sum_digits=int(sum_digits)  # convert the input to an integer

diff_digits=input('What is the difference of the digits of your number (first digit - second digit)? ')
diff_digits=int(diff_digits)  # convert the input to an integer

print('Let me think a moment...')

time.sleep(2) # delay for 2 seconds

# apply the equation to get the guess from the info
guess=10*(sum_digits+diff_digits)//2+(sum_digits-diff_digits)//2

print('Your number was ',guess,', right?')


# The following example computes the amount of interest earned after one year, given an initial principal and an annual interest rate.

# In[22]:


# get the initial values
principal=input('What is the initial principal? ')
principal=float(principal)  # convert to a real number

rate=input('What is the annual interest rate? ')
rate=float(rate)  # convert to a real number

print('The original principal is $',principal)
print('The interest rate is ',rate)

interest=principal*rate # calculate the interest
print('The total interest after 1 year is $',interest)

principal=principal+interest
print('The new principal after 1 year is $',principal)


# Note how the use of relevant variable names makes the code much easier to read.

# In[ ]:




