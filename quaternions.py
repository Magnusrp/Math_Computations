# -*- coding: utf-8 -*-

# some simple operations with quaternions

def check_dim(x):
    if not len(x) == 4:
        print(str(x) + ' is not a valid quaternion')
    return len(x) == 4
        
def add(a,b):
    if len(a)==len(b):    
        return tuple((a[i]+b[i] for i in range(len(a))))

def scalar_prod(a,c):
        return tuple((i*c for i in a))

def inverse(a):
    if check_dim(a):
        mag_squared = 0   # initializes these variables
        c = []
        for i in range(4): # simultanteously builds the divisor and the quaternion
            mag_squared += a[i]**2
            if i == 0:
                c.append(a[i])
            else: c.append(-a[i])
        return tuple((i/mag_squared for i in c))
    
def dot_prod(a,b):           # product of the vector part
    total = 0
    for i in range(1,4):
        total += a[i]*b[i]
    return total
    
def cross_prod(a,b):         # product of the vector part
    return tuple((a[2]*b[3]-a[3]*b[2],
                  a[3]*b[1]-a[1]*b[3],
                  a[1]*b[2]-a[2]*b[1]))

def hamilton_prod(a,b):
    if check_dim(a) and check_dim(b):
        dot = dot_prod(a,b)
        cross = cross_prod(a,b)
        scalar_prod1 = scalar_prod(b[1:4],a[0])   # only want the scalar mult of the vector parts
        scalar_prod2 = scalar_prod(a[1:4],b[0])
        vector_part = add(add(scalar_prod1,scalar_prod2),cross)
        c = [i for i in vector_part]
        c.insert(0, a[0]*b[0] - dot)
        return tuple((c))
    
# example of inputs

import numpy as np
x1 = tuple((np.random.random(4)))
x2 = tuple((np.random.random(4)))
print(hamilton_prod(x1,x2))