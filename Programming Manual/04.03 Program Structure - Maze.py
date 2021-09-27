#!/usr/bin/env python
# coding: utf-8

# ## Extended Example: Maze
# 
# In this section we write a program to generate a random maze. We will
# use Aldous-Broder's algorithm, which goes as follows:
# 
# > Start with a maze grid with all walls up (a bunch of individual,
# > walled cells). Pick a point, and move to a neighboring cell at random.
# > If the new cell has all of its walls still up, then knock the walls
# > down between the previous cell and the new cell. Keep moving to
# > neighboring cells until all cells have been visited.
# 
# We will start with the recipe, and then break each piece down into
# pieces.
# 
# then we expand those pieces
# 
# then we structure the while-loop
# 
# At this point we have to make some decisions about how to represent the
# maze itself. Pretty much we need to have a number of rows and columns
# for the maze, and know which walls are up for the particular cell. For
# example, say we have the following 3x3 maze, and a summary of the
# information to describe this maze:
# 
#                        +--+--+--+
#                        |        |
#                        +--+  +--+
#                        |        |
#                        +--+  +  +
#                        |     |  |
#                        +--+--+--+
# 
# The information in this maze is the following:
# 

# In[ ]:




