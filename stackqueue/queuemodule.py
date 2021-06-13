from queue import Queue
 
# Initializing a q
q = Queue(maxsize = 10)

q.put(1)
q.put(2)
q.put(3)
q.put(4)

print('\nElements poped from queue:')
print(q.get())
print(q.get())

print('\nqueue after elements are poped:')
print(q)