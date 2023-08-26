class linkedlist:
    __first = None
    __last = None
    __size = 0
    class __Node:
        def __init__(self, value, nextNode=None):
            self.value = value
            self.nextNode = nextNode

    def addLast(self, item):
        
        node = self.__Node(item)
        if self.__is_empty():
            self.__first = self.__last = node
        else:
            self.__last.nextNode = node
            self.__last = node
            
        self.__size +=1

    def addFirst(self, item):
        node = self.__Node(item)
        if self.__is_empty():
            self.__first = self.__last = node
        else:
            node.nextNode = self.__first
            self.__first = node
        self.__size +=1

    def __is_empty(self):
        if self.__first is None:
            return True
        else:
            return False
                 
    def IndexOf(self, item):
        index = 0
        current = self.__first
        while current is not None:
            if current.value == item: return index
            current = current.nextNode
            index += 1
        return -1
    
    def contains(self, item):
        if self.IndexOf(item) == -1:
            return False
        else:
            return True
        
    def removeFirst(self):
        if self.__is_empty():
            return None
        elif self.__first == self.__last:
            self.__first = self.__last = None
        else:
            second = self.__first.nextNode
            self.__first = None
            self.__first = second
        self.__size -=1
        
    def removeLast(self):
        if self.__is_empty():
            return None
        elif self.__first == self.__last:
            self.__first = self.__last = None
        else:
            previous = self.getPrevious(self.__last)
            self.__last = previous
            self.__last.nextNode = None
        self.__size -=1
        
    def getPrevious(self,lastnode):
        current = self.__first
        while current!= None:
            if current.nextNode == lastnode: return current
            current = current.nextNode     
        return None
    
    def size (self):
        return self.__size
    
    def Array (self):
        result = []
        current = self.__first
        while current != None:
            result.append(current.value)
            current = current.nextNode
        return result