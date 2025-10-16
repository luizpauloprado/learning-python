# stacks (LIFO - Last-In, First-Out)
# built-in list can effectively serve as a stack
print("stack:")
stack = [1, 2]
print(stack)
stack.append(3)  # Push
print(stack)

poped_value = stack.pop()  # Pop (removes and returns 3)
print(poped_value)

print(stack)  # Output: [1, 2]

# queues (FIFO - First-In, First-Out)
# collections.deque is more efficient for queue operations,
# especially for dequeuing from the front, as list.pop(0) has O(n) time complexity
print("queue:")
queue = [1, 2]
print(queue)
queue.append(3)
print(queue)

removed_value = queue.pop(0)  # Pop (removes and returns 1)
print(removed_value)

print(queue)  # Output: [2, 3]
