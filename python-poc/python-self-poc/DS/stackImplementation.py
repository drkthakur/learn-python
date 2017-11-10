class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

# pop removes the top item from the list
# return the item and stack is modified.
    def pop(self):
        return self.items.pop()

# return top item from the list but stack not modified.
# Doesn't remove the top item.
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


# s = Stack()
# print(s.is_empty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.is_empty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())
