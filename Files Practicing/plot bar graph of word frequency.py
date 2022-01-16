import string
import numpy
import pylab

# Keeping asking for a existing file
filename = input('Type the name of the file you want to open:')
while True:
    try:
        the_file = open(filename,'r')
        break
    except IOError:
        print("The file you required is not found.")
        filename = input('Type the name of the file you want to open:')
       

# Process line and create a dictionary with word as key and frequency as value      
count_dict = {}
for line in the_file:
    line_list=line.strip().split()
    for word in line_list:
        word = word.lower().strip().strip(string.punctuation)
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1

# Convert dict into a list of tuples to sort 
word_list = []
for key,val in count_dict.items():
    if val > 2 and len(key) >3:
        word_list.append((key,val))       
word_list.sort()


key_list = [key for key,val in word_list]
value_list = [val for key,val in word_list]
'''
You don't use key_list = count_dict.keys() & value_list = count_dict.values()
here because that way the keys and values have no order,therefore are not aligned.
When you plot, for every key you take you must take the corresponding value,
therefore you must put (key,val) into a list then extract them respectively (using comprehension here)
this way the key_list and value_list will have their elements aligned. 
'''

# Plotting
bar_width = 0.5
x_values = numpy.arange(len(key_list))
''' Basically means how many x values are there '''
pylab.xticks(x_values, key_list, rotation = 45)
'''First argument means the position of x value ticks:
every number in the x_value array;
second arument means the labels of each x value tick,
rotation = 45 just displys lables rotated 45 degrees'''
pylab.bar(x_values,value_list,width=bar_width,color='r')
'''First argument is tick locations. The labels set previously by .xticks()
Note the x values must be numbers -- regardless whether you label each number as some words,
the x(and y) values themselves must be numbers!!'''
pylab.show()

