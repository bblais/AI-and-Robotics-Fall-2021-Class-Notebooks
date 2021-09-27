#!/usr/bin/env python
# coding: utf-8

# # Program Design
# 
# ## Guidelines
# 
# You now know enough Python syntax to do almost any program. There are
# other parts of Python syntax that we will cover later, but it is
# important to pause and consider how programs are designed. A programmer
# *never* starts by just sitting at a keyboard and typing. There are
# several key steps before any code is written, or the programmer will
# waste hours, even days, with false starts and debugging issues.
# 
# A programmer starts with a problem, and usually some idea of how to
# solve it. The task of the programmer is to translate this idea into a
# step-by-step set of instructions to solve the problem. The basic
# approach is the following 
# - Break up the problem into smaller pieces,
# which can be tested individually. This is usually done by writing the
# program like a recipe with parts of the problem in English. You may have
# things like "do the following 5 times" or "calculate this value from the
# other values given". These will be fleshed out later in the process. You
# should have a full recipe for the problem, written out on paper, well
# before you start to type. 
# - Attack each smaller piece as a separate
# program, breaking into smaller pieces as necessary. 
# - You should find
# that your more refined recipe consists of a set of functions, each of
# which is small and does a very specific thing. 
# - Desk-check the recipe to
# see that it really works. This means stepping through your recipe, on
# paper, as if you were a computer, not taking anything for granted, and
# seeing that it works. You should also desk-check what your functions do
# when given improper input. The desk-check is a very important step, and
# is often skipped by beginning programmers who are in a rush to get to
# the keyboard. It also is a step that, when skipped, wastes more time
# than missing almost any other step! 
# - Identify what information each
# function needs to get from the main program. These will be your input
# arguments for that function. Identify what information each function
# needs to return to the main program. These will be its output arguments.
# - You then write each function in proper code, and test it *individually*. This is the important thing: **do not trust that a function works without testing it**. Put in bad values, and make sure it behaves well. Test it over the entire range of possible input values, especially values like zero or the maximum valid value, to make sure the
# function is robust. 
# - When you start putting the functions together to
# match your recipe, do it one function at a time, and test it. If you
# type the whole recipe out at once, and it doesn't work, then you don't
# where it is failing, and it will take you a long time to figure out
# where it is failing. Testing after the addition of *any* amount of code
# saves you time in the long run.
# 
# Here are some guidelines that help with programming and debugging.
# 
# 
# - Other than your main function, all other functions should only return
# values and *not* print things to the screen unless that is their *only*
# job. Let the main function print out the values if it needs to, or not
# if it doesn't need to. A function is much less useful if it prints
# values to the screen itself. 
# - 90% of debugging is *preventative*. If you
# are careful, test every bit of code you add (no matter how small or
# insignificant) *at the time you add it*, and follow the guidelines below
# you will avoid many pitfalls. 
# - Name variables consistently. If you use
# use variables like ` interestrate`, `interest_rate`, `InterestRate`,
# etc. then make *all* variables like that. You don't want to use
# `InterestRate` in one place and `mortgage_rate` somewhere else. It gets
# confusing! 
# - If you get an error, determine what the error is before you
# try to change your code to fix it. Although often terse and difficult to
# read, the error messages do tell you what is wrong (although it takes
# some practice to interpret them). 
# - Test each function separately, and
# over a wide range of possible input values. You can only trust a program
# if each function is working perfectly. 
# - Do not try to write the entire
# program before testing. This becomes a nightmare fast! Break things into
# pieces, and test each piece, no matter how trivial it seems. 
# - When you
# really get stuck, have someone else look at your code. Seeing with
# different eyes often allows someone to see errors that you've been
# staring at (and missing) for an hour. 
# - When trying to determine why
# something is going wrong, put in a lot of ` print` statements to confirm
# that the variables have the values you think they do. Do this even in
# cases where it is obvious that the variable is correct, because
# sometimes the obvious is not true. 
# - And finally, remember the golden
# rule of debugging: If you are absolutely sure that everything in your
# program is right, and if it still doesn't work, then one of the things
# that you are absolutely sure of is wrong.
# 

# In[ ]:




