from LinkedList import linkedlist


link = linkedlist()

link.addLast(10)
link.addLast(20)
link.addLast(30)
link.addLast(40)
link.removeFirst()
print(link.IndexOf(10))
print(link.contains(20))
link.removeLast()
print(link.size())
print(link.Array())