import math

class Point(object):
    def __init__(self, x_param = 0.0, y_param = 0.0):
        self.x = x_param
        self.y = y_param
        # Use default value in function definition is better than define self.x = 0,
        # beacuse this way you can change the default values by providing them,
        # so that you can create different instances .

        # Note that the initialiser must be called __init__ for it to be called after
        # a default instance is created thus effect instance creation. 

    def distance(self,param_pt):     # Note that the second argument is a point. So you should define that point before calling method. 
        x_diff = self.x - param_pt.x
        y_diff = self.y - param_pt.y
        return math.sqrt(x_diff**2 + y_diff**2)

    def vector_sum(self,param_pt):
        new_pt = Point()            # Because for vector sum you should return a point, you must initialise the point first
        new_pt.x = self.x + param_pt.x
        new_pt.y = self.y + param_pt.y
        return new_pt

    # If you do print(p1.vector_sum(p2)), shell returns <__main__.Point object at .......>
    # Therefore you need to provide a __str__ method in Point that gets called when printing an instance.

    def __str__(self):
        print('Call the __str__ method:')
        return '({:.2f}, {:.2f})'.format(self.x , self.y)
    # Note 'the method that gets called when printing an instance'
    # must be named ' __str__ '. As long as this name exists, whenever
    # an instance is printed it is automatically called. 
