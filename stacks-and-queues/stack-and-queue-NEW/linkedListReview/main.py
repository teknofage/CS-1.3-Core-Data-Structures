#linked list

#"hello" -> "hey" -> "hi" -> None

class Node:

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

class LinkedList:

  #Create
  def __init__(self):
    self.head = None
    self.tail = None

  #Update
  def append(self, new_node):
    #the linked is empty
    if self.tail is None:
      self.head = new_node
      self.tail = new_node
    else: #the linked has nodes
      self.tail.next = new_node
      self.tail = new_node

  #Read all the things
  def print_list(self):
    current = self.head
    while current != None:
      print(current.data)
      current = current.next

  #Delete
  def delete_from_tail(self):
    current = self.head
    while current != None:
      if current.next == self.tail:
        break
      current = current.next
    #have the node right before the tail
    current.next = None
    self.tail = current

my_ll = LinkedList()
my_ll.append(Node("hello"))
my_ll.append(Node("hi"))
my_ll.append(Node("hey"))
my_ll.append(Node("greetings"))

my_ll.print_list()

print("Delete item")
my_ll.delete_from_tail()
my_ll.delete_from_tail()
my_ll.print_list()