#A linked list is a linear data structure that includes a series of connected nodes. 
#Here, each node stores the data and the address of the next node
#You have to start somewhere, so we give the address of the first node a special name called HEAD.
# Also, the last node in the linked list can be identified because its next portion points to NULL

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

def TraverseAndPrint(head):
    currentNode=head
    while currentNode:
        print(currentNode.data,end=" ")
        currentNode = currentNode.next

node1 = Node(7)
node2=Node(11)
node3=Node(3)
node4=Node(2)
node5=Node(9)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

TraverseAndPrint(node1)