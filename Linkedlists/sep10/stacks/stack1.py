"""

stack implementation using lists

here time complexity to append is  o(n)
and also pop is also O(n)
"""
stack = []

stack.append("a")
stack.append("b")
stack.append("c")
print(f"initial stack {stack}")

print("popping the elements")

print(stack.pop())
print(stack.pop())
print(stack.pop())

print(f"all elements are popped={stack}")