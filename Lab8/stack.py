"""Part A. A stack: last in, first out (Section 8.1).

The stack is a Python list. The END of the list is the TOP of the stack.
Replace each `pass` with your own code. Each function needs one or two lines.
"""


def push(stack, item):
    """Put item on the top of the stack."""
    stack.append(item)


def pop(stack):
    """Take the top item off the stack and return it.

    If the stack is empty, return None.
    """
    if len(stack) == 0: 
        return None
    else: 
        last = stack.pop() 
        return last


def top(stack):
    """Return the top item without removing it.

    If the stack is empty, return None.
    """
    if len(stack) == 0: 
        return None
    else:  
        last = stack[-1]
        return last 
