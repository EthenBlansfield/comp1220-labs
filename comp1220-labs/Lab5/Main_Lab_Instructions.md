# Lab 5: Algorithms in Python (Loops, Sorting, Searching, and Efficiency)

## Purpose

In Chapter 5 we described algorithms in pseudocode. In this lab you will turn several of those algorithms into working Python. Then you will measure them to check whether the textbook's efficiency predictions hold up.

Textbook: Brookshear & Brylow, *Computer Science: An Overview*, 13th ed., Sections 5.2–5.6.

## Learning goals

By the end of the lab, you should be able to:

1. Identify the **initialize, test, and modify** parts of a loop, and fix a loop that never terminates.
2. Write both a **pretest** (`while`) loop and a **posttest** (repeat…until) loop.
3. Turn a word problem into an algorithm by writing one function per clue.
4. Implement the **insertion sort** from pseudocode and count its comparisons.
5. Implement a **recursive binary search** and explain its base case.
6. Compare measured work with the textbook's best-case, worst-case, and average-case formulas.

## Points

| Problem | File | Topic | Code | Written | Total |
|---|---|---|---:|---:|---:|
| 1 | `p1_loop_control.py` | Loop control, pretest vs. posttest | 8 | 2 | **10** |
| 2 | `p2_euclid_gcd.py` | Euclidean algorithm, iterative and recursive | 10 | 0 | **10** |
| 3 | `p3_ages_puzzle.py` | From puzzle to algorithm (Section 5.3) | 12 | 3 | **15** |
| 4 | `p4_insertion_sort.py` | Insertion sort (Figure 5.11) | 18 | 7 | **25** |
| 5 | `p5_binary_search.py` | Recursive binary search (Figure 5.14) | 14 | 6 | **20** |
| 6 | `p6_efficiency_experiment.py` | Measuring efficiency (Section 5.6) | 5 | 10 | **15** |
| 7 | `p7_armstrong_numbers.py` | Armstrong numbers (Review Problem 38) | 5 | 0 | **5** |
| | | | **72** | **28** | **100** |

Written answers go in `written_answers.md`.

## Starting the lab

1. Clone or download the starter repository.
2. Open the `Lab5` folder in your editor. Every file must stay in the **same folder**, because each problem imports `lab5_data.py` and `lab5_checks.py`.
3. Work on one problem at a time. Replace each `raise NotImplementedError` line with your code.
4. Run the problem file from a terminal in the `Lab5` folder:

   ```bash
   python p1_loop_control.py
   ```

   Each check prints **PASS**, **FAIL** (with the expected and actual values), or **TODO**.
5. Passing every self-check is necessary but **not sufficient**. The grader also runs hidden tests and reads your code to make sure you followed each problem's rules.

### Rules for the whole lab

- Do **not** use `sort()`, `sorted()`, `min()`, `max()`, `sum()`, `math.gcd`, or any import that does the problem's work for you. (The provided check code uses `sorted()` to check *your* answer, and that's fine.)
- Do not edit `lab5_data.py` or `lab5_checks.py`.
- Use clear variable names and keep the structure of the book's pseudocode recognizable.

---

## Problem 1: Loop control (10 points)

File: `p1_loop_control.py` · Section 5.4

Section 5.4 shows a loop that starts `Number` at 1, adds 2 each time, and stops when `Number == 6`. It never stops. **Do not run that loop.**

1. **1a.** `odd_numbers_below(limit)`: collect 1, 3, 5, … below `limit` with a `while` loop that is guaranteed to stop.
2. **1b.** `total(numbers)`: add up a list with a **for-each** loop (`for number in numbers:`).
3. **1c.** `repeat_until_version()`: rewrite the pretest loop from Section 5.4, Question 2 as a **posttest** loop, using `while True:` with an `if …: break` as the last statement of the body.

**Written (2 pts):**

- Which of the three loop-control parts (initialize, test, modify) is "broken" in the book's never-ending loop?
- Exactly what change did your 1a make so the loop must terminate?

---

## Problem 2: The Euclidean algorithm (10 points)

File: `p2_euclid_gcd.py` · Section 5.2 Question 3, Review Problem 30

Write the greatest-common-divisor algorithm twice:

1. **2a.** `gcd(x, y)` uses a `while` loop.
2. **2b.** `gcd_recursive(x, y)` uses **no loops**. The function calls itself.

Use `%` for remainder. Test cases include `gcd(1071, 462) == 21`.

---

## Problem 3: Let the computer solve the ages puzzle (15 points)

File: `p3_ages_puzzle.py` · Section 5.3

We solved the "ages of three children" puzzle by hand in class. Now turn each clue into a function:

