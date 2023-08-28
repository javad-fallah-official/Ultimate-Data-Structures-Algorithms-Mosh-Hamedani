from stack import Stack
# from abc import classmethod

class Expression:
    opens = ["(", "[", "<", "{"]
    closes = [")", "]", ">", "}"]

    def __init__(self, text):
        self.text = text

    def is_it_Balanced(self):
        self.stack = Stack()
        
        for char in self.text:
            
            if char in self.opens:
                self.stack.push(char)
                
            if char in self.closes:
                if self.stack.isEmpty(): return False
                
                top = self.stack.pop()
                if not Expression.does_match(top, char):
                    return False

        return self.stack.isEmpty()
    
    @classmethod
    def does_match(cls,open,close):
        return cls.opens.index(open) == cls.closes.index(close)
