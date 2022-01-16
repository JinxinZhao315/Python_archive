import math
import pylab
y_values = []
x_values = []
number = 0.0

while number < math.pi * 4:
    y_values.append(math.sin(number))
    x_values.append(number)
    number += 0.1

# This iteration can be done better by using array

pylab.plot(x_values,y_values,'ro')

''' The 'ro' here is a format string.
The first is a lowercase letter for the color. “r” is
red, “b” is blue, “g” is green.“k” is black.
The second element is a single character indicating the type of marker
“o” is for circles, “.” is for dots, “x” is for an x marker, “+” is for a plus marker.
'''

pylab.show()
# Remember to show! Or the graph does not appear
