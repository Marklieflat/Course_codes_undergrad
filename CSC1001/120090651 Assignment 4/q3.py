a = 'A'
c = 'C'
b = 'B'

class ListStack():
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self.data) == 0
    
    def push(self,value):
        self.data.append(value)
    
    def pop(self):
        if self.is_empty():
            print('It is empty')
        else: 
            last = self.data[-1]
            self.data = self.data[:-1]
            return last

    def top(self):
        if self.is_empty():
            print('It is empty')
        else:
            return self.data[len(self.data)-1]

    def getData(self):
        for i in self.data:
            print(i,end = ' ')
            print('THE END')


def movement(n,a = 'A',c = 'C',b = 'B'):
    s = ListStack()    
    s.push([n, a, c, b])   
    while s.is_empty() == False:  
        newlist = s.pop()
        n = newlist[0]
        if n == 1:  
            print(newlist[1] + ' --> ' + newlist[2]) 
            for i in range(3):  
                if s.is_empty():
                    break
                newlist = s.pop()
                print(newlist[1] + ' --> ' + newlist[2]) 
        else: 
            s.push([n-1, newlist[3], newlist[2], newlist[1]])  
            s.push(newlist)  
            s.push([n-1, newlist[1], newlist[3], newlist[2]])  

def main():
    n = int(input('Enter the number of disks:'))
    movement(n, a, c, b)

main()