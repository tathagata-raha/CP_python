from collections import deque
 
dq = deque()

dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)
dq.append(5)
dq.append(6)
 
print('Initial deque')
print(dq)

print('\nElements poped from deque:')
print(dq.pop())
print(dq.pop())
 
print('\nElements poped from left:')
print(dq.popleft())
print(dq.popleft())

print('\ndq after elements are poped:')
print(dq)