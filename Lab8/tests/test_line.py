"""Part B tests. Your code goes in Lab8/line.py."""
from line import enqueue, dequeue


def test_enqueue_adds_at_the_tail():
    queue = []
    enqueue(queue, "A")
    enqueue(queue, "B")
    assert queue == ["A", "B"]


def test_dequeue_returns_the_first_item_added():
    queue = ["A", "B", "C"]
    assert dequeue(queue) == "A"


def test_dequeue_removes_the_item():
    queue = ["A", "B", "C"]
    dequeue(queue)
    assert queue == ["B", "C"]


def test_dequeue_on_empty_queue_returns_none():
    queue = []
    assert dequeue(queue) is None
    assert queue == []


def test_first_in_first_out():
    queue = []
    enqueue(queue, "A")
    enqueue(queue, "B")
    enqueue(queue, "C")
    assert dequeue(queue) == "A"
    assert dequeue(queue) == "B"
    assert dequeue(queue) == "C"
