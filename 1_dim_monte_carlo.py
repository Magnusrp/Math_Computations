# -*- coding: utf-8 -*-

# I intend to use this as a framework for a more generalized n-dim monte carlo sim
# It should be relatively straightforward for 'square' domains

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# hyperparameters
num_points = 10**5
num_runs = 3
step = 0.01
boundary = [-4,4]

def test_function(x1):
    return x1**3

# plots the points that will be compared with the function to determine the integral
def random_points(x,y,bound,num):
    points_x = np.random.uniform(bound[0],bound[1],num)
    points_y = np.empty(num)          # initializes the y array of the random points
    test_value = test_function(points_x)
    for i in range(num):
        if test_value[i] > 0:
            points_y[i] = np.random.uniform(0,max(y))
        elif test_value[i] < 0:
            points_y[i] = np.random.uniform(min(y),0)
        else: points_y[i] = 0
    return test_value,points_x,points_y

# for determining the total area, we need to determine the regions by their sign and location
def def_regions(x,y):
    signs = np.sign(y)
    regions_coord = [[signs[0]],[x[0]]]      # [[+ or -],[x-val of change]]
    for i in range(1,len(x)):        # ignore inital x-value
        if signs[i] != signs[i-1] and signs[i-1] != 0:
            regions_coord[0].append(signs[i])
            regions_coord[1].append(x[i])
        if signs[i] != signs[i-1] and signs[i-1] == 0:
            regions_coord[0][i-1] = signs[i]
    return regions_coord

def total_area(sign,coord,xmax,y):
    diff = []
    for i in range(1,len(coord)):    # to get list of size n-1
        if sign[i-1]==1: diff.append((coord[i]-coord[i-1])*abs(max(y)))
        else: diff.append((coord[i]-coord[i-1])*abs(min(y)))
    if sign[i]==1: diff.append((xmax - coord[-1])*abs(max(y)))
    else: diff.append((xmax - coord[-1])*abs(min(y)))
    return sum(diff)

x_values = np.arange(boundary[0],boundary[1]+step,step)
y_values = test_function(x_values)
regions = def_regions(x_values,y_values)

definite_integral = 0
for j in range(num_runs):
    test_value,points_x,points_y = random_points(x_values,y_values,boundary,num_points)
    counter = [0,0]     # [pos,neg] contributions to the area
    for i in range(num_points):
        if test_value[i] > 0 and points_y[i] < test_value[i]:
            counter[0] += 1
        elif test_value[i] < 0 and points_y[i] > test_value[i]:
            counter[1] -= 1
    definite_integral += (sum(counter)/num_points) \
                            * total_area(regions[0],regions[1],x_values[-1],y_values)
definite_integral /= num_runs

# the plot serves no purpose here; I used it as a visual aid during debugging
plt.plot(x_values,y_values,points_x[0:500],points_y[0:500],'r.')

print(definite_integral)