# input: number of bottles first then loop through the bottles and add colour of each layer or empty
# does some stuff
# output: steps to take to sort in most efficient way similar to chess moves?

num_of_bottles = 5

# start with

# blue   yellow   blue   empty   empty
# blue   yellow    red   empty   empty
# yellow  red     red    empty   empty
# yellow  blue    red    empty   empty

# the bottles are an array of stacks

class Bottle:
    def __init__(self, size):
        #idk if i need this yet
        self.top = -1
        self.size = size
        self.items = [None] * self.size
    
    def push(self, colour):
        self.top+=1
        self.items[self.top] = colour
    
    def pop(self, colour):
        pass
    
    def isEmpty(self):
        pass
    
    def inStack(self):
        pass
    
    def pour(self):
        pass
    #might also want an is sorted function 
    

    
    