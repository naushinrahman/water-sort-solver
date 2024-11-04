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
        if self.is_full():
            print("Cannot add: Bottle is full")
            return
        if colour != 'empty':      #when it is a colour
            self.top_colour = colour
            self.used+=1
            self.top+=1
            self.items[self.top] = colour
    
    def pop(self):
        if self.is_empty():
            print("Cannot remove: Bottle is empty")
            return
        self.items[self.top] = None
        self.top-=1
        self.used-=1
        self.top_colour = self.items[self.top] if self.top >= 0 else None


    def is_empty(self):
        return True if self.used == 0 and self.top == -1 else False
    
    def is_full(self):
        return True if self.used == self.size and self.used > 0 else False
    
    def print(self):
        for i in range((self.size-1), -1, -1):
            print(self.items[i])

    def search(self, colour):       #returns array of top colour/emptyspaces
        instances_of_colour = []
        
        for i in range((self.used-1), -1, -1):
            if self.items[i] == colour:
                instances_of_colour.append(colour)
            else:               
                break
        return False if len(instances_of_colour) <= 0 else instances_of_colour
    
    def search_empty(self, colour):       #returns array of top colour/emptyspaces
        instances_of_colour = []
        
        for i in range((self.size-1), -1, -1):
            if self.items[i] == colour:
                instances_of_colour.append(colour)
            else:               
                break
        return False if len(instances_of_colour) <= 0 else instances_of_colour
    
    def return_top_colour(self):
        return self.top_colour
    
    def is_sorted(self):
        top = self.items[self.top]
        flag = True
        for item in self.items:
            if item.lower() != top.lower():
                flag = False
        return True if flag == True else False
    
    
    def empty_spaces(self):
        counter = 0
           
        for item in self.items:
            if item == 'e':
                counter+=1   
                     
        if self.is_empty() == True:    #should i check isEmpty or isFull here or in pour f'n?
            counter = 4
        if self.is_full() == True:
            counter = 0
        return counter    #feel like im missing something here
            

def pour(initial_bottle, final_bottle):
    
    if initial_bottle.is_empty():            #check if initial bottle is empty
        print('Error: Nothing in initial bottle, cannot pour')
        return
    
    if final_bottle.is_full():            
        print('Error: Bottle full, cannot pour')
        return
    
    top_colour = initial_bottle.return_top_colour()
    num_colour = len(initial_bottle.search(top_colour))
    
    if final_bottle.is_empty() is False:
        matching_top = final_bottle.return_top_colour()
        if matching_top != top_colour:
            print('Error: cannot pour on to a different colour')
            return
    
    num_of_spaces = len(final_bottle.search_empty(None))
    
    try:
        while num_of_spaces > 0 and num_colour > 0:
            final_bottle.push(top_colour)
            initial_bottle.pop()
            num_colour-=1
            num_of_spaces-=1
    except:
        print("Error: pour unsuccessful")
    

def sort():
    pass

def user_input():                    
	global array_of_bottles
	count_of_bottles = num_of_bottles
	current_index = 0

	while count_of_bottles > 0:
		print('you have', count_of_bottles, 'bottles you need to fill')
		
		counter = 1
		temp = Bottle()
		is_valid = True
		previous_was_empty = False

		while counter <= 4:
			colour = input(f'Enter colour number {counter} (from bottom to top): ').strip().lower()

			if colour == "" or colour == "empty":
				if not previous_was_empty:
					previous_was_empty = True
				else:
					print("Error: Empty spaces can only be on top of other empty spaces.")
					is_valid = False
					break
			else:
				previous_was_empty = False

			temp.push(colour)
			counter+=1

		if is_valid:
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
		print('\n')
		item.print()
		print('top colour: ', item.top_colour)
		print('index:', item.top)
		print('used:', item.used)


pour(array_of_bottles[0], array_of_bottles[1])

print('after pour:')

for item in array_of_bottles:  
		print('\n')
		item.print()
		print('top colour: ', item.top_colour)		
		print('index:', item.top)
		print('used:', item.used)