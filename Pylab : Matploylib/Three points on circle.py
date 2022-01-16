# To prove three points(two moving points 1 and 2, one fixed (4,4)) are always on the same circle


import math
import pylab
x_values1 = []
y_values1 = []
theta = 0.0
x_values2 = []
y_values2 = []


while theta < math.pi*2:
    x_value1 = 5+(2**0.5)*math.cos(theta)
    x_values1.append(x_value1)
    y_value1 = 5+(2**0.5)*math.sin(theta)
    y_values1.append(y_value1)
    x_value2 = 5-(2**0.5)*math.sin(theta)
    x_values2.append(x_value2)
    y_value2 = 5+(2**0.5)*math.cos(theta)
    y_values2.append(y_value2)
    theta += 0.05


pylab.plot(x_values1,y_values1,'ro')
pylab.plot(x_values2,y_values2,'bo')
pylab.plot(4,4,'ko')

pylab.show()
    
