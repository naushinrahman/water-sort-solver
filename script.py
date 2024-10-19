# input: number of bottles first then loop through the bottles and add colour of each layer or empty
# does some stuff
# output: steps to take to sort in most efficient way similar to chess moves?

import sys

num_of_bottles = 2
array_of_bottles = [None] * num_of_bottles

# the bottles are an array of stacks

class Bottle:
    def __init__(self):
        self.top = -1
        self.size = 4
        self.items = [None] * self.size
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
    
    def print(self):
        for item in self.items:
            print(item)
      

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
    
    if initial_bottle.isEmpty():            #check if initial bottle is empty
        print('Nothing in initial bottle')
        return
	    
    top_colour = initial_bottle.top.lower()  #check top colour
    print(top_colour)
    
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


def user_input():
	global array_of_bottles
	count_of_bottles = num_of_bottles
	current_index = 0

	while count_of_bottles > 0:
		print('you have', count_of_bottles, 'bottles you need to fill')
		
		counter = 1
		temp = Bottle()

		while counter <= 4:
			print('Enter colour number ', counter)
			colour = input(' : ')
			temp.push(colour)
			counter+=1

		#temp.print()

		array_of_bottles[current_index] = temp

		current_index+=1
		count_of_bottles-=1

	for item in array_of_bottles:
		item.print()
		print('\n')
	#print(array_of_bottles)


# ex
# blue   yellow   blue   empty   empty
# blue   yellow    red   empty   empty
# yellow  red     red    empty   empty
# yellow  blue    red    empty   empty


user_input()