| Function | Clue |
|---|---|
| `triples_with_product(product)` | The ages multiply to `product`. |
| `repeated_sums(triples)` | Knowing the sum was **not** enough, so the sum must repeat. |
| `has_unique_oldest(triple)` | There is an oldest child. |
| `solve_ages(product)` | All three clues together. |

Your functions must work for **any** product, not only 36.

**Written (3 pts):**

1. Run `solve_ages` for at least three other products of your choice. Record which products give exactly **one** answer, which give none, and which give more than one.
2. Section 5.3 describes Polya's four problem-solving phases. Which phase does writing these functions correspond to, and which phase did step 1 above correspond to?

---

## Problem 4: Insertion sort (25 points)

File: `p4_insertion_sort.py` · Section 5.4, Figure 5.11

Translate the insertion sort pseudocode into Python. `insertion_sort(items, show=False)` must:

- sort the list **in place** (no second list)
- start the pivot at the **second** entry (Python index 1)
- save the pivot in a temporary variable, leaving a "hole"
- slide entries that are **greater than** the pivot down into the hole
- place the pivot in the final hole
- **count every comparison** between a list entry and the pivot, and return that count
- print the list after each pass of the outer loop when `show=True`

Data: `BAND_ROSTER` (12 unsorted names) in `lab5_data.py`.

**Written (7 pts):**

1. **Before running**, predict what `BAND_ROSTER` looks like after the first **four** passes of the outer loop. Then run the file and compare. Copy both your prediction and the actual output into the answer sheet.
2. For the **outer** loop and for the **inner** loop, name the initialize, test, and modify steps in *your* code.
3. Section 5.4, Question 5: why would changing "greater than" to "greater than or equal to" in the inner loop be a bad idea? Try it with the duplicate list `["Fay", "Al", "Fay", "Bo"]` and describe what changes.

---

## Problem 5: Recursive binary search (20 points)

File: `p5_binary_search.py` · Section 5.5, Figure 5.14

Write `binary_search(items, target, visited)`:

- It must be **recursive**, with no `while` or `for` loops inside it.
- The "middle" is the **first entry of the second half**: index `len(items) // 2`.
- Use slices for the sublists: `items[:m]` and `items[m + 1:]`.
- Append every test entry you examine to `visited`.
- Return `True` or `False`.

Data: `CLASS_ROSTER` (31 sorted names).

**Written (6 pts):**

1. Pick a name that is **not** one of the self-check names. Some should be on the roster, and at least one should be absent. **Predict** the `visited` list for each name, then run it and record the actual result.
2. What are the **base cases** (termination conditions) of your function?
3. When searching for `"Gideon"`, how many activations ("copies") of `binary_search` exist at the moment `"Gideon"` is found?
4. Why does binary search give wrong answers on an **unsorted** list? Give a small example list and target that fails.

---

## Problem 6: Measure efficiency (15 points)

File: `p6_efficiency_experiment.py` · Section 5.6

Finish Problems 4 and 5 first. This program imports your `insertion_sort` and `binary_search`.

**Code (5 pts):** complete `make_list(n, order)` and `max_interrogations(sorted_list, targets)`.

When you run the file, it prints two tables:

- comparisons made by **your** insertion sort on sorted, reversed, and shuffled lists of 10 to 320 numbers, next to the textbook formulas
- the most entries **your** binary search ever visits on lists of up to 100,000 student IDs, next to log₂(n)

**Written (10 pts):** copy both tables into `written_answers.md` and answer:

1. Do your best-case and worst-case counts match the formulas exactly? If not, find the reason.
2. How close is the shuffled count to the average-case estimate?
3. When n **doubles**, about how much does the worst-case number of comparisons grow? What about binary search?
4. Section 5.6 describes a registrar searching 30,000 student records. Use your table to explain why binary search makes that search feel instant.
5. Insertion sort's best case is very fast. Describe a real situation where data arrives *almost* sorted.

---

## Problem 7: Armstrong numbers (5 points)

File: `p7_armstrong_numbers.py` · Chapter 5 Review Problem 38

An Armstrong number equals the sum of the **cubes** of its digits (for example, 153 = 1³ + 5³ + 3³). Use `% 10` and `// 10` in a `while` loop to pull digits apart. Do not convert the number to a string. List every Armstrong number below 1000.

---

## Submission checklist

Submit the whole `Lab5` folder, containing:

- [ ] `p1_loop_control.py` through `p7_armstrong_numbers.py`, completed
- [ ] `written_answers.md`, with every question answered and both Problem 6 tables pasted in
- [ ] the unchanged `lab5_data.py` and `lab5_checks.py`

Before submitting, run every problem file and confirm that it runs without errors.
