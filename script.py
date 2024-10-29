# output: steps to take to sort in most efficient way similar to chess moves?

num_of_bottles = 2
array_of_bottles = [None] * num_of_bottles

# the bottles are an array of stacks

class Bottle:
    def __init__(self):
        self.top = -1
        self.size = 4
        self.items = [None] * self.size
        self.used = 0
        self.top_colour = None
    
    def push(self, colour):
        if self.isFull():
            print("Error: Cannot add: Bottle is full")
            return
        self.top+=1
        self.items[self.top] = colour
        if colour != 'empty':
            self.used+=1
            self.top_colour = colour
    
    def pop(self):
        if self.isEmpty():
            print("Error: Cannot remove: Bottle is empty")
            return
        if self.top_colour == 'empty':
            print("Error: Cannot pop, top is empty")
            return
        self.top_colour = 'empty'
        self.top-=1
        self.used-=1
        self.top_colour = self.items[self.top] if self.top >= 0 else 'empty'


    def isEmpty(self):
        return True if self.used == 0 and self.top == -1 else False
    
    def isFull(self):
        return True if self.used == self.size and self.used > 0 else False
    
    def print(self):
        for i in range(self.top, -1, -1):
            print(self.items[i])

    def search(self, colour):
        instances_of_colour = []
        for i in range(self.top, -1, -1):
            if self.items[i] == colour:               
                instances_of_colour.append(colour)
        return False if len(instances_of_colour) <= 0 else instances_of_colour
    
    
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
    
    if initial_bottle.isEmpty():            #check if initial bottle is empty
        print('Error: Nothing in initial bottle, cannot pour')
        return
	    
    top_colour = initial_bottle.top_colour  
    num_colour = len(initial_bottle.search(top_colour))
    
    try:
        num_of_spaces = len(final_bottle.search('empty'))
    except TypeError:
        print('Error: Bottle full, cannot pour')
    
    matching_top = final_bottle.search(top_colour)
    if matching_top != top_colour:
        print('Error: cannot pour on to a different colour')
        return
    
    while num_of_spaces > 0:
        
        final_bottle.used+=1
        initial_bottle.used-=1
        num_colour-=1
        num_of_spaces-=1
    
    
'''
need to search in initial bottle
	#if false return error message
else count length of array returned
then check emptySpaces of final bottle in a var
	#if there are no empty spaces in final bottle return error message
if there are empty spaces check top of both bottles
	#if tops match: 
		count how much of the same colour in initial bottle in a var
		while emptySpaces > 0: final.used+=1, initial.used-=1, emptySpaces-=1 
'''

def sort():
    pass

def user_input():                      #add documentation for this function
	global array_of_bottles
	count_of_bottles = num_of_bottles
	current_index = 0

	while count_of_bottles > 0:
		print('you have', count_of_bottles, 'bottles you need to fill')
		
		counter = 1
		temp = Bottle()

		while counter <= 4:
			print('Enter colour number ', counter, '(from bottom to top)')
			colour = input(' : ')  #need to check: emptySpaces can only have other emptySpaces on top
								   #and that im taking lower case input only
			temp.push(colour)
			counter+=1

		array_of_bottles[current_index] = temp

		current_index+=1
		count_of_bottles-=1


# ex
# blue   yellow   blue   empty   empty
# blue   yellow    red   empty   empty
# yellow  red     red    empty   empty
# yellow  blue    red    empty   empty


user_input()

for item in array_of_bottles:  
		item.print()
		print('\n')
		print('top colour: ', item.top_colour)
		print('\n')


pour(array_of_bottles[0], array_of_bottles[1])