"""Part A tests. Your code goes in Lab8/stack.py."""
from stack import push, pop, top


def test_push_puts_item_on_top():
    stack = []
    push(stack, "A")
    push(stack, "B")
    assert stack == ["A", "B"]


def test_pop_returns_the_last_item_pushed():
    stack = ["A", "B", "C"]
    assert pop(stack) == "C"


def test_pop_removes_the_item():
    stack = ["A", "B", "C"]
    pop(stack)
    assert stack == ["A", "B"]


def test_pop_on_empty_stack_returns_none():
    stack = []
    assert pop(stack) is None
    assert stack == []


def test_top_returns_the_top_item():
    assert top(["A", "B", "C"]) == "C"


def test_top_does_not_remove_anything():
    stack = ["A", "B", "C"]
    top(stack)
    assert stack == ["A", "B", "C"]


def test_top_on_empty_stack_returns_none():
    stack = []
    assert top(stack) is None
    assert stack == []


def test_push_pop_push():
    # Push A, B, C. Pop one. Push D and E.
    stack = []
    push(stack, "A")
    push(stack, "B")
    push(stack, "C")
    assert pop(stack) == "C"
    push(stack, "D")
    push(stack, "E")
    assert stack == ["A", "B", "D", "E"]
    assert top(stack) == "E"
