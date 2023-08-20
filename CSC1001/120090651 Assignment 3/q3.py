import random
class ecosystem:
    def __init__(self, length=None, fishes=None, bears=None):
        river = ['F']*fishes + ['B']*bears +['N']*(length-fishes-bears) #Initialize the river 
        random.shuffle(river)
        self.river = river
        self.empty = [index for index in range(len(self.river)) if self.river[index] == 'N']  #Index of 'N' (blank space)

    def random_move(self,index):
        dire = [0,1,-1]             #0:stay still 1:right -1:left
        if index == 0:
            dire.remove(-1)
        elif index == len(self.river)-1:
            dire.remove(1)
        direction = random.choice(dire)
        return direction 
        
    def Determine(self,_index,_direction):
        if _direction == 0:       #stay still
            return
        else:
            exchange = _index + _direction # New index that needs to exchange
            if self.river[exchange] =='N': #New index has nothing on it
                self.river[_index],self.river[exchange] = self.river[exchange],self.river[_index]
            elif self.river[_index] == self.river[exchange]:  # The two animals are the same and they are at the left-right position
                if self.empty == []:
                    return True  
                newIndex = random.choice(self.empty)
                self.river[newIndex] = self.river[_index]  
                return newIndex
            else:     # When two different animals are near, fish will die
                if self.river[_index] == 'F': 
                    self.river[_index] = 'N'
                else:
                    self.river[exchange] = 'N'

    def simulation(self):
        n = int(input('Enter the steps of simulation:'))
        for i in range(n):
            index = 0 
            while index <= len(self.river)-1:  
                if self.river[index] == 'N': # If there is no animal on this index, then continue to find the next one
                    index = index + 1
                    continue
                direction = self.random_move(index)   # Generate the random move
                newIndex = self.Determine(index, direction)  # Generate the procedure when animals are met
                if str(newIndex) =='True':   # No empty space is available, the river is full of bears
                    print('Not enough space! Goodbye~')
                    return
                self.empty = [index for index in range(len(self.river)) if self.river[index] == 'N']
                for i in self.river: # Print out the immediate process of the simulation
                    print(i,end='')
                print('')
                index = index + 1


length1 = int(input('Enter the length of the river: '))
fishes1 = int(input('Enter the number of fishes: '))
bears1 = int(input('Enter the number of bears: '))
a = ecosystem(length1, fishes1, bears1)
a.simulation()
