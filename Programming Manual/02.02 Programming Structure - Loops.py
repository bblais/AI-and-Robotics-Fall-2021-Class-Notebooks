#!/usr/bin/env python
# coding: utf-8

# In[1]:


# make all of the diagrams appear in the notebook, not in an external window
get_ipython().run_line_magic('pylab', 'inline')
from mplturtle import *


# ## Loops 
# 
# A loop is used to repeat a set of statements many times, usually until
# some condition is met. One loop structure we will introduce now is the
# while-loop. It has the form
# 
# ```python
#     while CONDITION:
#         STATEMENTS
# ```
# 
# This structure works like a repeating if-statement: if `CONDITION` is
# true, then the `STATEMENTS` are executed. In a while-loop, however, the
# program flow returns back to the `while (CONDITION)` line and the
# ` CONDITION` is tested again. If it is still true, then the `STATEMENTS`
# will be executed *again*. This will repeat until such time as
# ` CONDITION` is tested and comes up false. Then program flow jumps to
# the line following the entire `while` clause. The following is an
# example that prints out the numbers 1, 2, 3, 4 and 5.
# 
# 

# In[7]:


x=1
while x<=5:
    print(x)
    x=x+1

print('Done!')


# The program flow in this example is as follows. The first line to be
# executed is `x=1` which sets the value of `x` to 1. Then the program
# tests to see if `x` is less than or equal to five, which is true, so the
# lines within the while-loop are executed. The first line displays `x`,
# which prints a "1" on the screen, and the next line adds one to `x`,
# yielding the answer 2, and assigns this new value to `x`. The program
# then jumps back to the `while` statement and tests `x` again to see if
# it is less than or equal to five, which is again true. Again, the value
# of `x` is printed to the screen, this time it is "2", and again `x` is
# incremented by 1, yielding 3. The `while` tests `x` again at 3, 4, and
# 5, passing each time and displaying the result. When `x` passes with a
# value of 5, the two lines are executed, displaying "5" and incrementing
# `x` to 6. The `while` tests `x` to see if it is less than or equal to 5,
# which is *false* now, and skips to the indented lines in the `while`
# block. The next line to be executed displays "Done!" and the program
# ends. Notice that the last value of `x` is 6, but the last value to be
# displayed is 5.
# 
# We can extend the `interest` program written in
# the Section on Variables to use a while-loop, and calculate the
# accumulated interest over the course of many years.
# 
# 

# In[9]:


# get the initial values
principal=input('What is the initial principal? ')
principal=float(principal)

rate=input('What is the annual interest rate? ')
rate=float(rate)

number_of_years=input('How many years do you want to calculate interest? ')
number_of_years=int(number_of_years)

print('The original principal is $',principal)
print('The interest rate is ',rate)

current_year=1
while current_year<=number_of_years:
  
    interest=principal*rate; # calculate the interest
    principal=principal+interest;
    
    print('After year ',current_year,': ')
    print('  The interest is $',interest)
    print('  And the new principal is $',principal)
    
    current_year=current_year+1;


# In[ ]:





# One technique for using a while loop is to repeat a question if the user
# gave a bad answer. For example, the following code fragment keeps the
# user from entering a negative principal value, but allows the user to
# retype a valid answer.
# 

# In[12]:


principal=-1

while principal<0:
    principal=input('What is the initial principal? ')
    principal=float(principal)

    if principal<0:
        print('The principal value cannot be negative.  Please reenter it.')


# It is necessary for the initial value of `principal` to be less than
# zero, so that the statements within the while-loop will execute the
# first time. If we forgot the `principal=-1` line, we'd receive an error
# like:
# 
# ```python
#     NameError: name 'principal' is not defined
# ```
# 
# If we had set `principal` to a positive value, then the while-loop would
# have tested *false*, and skipped all of the statements in the
# while-loop. The `principal=-1` line gets us into the while loop. After
# that, the user input will keep us there until the user enters a valid,
# positive (or zero) principal.
# 

# ### The `for`-loop
# 
# Ninety percent of loops one writes, repeat a specified number of times,
# like the first example above, which repeats 5 times. Because of this,
# there is a more convenient form of a loop for this purpose, called a
# `for`-loop. The following two pieces of code do the same thing:
# 
# 

# In[14]:


# while-loop
x=0
while x<10:
    print(x)
    x=x+1

print('Done!')

# do the same thing with a for-loop

for x in range(10):
    print(x)
    
print('Done!')


# 
# The `for`-loop moves through each value of `range(10)`, which goes from
# 0 to 9 (not 1 to 10), which repeats the statements in the `for`-loop 10
# times. Both the setting of the initial value, and the incrementing, is
# done automatically.
# 
# The following example is the same as the
# Square program earlier, but uses a `for`-loop to reduce some
# of the redundancy.
# 
# 
# 

# In[19]:


# remember to import the turtle functions and the pylab inline from before if you're running just this cell
reset()

size=70
for side in range(4):
    forward(size)
    right(90)


# 
# Another example with a square, with some extra variables. What do these
# variables do?
# 

# In[25]:


reset()

number_of_sides=4
angle=360/number_of_sides
size=70

for side in range(number_of_sides):
    forward(size)
    right(angle)

