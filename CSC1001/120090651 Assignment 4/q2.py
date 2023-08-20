class Node:
    def __init__(self, element, pointer):
        self.element = element
        self.pointer = pointer

class SinglyLinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def insert(self, data):
        firstdata = Node(data, None)
        if self.is_empty():
            self.head = firstdata
        else:
            self.tail.pointer = firstdata
        self.tail = firstdata
        self.size += 1

    def quick_sort(self, head):
        if head == None or head.pointer == None:
            return head
        less = SinglyLinkedList()
        greater = SinglyLinkedList()
        pivot = head.element   
        now = head
        while now != None:    
            if now.element < pivot:
                less.insert(now.element)   
            elif now.element > pivot:
                greater.insert(now.element) 
            now = now.pointer
        low = self.quick_sort(less.head)    
        high = self.quick_sort(greater.head)   
        head.pointer = high    
        try:
            tail = low
            while tail.pointer != None:   
                tail = tail.pointer
            tail.pointer = head    
        except:  
            low = head
        return low


def main():
    queue = SinglyLinkedList()
    lst = [5,2,3,9,8,7,10,13,26,1]
    for i in lst:
        queue.insert(i)
    head = queue.quick_sort(queue.head)
    now = head
    while now != None:
        print(now.element,end=' ')
        now = now.pointer
    print()

main()



