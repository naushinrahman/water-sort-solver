
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
        if colour == 'empty':
            colour = None     
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
    
    def print_items(self):
        for i in range((self.size-1), -1, -1):  #display all items from top of Bottle to bottom
            print(self.items[i])

    def search(self, colour):       #returns array of top colour
        if self.top_colour != colour:
            return False
        
        instances_of_colour = 0
        
        for i in range((self.used-1), -1, -1):    #starting from the top of the Bottle
            if self.items[i] == colour:           #if the top item and contiguous items match colour argument
                instances_of_colour+=1            #increment counter
            else:               
                break      #the first non matching item causes a break
        return instances_of_colour  
    
    def search_empty(self):       #returns array of emptyspaces at top of Bottle
        array_of_empty = 0
        
        for i in range((self.size-1), -1, -1):
            if self.items[i] == None:
                array_of_empty+=1
            else:               
                break
        return array_of_empty
    
    def is_sorted(self):
        flag = True
        for item in self.items:
            if item != self.top_colour:
                flag = False
        return flag
            
class MoveTracker:
    def __init__(self):
        self.moves = []  # To store all moves as tuples (source_bottle, target_bottle)

    def record_move(self, source, target):
        self.moves.append((source, target))

    def get_moves(self):
        return self.moves

    def undo_last_move(self, array_of_bottles):
        if not self.moves:
            print("No moves to undo.")
            return

        source, target = self.moves.pop()

        top_colour = array_of_bottles[target].top_colour
        array_of_bottles[target].pop()
        array_of_bottles[source].push(top_colour)

        print(f"Undo: Pour from Bottle {target + 1} back to Bottle {source + 1}")


def pour(initial_bottle, final_bottle):
    
    if initial_bottle.is_empty():            #check if initial bottle is empty
        print('Error: Nothing in initial bottle, cannot pour')
        return
    
    if final_bottle.is_full():            #check if final bottle is full
        print('Error: Bottle full, cannot pour')
        return
    
    top_colour = initial_bottle.top_colour          #find top colour
    num_colour = initial_bottle.search(top_colour)  #find how many layers of top colour are contiguous
    
    if final_bottle.is_empty() is False:            #if final bottle has some liquid 
        if top_colour != final_bottle.top_colour:   #if top colours of each bottle dont match
            print('Error: cannot pour on to a different colour')
            return
    
    num_of_spaces = final_bottle.search_empty()   #find how many empty spaces are in the final bottle
    
    try:
        while num_of_spaces > 0 and num_colour > 0:  #if there is still liquid to pour and space in the final bottle
            final_bottle.push(top_colour)            #pour 1 layer of liquid into final bottle
            num_of_spaces-=1
            initial_bottle.pop()                     #delete that layer of liquid from inital bottle
            num_colour-=1
    except:
        print("Error: pour unsuccessful")          #if any issues pouring print error message
    

def sort():
    moves = []
    visited_states = set()
    sorted_bottles = [bottle.is_sorted() if bottle else True for bottle in array_of_bottles]
    MAX_MOVES_PER_PAIR = 5  # Limit moves between specific pairs
    move_count = {}
    
    def encode_state(bottles):
        return tuple(tuple(bottle.items) if bottle else None for bottle in bottles)
    
    while not all(sorted_bottles):
        move_found = False
        
        state = encode_state(array_of_bottles)

        if state in visited_states:
            print("State already visited. Skipping further exploration.")
            break

        visited_states.add(state)
        
        for i, bottle in enumerate(array_of_bottles):
            print(f"Bottle {i + 1}: {bottle.items}")
            if bottle.is_empty() or bottle.is_sorted():
                continue
            top_colour = bottle.top_colour

            for j, target_bottle in enumerate(array_of_bottles):
                if i == j or target_bottle.is_full():
                    continue
                if target_bottle.is_empty() or target_bottle.top_colour == top_colour:
                    pour(bottle, target_bottle)
                    moves.append(f"Pour from Bottle {i + 1} to Bottle {j + 1}")
                    move_found = True
                    break
            if move_found:
                break

        sorted_bottles = [bottle.is_sorted() for bottle in array_of_bottles]
         
        if not move_found:
            print("No more moves found. Sorting may not be possible.")
            break

    return moves


def user_input():                    
	global array_of_bottles  #ask user how many bottles
	count_of_bottles = num_of_bottles  #want button for empty bottles
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



num_of_bottles = 3
array_of_bottles =  [Bottle() for _ in range(num_of_bottles)]

array_of_bottles[0].push("red")
array_of_bottles[0].push("blue")
array_of_bottles[1].push("blue")
array_of_bottles[1].push("red")

for idx, bottle in enumerate(array_of_bottles):
    print(f"Bottle {idx + 1}: {bottle.items}\n")

moves = sort()
print("Moves:", moves)

for idx, bottle in enumerate(array_of_bottles):
    print(f"Bottle {idx + 1}: {bottle.items}")


# if __name__ == "__main__":
#     user_input()
    
#     for item in array_of_bottles:  
#         print('\n')
#         item.print_items()
#         print('top colour: ', item.top_colour)
#         print('index:', item.top)
#         print('used:', item.used)
    
#     pour(array_of_bottles[0], array_of_bottles[1])
    
#     print('after pour:')
#     for item in array_of_bottles:  
#         print('\n')
#         item.print_items()
#         print('top colour: ', item.top_colour)
#         print('index:', item.top)
#         print('used:', item.used)

