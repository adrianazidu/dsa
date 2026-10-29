"""A stack is a linear data structure that follows the principle of Last In First Out (LIFO). This means the last element inserted inside the stack is removed first.
In programming terms, putting an item on top of the stack is called push and removing an item is called pop.
For the array-based implementation of a stack, the push and pop operations take constant time, i.e. O(1)
The operations work as follows:
A pointer called TOP is used to keep track of the top element in the stack.
When initializing the stack, we set its value to -1 so that we can check if the stack is empty by comparing TOP == -1.
On pushing an element, we increase the value of TOP and place the new element in the position pointed to by TOP.
On popping an element, we return the element pointed to by TOP and reduce its value.
"""

def create_stack():
    stack = [] #list
    return stack

def check_empty(stack)->bool:
    return len(stack)==0


def push(stack,item)->None:
    stack.append(item)

def pop(stack):
    if not check_empty(stack):
        return stack.pop()
    else:
        return None

stack = create_stack()
push(stack,str(1))
push(stack,str(2))
push(stack,str(3))
print("pop item" + pop(stack))
print("stack after " + str(stack))