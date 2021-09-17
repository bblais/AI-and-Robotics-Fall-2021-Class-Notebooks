#!/usr/bin/env python
# coding: utf-8

# In[1]:


# make all of the diagrams appear in the notebook, not in an external window
get_ipython().run_line_magic('pylab', 'inline')
from mplturtle import *


# ## Branching: If-statements
# 
# Programs execute one line at a time, in consecutive order. This
# sequential program flow can be modified using two types of programing
# structures: branches and loops. We consider branches in this section,
# and loops in the next section.
# 
# The form of a simple branch is the following:
# 
#     if CONDITION:
#         STATEMENTS
# 
# where I am using `ALL CAPITAL LETTERS` to denote something which stands
# for code that you would need to write, but is not code itself. The colon
# (:) is necessary at the end of the `if` line, or a syntax error will
# result. A branch, or if-statement, is interpreted in the following way:
# only execute the `STATEMENTS` if the `CONDITION` is true. For example,
# here is a program which swaps the two values of `x` and `y` only if `x`
# is originally larger than `y`. The result is that the final value of `x`
# will always be smaller, or equal to, the final value of `y`.

# In[3]:


# An example which swaps two variable values, 
# only if the first is larger

# get the initial values
x=input('What is the initial value of x? ')
y=input('What is the initial value of y? ')

# display the initial values
print('x has the value ',x)
print('y has the value ',y)
print('--------------------------')

if x>y:
    print('***Swapping***')
    x,y = y,x

# display the final values
print('x has the value ',x)
print('y has the value ',y)


# Say we input the values of 5 for `x` and 10 for `y`.
# 
#     What is the initial value of x? 5
#     What is the initial value of y? 10
#     x has the value  5 
#     y has the value  10 
#     --------------------------
#     x has the value  5 
#     y has the value  10 
# 
# As the program progresses, it gets to the line `if x>y:` which is
# calculated to be `if 5>10:` or `if False:` since `5` is not greater than
# `10`. Because the condition is false, the statements after the `if`
# which are indented by 4 spaces will not be executed, and the program
# continues with the next line of code after the indented lines. If,
# however, we input the values of 15 for `x` and 10 for `y`.
# 
#     What is the initial value of x? 15
#     What is the initial value of y? 10
#     x has the value  15 
#     y has the value  10 
#     --------------------------
#     ***Swapping***
#     x has the value  10 
#     y has the value  15 
# 
# The values get swapped!
# 

# ### Comment on Boolean variables
# 
# A boolean variable is one that has a value of true or false, instead of
# a number. In Python those values are `True` and `False` (note the
# capital first letter). Thus, each of the following if-statements will
# print a message to the screen
# 
# ```python
#     if True:
#         print 'this line gets executed'
#         
#     if 3>2:
#         print 'this line gets executed'
# 
#     printit= (3>2)  # set the variable printit to True
# 
#     if printit:
#         print 'this line gets executed'
# ```
# 
# whereas the following if-statements will print nothing
# 
# ```python
#     if False:
#         print 'this line does not get executed'
#         
#     if 50<10:
#         print 'this line does not get executed'
# 
#     printit= (34>57)  # set the variable printit to False
# 
#     if printit:
#         print 'this line does not get executed'
# ```
# 
# The `CONDITION` in an if-statement *must* reduce to a true or false
# value for it to have any meaning.
# 

# ### Boolean Operators
# 
# The following are the allowed boolean operators.
# 
# | operator | meaning |
# | --- | ---
# | ==  | equal to                 |
# | >   | greater-than             |
# | <   | less-than                |
# | >=  | greater-than or equal to |
# | <=  | less-than or equal to    |
# | not | not (negation)           |
# | !=  | not equal to             |
# | and | and                      |
# | or  | or                       |
# 
# A **very** common mistake for beginning programmers is to use the
# assignment `=` instead of the equality `==` in a `CONDITION` of an
# if-statement. Whenever you are testing if two values are equal in
# if-statement (or a while-loop, which we discuss later), you **must** use
# `==`. For example, the following code fragment will print out a message
# 
# ```python
#     a=5
#     b=5
#     if a==b:
#         print 'a is equal to b'
# ```
# 
# but the following code fragment will not
# 
# ```python
#     a=5
#     b=6 # <--- b is not equal to a
#     if a==b:
#         print 'a is equal to b'
# ```
# 
# If one wanted to test to see if `x` is bigger than both `y` and ` z`,
# one would write
# 
# ```python
#     if x>y and x<z:
#         print x is bigger than both y and z
# ```
# 
# Translating back to English we have "`x` is greater than `y` and ` x` is
# also greater than `z`". What would have happened if we had written
# instead, `x > y and z`? If you test it yourself you will find that it
# prints the message whenever `z` is not equal to zero, and `x` is greater
# than `y`! Why is that? As stated in the beginning, computers are very
# literal, and follow a strict syntax. Python is interpreting
# `x > y and z` as ` (x>y) and (z)` where `z` is seen as a *boolean*
# (true/false) variable even though we didn't mean it to. In this sense,
# anything non-zero is true, so Python is interpreting `x > y and z` as
# true whenever `z` is not equal to zero, and `x` is greater than `y`.
# 
# Although it is not *always* necessary, it is a very good habit to put
# parentheses around any operation of two variables, like `(x>y)` or
# `( (x>y) and (x>z) )`. It may be a bit more typing, but it can save you
# hours in debugging logic that is hard to see otherwise.
# 

# ### if, elif, and else
# 
# The if-statement has a more general structure which is very useful. It
# looks like
# 
# ```python
#     if CONDITION1:
#         STATEMENTS  # these statements run if CONDITION1 is true
#     elif CONDITION2:
#         STATEMENTS  # these statements run if CONDITION1 is false, and 
#                     #                         CONDITION2 is true
#     elif CONDITION3:
#         STATEMENTS  # these statements run if CONDITION1 is false, and 
#                     #                         CONDITION2 is false, and
#                     #                         CONDITION3 is true
#     else:
#         STATEMENTS  % these statements run if all of the CONDITIONS are false
# ```
# 
# You can have as many or as few (even zero) `elif` clauses, and either
# include or not the final `else` clause. This structure lets you set up
# different actions for many different incoming possibilities. The colon
# (:) needs to be at the end of each line which starts a block of code,
# like ` if`, `elif`, and `else`.
# 
# For example, the following program asks the user if she likes bananas,
# and responds differently given the user's response. Although we haven't
# used strings so far, the example is fairly self-explanatory.
# 

# In[5]:



response=input('Do you like Bananas? ');

if response=='yes':
    print ('I like Bananas too!')
elif response=='no':
    print ('I dislike Bananas too!')
else:
    print ('I did not understand what you wrote.')


# > **Exercise** Make a turtle program to ask the user what shape to draw, and draw it. You should have at least 3 different shape choices.
