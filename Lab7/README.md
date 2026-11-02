# Lab 7: Classes in Python

In Section 6.5 we looked at classes and objects with the laser example. In this lab you write your own classes in three files and check them with **pytest**, the testing tool real Python projects use.

You will create these three files yourself, inside the `Lab7` folder:

| File | What goes in it |
|---|---|
| `laser.py` | Part A. `LaserClass` and `RechargeableLaser` |
| `bank.py` | Part B. `BankAccount` and `SavingsAccount` |
| `people.py` | Part C. `Person`, `Student` and `Instructor` |

The tests are already written, in the `tests` folder. Don't edit them. Your job is to make them pass.

## Getting the lab

If you forked the repository for Lab 5, sync your fork to get the new `Lab7` folder. On your fork's GitHub page click **Sync fork**, then **Update branch**, then run `git pull` on your computer. If you haven't forked yet, follow the setup in the main [README](../README.md) first.

## Running the tests

Install pytest once.

```bash
python -m pip install pytest
```

Then run the tests from **inside the `Lab7` folder**.

```bash
cd Lab7
python -m pytest
```

(On a Mac, use `python3` wherever this says `python`.)

pytest prints a dot for each test that passes and an **F** for each one that fails, then a summary at the bottom. You're done when it says **29 passed**.

To run just one part while you work on it

```bash
python -m pytest tests/test_laser.py -v
```

The `-v` flag lists every test by name, so you can see exactly which ones still fail. When one fails, pytest shows the line of the test and the value your code gave. Read that, fix your code and run it again.

Before you write a file, its tests will fail with `ModuleNotFoundError`. That just means the file doesn't exist yet.

## Part A. `laser.py`

### `LaserClass`

| Name | What it does |
|---|---|
| `LaserClass(initial_power=100)` | Creates a laser. Sets `remaining_power` to `initial_power` and `direction` to `0`. |
| `remaining_power` | How much power is left, a number |
| `direction` | The angle in degrees, a number. 0 is straight up. |
| `turn_right()` | Adds 15 to `direction` |
| `turn_left()` | Subtracts 15 from `direction` |
| `fire()` | If `remaining_power` is at least 10, subtracts 10 and returns `True`. Otherwise changes nothing and returns `False`. |

### `RechargeableLaser(LaserClass)`

It inherits everything from `LaserClass` and adds

| Name | What it does |
|---|---|
| `RechargeableLaser(initial_power=100)` | Calls the parent's `__init__`, then sets `max_power` to `initial_power` |
| `max_power` | The power it started with |
| `recharge()` | Sets `remaining_power` back to `max_power` |

## Part B. `bank.py`

### `BankAccount`

| Name | What it does |
|---|---|
| `BankAccount(owner, balance=0)` | Creates an account. Sets `owner` and `balance`. |
| `owner` | The owner's name, a string |
| `balance` | The money in the account, a number |
| `deposit(amount)` | If `amount` is more than 0, adds it to `balance` and returns `True`. Otherwise changes nothing and returns `False`. |
| `withdraw(amount)` | If `amount` is more than 0 and no more than `balance`, subtracts it and returns `True`. Otherwise changes nothing and returns `False`. |
| `get_balance()` | Returns `balance` |

### `SavingsAccount(BankAccount)`

It inherits everything from `BankAccount` and adds

| Name | What it does |
|---|---|
| `SavingsAccount(owner, balance=0, annual_rate=0.03)` | Calls the parent's `__init__`, then sets `annual_rate` |
| `annual_rate` | The yearly interest rate as a decimal. 0.03 means 3% per year. |
| `add_monthly_interest()` | Works out one month of interest, adds it to `balance` and returns it. One month of interest is `balance * annual_rate / 12`, rounded to 2 decimals with `round(x, 2)`. |

At 6% per year, $1000 earns $5.00 in one month.

## Part C. `people.py`

### `Person`

| Name | What it does |
|---|---|
| `Person(name)` | Creates a person. Sets `name`. |
| `name` | A string |
| `introduce()` | Returns `"Hi, I'm Sam."` for a person named Sam |

### `Student(Person)`

| Name | What it does |
|---|---|
| `Student(name)` | Calls the parent's `__init__`, then sets `scores` to an empty list |
| `scores` | A list of numbers |
| `add_score(score)` | Adds `score` to the end of `scores` |
| `average()` | Returns the average of `scores`, or `0` if there are none |
| `introduce()` | Returns `"Hi, I'm Kai, a student."` for a student named Kai |

### `Instructor(Person)`

| Name | What it does |
|---|---|
| `Instructor(name, department)` | Calls the parent's `__init__`, then sets `department` |
| `department` | A string |
| `introduce()` | Returns `"Hi, I'm Dr. Lee and I teach Computer Science."` for Dr. Lee in Computer Science |

Notice that all three classes have an `introduce()` method that answers differently. That is polymorphism from Section 6.5.

## Submitting

1. Run `python -m pytest` one last time and take a screenshot of the summary line.
2. Commit and push your three files to your fork.

    ```bash
    git add laser.py bank.py people.py
    git commit -m "Finish Lab 7"
    git push
    ```

3. On Canvas, submit your fork's URL and upload the screenshot.

What is on GitHub at the due time is what gets graded.
