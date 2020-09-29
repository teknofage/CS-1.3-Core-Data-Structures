#linked list

#"hello" -> "hey" -> "hi" -> None

class Node:

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

#create
#make nodes and link them together
#set head and tail
first_node = Node("hello")
another_node = Node("hey")
third_node = Node("Hi")
first_node.next = another_node
another_node.next = third_node

#print(first_node.next)
#print(another_node.next)
#print(third_node.next)

head = first_node
tail = third_node

#traverse
#read or visit each node
current = head
while current != None:

  #visit the Node
  print(current.data)
  #move on to the next node
  current = current.next

new_node = Node("greetings!")
#update
#append this new node to the end of the linked list
tail.next = new_node
tail = new_node

print("New node added")
current = head
while current != None:

  #visit the Node
  print(current.data)
  #move on to the next node
  current = current.next


#delete from the tail
#"hello" -> "hey" -> "hi" -> "greetings" -> None

#get the node that is right before the tail
current = head
while current != None:
  current = current.next
  if current.next == tail:
    break
#print(current.data)

#removing the current tail
current.next = None
#resetting the tail
tail = current

print("tail deleted")
current = head
while current != None:

  #visit the Node
  print(current.data)
  #move on to the next node
  current = current.next