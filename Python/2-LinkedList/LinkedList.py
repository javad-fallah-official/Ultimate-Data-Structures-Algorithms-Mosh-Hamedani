class linkedlist:
    __first = None
    __last = None

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

    def addFirst(self, item):
        node = self.__Node(item)
        if self.__is_empty():
            self.__first = self.__last = node
        else:
            node.nextNode = self.__first
            self.__first = node

    def __is_empty(self):
        return self.__first is None
            

    def removeFirst(self):
        second = self.__first.nextNode
        self.__first = None
        self.__first = second
        
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
