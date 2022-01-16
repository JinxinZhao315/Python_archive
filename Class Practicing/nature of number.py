class NewClass(object):
    def __init__(self,param_int=1):
        self.the_int = param_int
        if param_int%2==0:
            self.parity='even'
        else:
            self.parity='odd'
    # Remember there is no 'return' for initialisers. Python automatically adds 'return self' for you, so you should not type. 
    def process(self,instance):
        sum_int = self.the_int + instance.the_int
        if sum_int < 0:
            return 'negative'
        elif sum_int % 2==0:
            return 'even'
        else:
            return 'odd'
    def __str__(self):
        return 'Value {} is {}'.format(self.the_int,self.parity)


inst1=NewClass(4)
inst2=NewClass(-5)
inst3=NewClass()
print(inst1)          # Directly 'print' the instance results in what is returned by the __str__ constructor 
print(inst1.parity)   # Print an attribute of the instance
print(inst1.process(inst2))   # Print what is returned by the process method 
