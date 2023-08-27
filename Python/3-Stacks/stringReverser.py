from stack import Stack

class StringReverser():
    def __init__(self,text):
        self.stack = Stack()
        self.text = text
    def __str__(self):
        result = ""
        for ch in self.text:
            self.stack.push(ch)
        while not self.stack.is_empty():
            result += self.stack.pop()
        return result