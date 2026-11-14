# Lab 8: Stacks, Queues and Arrays

In Chapter 8 we looked at stacks, queues and how a table is stored in memory. In this lab you finish three small files and check them with **pytest**, the same way as Lab 7.

This lab is short. The files are already there, and each function needs only one or two lines.

| File | What goes in it |
|---|---|
| `stack.py` | Part A. `push`, `pop` and `top` |
| `line.py` | Part B. `enqueue` and `dequeue` |
| `address.py` | Part C. `address` |

Open each file and replace every `pass` with your own code. Don't edit the files in the `tests` folder.

## Getting the lab

On your fork's GitHub page click **Sync fork**, then **Update branch**, then run `git pull` on your computer. You will see a new `Lab8` folder.

## Running the tests

Run the tests from **inside the `Lab8` folder**.

```bash
cd Lab8
python -m pytest
```

(On a Mac, use `python3` wherever this says `python`.)

You're done when it says **18 passed**. Before you write anything, most of them fail. That is expected.

To run just one part while you work on it

```bash
python -m pytest tests/test_stack.py -v
```

## Part A. `stack.py`

A stack is last in, first out. Think of a stack of plates. You add to the top and take from the top.

Our stack is a Python list, and the **end** of the list is the **top** of the stack.

| Function | What it does |
|---|---|
| `push(stack, item)` | Adds `item` to the top of the stack |
| `pop(stack)` | Removes the top item and returns it. Returns `None` if the stack is empty. |
| `top(stack)` | Returns the top item without removing it. Returns `None` if the stack is empty. |

Three things about Python lists that you will need

```python
letters = ["A", "B"]
letters.append("C")    # letters is now ["A", "B", "C"]
last = letters.pop()   # last is "C" and letters is ["A", "B"]
letters[-1]            # the last item, "B", and nothing is removed
```

To check for an empty list, use `if len(stack) == 0:`.

## Part B. `line.py`

A queue is first in, first out, like a line at a store. You join at the tail and leave from the head.

Our queue is a Python list. The **front** of the list is the **head** and the **end** of the list is the **tail**.

| Function | What it does |
|---|---|
| `enqueue(queue, item)` | Adds `item` at the tail of the queue |
| `dequeue(queue)` | Removes the item at the head and returns it. Returns `None` if the queue is empty. |

One more thing about Python lists

```python
letters = ["A", "B", "C"]
first = letters.pop(0)   # first is "A" and letters is ["B", "C"]
```

## Part C. `address.py`

A table is stored in memory one row after another. The book calls this row major order (Section 8.3).

Here is a table with 5 columns that starts at address 100. Each box shows the address of that entry.

| | col 1 | col 2 | col 3 | col 4 | col 5 |
|---|---|---|---|---|---|
| **row 1** | 100 | 101 | 102 | 103 | 104 |
| **row 2** | 105 | 106 | 107 | 108 | 109 |
| **row 3** | 110 | 111 | 112 | 113 | 114 |

| Function | What it does |
|---|---|
| `address(x, cols, row, col)` | Returns the address of the entry at `row` and `col`, for a table with `cols` columns that starts at address `x` |

So `address(100, 5, 3, 4)` is `113`.

To get to row 3 you skip 2 full rows. To get to column 4 you skip 3 entries in that row. Turn that into one line of arithmetic.

## Submitting

1. Run `python -m pytest` one last time and take a screenshot of the summary line.
2. Commit and push your three files to your fork.

    ```bash
    git add stack.py line.py address.py
    git commit -m "Finish Lab 8"
    git push
    ```

3. On Canvas, submit your fork's URL and upload the screenshot.

What is on GitHub at the due time is what gets graded.
