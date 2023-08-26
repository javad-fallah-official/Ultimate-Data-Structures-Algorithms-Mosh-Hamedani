class Array:
    def __init__(self, length):
        self.length = length
        self.values = [None] * self.length
        self.count = 0

    def insert(self, value):
        if self.count == self.length :
            #Pythonic way
            self.values.append(value)
            #'''#global way / the way used in course
            # (its not a good way at all btw becuase of high memory usage)
            # new_array = [None] * self.count * 2
            # for index, item in enumerate(self.values):
            #     new_array[index] = item
            # new_array[self.count]=value
            # self.values = new_array'''
            self.count +=1
            self. length += 1
        else:
            self.values[self.count] = value
            self.count += 1
            
    def print(self):
        for index in range(self.count):
            print(self.values[index])

    def removeAt(self, index):
        if index < 0 or index >= self.count:
            raise IndexError(f"Out of Index, the array have only {self.count} elements")
        else:
            for i in range(index,self.length-1):
                self.values[i] = self.values[i+1]
            self.count -= 1
                
    def indexOf (self,value):
        #pythonic
        if value not in self.values:
            return -1
        else:
            for index,item in enumerate(self.values):
                if item == value:
                    return index
        #non pythonic? 
        # for index,item in enumerate(self.values):
        #         if item == value:
        #             return index
        # return -1
        
            


