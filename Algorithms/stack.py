class Stack:
    def __init__(self):
        self.stack = []
        self.stack_size = len(self.stack)

    def top(self):
        '''Return the top element'''
        if self.stack_size == 0:
            return None
        else:
            return self.stack[self.stack_size-1]
      

    def pop(self):
        '''Remove the top element'''
        if self.stack_size == 0:
            return None
        else:
            self.stack.remove(self.stack_size-1)
            return self.stack
        

    def insert(self,x):
        '''insert x into the stack'''
        self.stack.insert(0,x)
        return self.stack
        
        
        
