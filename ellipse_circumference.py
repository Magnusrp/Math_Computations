# -*- coding: utf-8 -*-

import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

semi_axes = (8,2)   # as measured from (0,0) to the boundary
n = 100

semimajor_axis = max(semi_axes)
semiminor_axis = min(semi_axes)

# this section is just for plotting and doesn't contribute to the calculation

def ellipse(x,a,b):
    return b * np.sqrt(1-x**2/a**2)

x_range = np.arange(-semimajor_axis, semimajor_axis, 0.01*semiminor_axis)
y_range = ellipse(x_range,semimajor_axis,semiminor_axis)
x_range = np.append(x_range,semimajor_axis) # to avoid invalid value encountered in sqrt
y_range = np.append(y_range,0)

limiter = max(semimajor_axis, semiminor_axis)
plt.plot(x_range,y_range,x_range,-y_range, c='b')
plt.xlim((-1.5*limiter,1.5*limiter))
plt.ylim((-1.5*limiter,1.5*limiter))

# this is an expansion of an elliptic integral of the second kind

def expansion(h,n):
    nth_order = 0
    for i in np.arange(1,n+1):
        i = int(i)            # python ints are of unlimited size; prevents overflow for large n
        nth_term = (h**i)*(math.factorial(2*i-2) / (math.factorial(i)*math.factorial(i-1)*2**(2*i-1)))**2
        nth_order += nth_term
    return nth_order

def circumference(a,b,n):
    h = (a-b)**2 / (a+b)**2
    return np.pi*(a+b)*(1+expansion(h,n))

print('The circumference is: ' + str(circumference(semimajor_axis,semiminor_axis,n)),
      'The area is: ' + str(math.pi*semimajor_axis*semiminor_axis),
      'The eccentricity is: ' + str(math.sqrt(1 - ((semiminor_axis**2)/(semimajor_axis**2)))),
      sep='\n')
