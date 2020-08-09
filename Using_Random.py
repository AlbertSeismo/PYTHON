#In this program we will use range to generate numbers for x between 0-1000000
# and for y between 100-10000 using range an inbuilt function in python (use: help("range"), to find out more)
# then we will pick random numbers using the random module to generate 5000 numbers
#This will also form our big part in visualization of data in python
#As always begin by importing the necessary packages/modules or functions in your working space
import random
import matplotlib.pyplot as plt
import numpy as np
#matplotlib.pyplot module for plotting

x = random.sample(range(1000000),100)
y = random.sample(range(100,10000),len(x))        #Iam using len(x) in order y have the same length as x
#lets scatter or plot the randomly generated points on the graph or chart
plt.figure()
plt.scatter(x,y,edgecolors="red")
plt.grid()
plt.xlabel("X-Axis")    #label the x axis
plt.ylabel("Y-Axis")    #label the y axis
plt.title("A SCATTER plot showing Y against X")    #put the title to the graph to make sense
#plt.show()                                 #we need to show always in order the graph/chart to show up

##############################################
#This is another example of random generator from numpy, so i begin by applying np
#it generates 50 numbers, and to show them on graph i am using plot, but i could use scatter as well
plt.figure()
R =np.random.randn(50)
S = np.random.randn(len(R))  #still here i am using len(R) because i want R,S to have the same size/length
#otherwise if they are of different length if we plot it will retun an error, there is a way to manouvre it though

plt.plot(R,S,"g-v",LineWidth =2)
#plt.scatter(R,S,edgecolors="green")  #you can try this choice by removing the harsh tag and comment or #the other one
plt.grid()
plt.xlabel("R, X-Axis")    #label the x axis
plt.ylabel("S, Y-Axis")    #label the y axis
plt.title("A plot showing S against R")    #put the title to the graph to make sense
plt.show()


#TASK 3
"""Task: I want you to create 200 random points of say x,y and plot them, using the procedure above using the 2 methods"""
#The goal in this script/program is get you started and be familiar with data Visualization, plotting
#How results can be displayed
#How you can generate random numbers using either the builtin function or the numpy's random.randn


