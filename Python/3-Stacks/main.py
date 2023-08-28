from stack import Stack
from stringReverser import StringReverser
from Expressions import Expression 

text = "abcdefg"
Implementation = "(([a[]]-zA{{}}-Z))"
text = StringReverser(text)
obj = Expression(Implementation)

print (obj.is_it_Balanced())

