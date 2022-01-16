import numpy
import pylab

theta = pylab.arange(0,2*numpy.pi,0.05)
x_values1 = 5+(2**0.5)*numpy.cos(theta)
y_values1 = 5+(2**0.5)*numpy.sin(theta)
x_values2 = 5-(2**0.5)*numpy.sin(theta)
y_values2 = 5+(2**0.5)*numpy.cos(theta)


pylab.plot(x_values1,y_values1,'ro')
pylab.plot(x_values2,y_values2,'bo')
pylab.plot(4,4,'ko')

pylab.show()
