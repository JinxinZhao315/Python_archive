import numpy
import pylab

x_value = pylab.arange(0,4*numpy.pi,0.1)
y_value_sin = numpy.sin(x_value)    # Note here you must use numpy.sin/cos instead of math.sin/cos. It seems math module cannot handle array 
y_value_cos = numpy.cos(x_value)

# Good thing about array is you can directly multiply an array by a number,
# and all numbers in the array is multiplied
# Or you need to iterate through the list of x-values and produce y one by one

pylab.title('sin and cos Graph')  # Yes you can do this. Give the graph a title.
pylab.plot(x_value,y_value_sin,'b')
pylab.plot(x_value,y_value_cos,'r')

pylab.show()

