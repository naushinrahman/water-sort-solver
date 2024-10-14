# input: number of bottles first then loop through the bottles and add colour of each layer or empty
# does some stuff
# output: steps to take to sort in most efficient way similar to chess moves?

num_of_bottles = 5

# ex
# blue   yellow   blue   empty   empty
# blue   yellow    red   empty   empty
# yellow  red     red    empty   empty
# yellow  blue    red    empty   empty

# the bottles are an array of stacks

class Bottle:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.items = []
        self.used = 0
    
    def push(self, colour):
        self.top+=1
        self.items[self.top] = colour
        self.used+=1
    
    def pop(self):
        if self.isEmpty() is False:
            self.top-=1
            self.used-=1


    def isEmpty(self):
        return True if self.used == 0 and self.top == -1 else False
    
    def isFull(self):
        return True if self.used == self.size and self.used > 0 else False


    def search(self, colour):
        instances_of_colour = []
        for item in self.items:
            if item.lower() == colour.lower():  #want to be case insensitive 
                index = self.items.index(colour)
                instances_of_colour.append(index)

        return False if len(instances_of_colour) > 0 else instances_of_colour
    
    def isSorted(self):
        top = self.items[self.top]
        flag = True
        for item in self.items:
            if item.lower() != top.lower():
                flag = False
        
        return True if flag == True else False
    
    def emptySpaces(self):
        counter = 0
           
        for item in self.items:
            if item == 'e':
                counter+=1   
                     
        if self.isEmpty() == True:    #should i check isEmpty or isFull here or in pour f'n?
            counter = 4
        if self.isFull() == True:
            counter = 0
        
        return counter    #feel like im missing something here
            

def pour(initial_bottle, final_bottle):
    '''
    need to search in initial bottle
    	#if false return error message
    else count length of array returned
    then check emptySpaces of final bottle
		#if there are no empty spaces in final bottle return error message
	if there are empty spaces check top of both bottles
		#if tops match: 
			count how much of the same colour
   			increment final.used in a loop until either 
    
    '''
    pass
	


def user_input():
    pass