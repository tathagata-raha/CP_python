from queue import LifoQueue
 
# Initializing a stack
stack = LifoQueue(maxsize = 10)

stack.put(1)
stack.put(2)
stack.put(3)
stack.put(4)

print('\nElements poped from stack:')
print(stack.get())
print(stack.get())

print('\nStack after elements are poped:')
print(stack)