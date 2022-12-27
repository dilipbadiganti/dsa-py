class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
  
class SLL:
  def __init__(self):
    self.head = None

# creating nodes
n1 = Node(111)
n2 = Node(112)
n3 = Node(113)
n4 = Node(114)

#creating linked list object for SLL class:

ll = SLL()

#set n1 as the head node
#and n2 as n1's next, n3 as n2's next and so on...
ll.head = n1
n1.next = n2
n2.next = n3
n3.next = n4


#put head in a temp variable for traversing to the last node

#why traversing to last node?

#becasue we need to start printing till the head is empty ie last node

temp_node = ll.head
while temp_node is not None:
  print(temp_node.data,"-->",end=" ")
  temp_node = temp_node.next
