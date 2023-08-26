from LinkedList import linkedlist


link = linkedlist()

link.addLast(10)
link.addLast(20)
link.addLast(30)
link.addLast(40)
link.addLast(50)
link.addLast(60)
link.addLast(70)
link.addLast(80)
link.removeFirst()
print(link.IndexOf(10))
print(link.contains(20))
link.removeLast()
print(link.size())
print(link.Array())
print(link.reverse())
print(link.Array())
print(link.getKthFromEnd(7))