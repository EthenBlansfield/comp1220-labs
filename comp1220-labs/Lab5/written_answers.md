# Lab 5: Written Answers

Name: 

Ethen Blansfield

## Problem 1 (2 pts)

**Which loop-control part is broken in the book's never-ending loop?**
The loop control part that is broken in the book's never-ending loop is the while part since while (Number !=6) while not terminate and continue to go on forever. 
**What change in your 1a guarantees termination?**
The change was making the while statement (number_to_print < limit) since the statement while terminate and not go on forever. 
---

## Problem 3 (3 pts)

| Product | `solve_ages` result | One, none, or many answers? |
|---:|---|---|
|72 |(3,3,8) | one answer|
|90  |(1, 9, 10), (2, 3, 15), (2, 5, 9), (3, 3, 10) |  many answers|
|120  |none| no answers|

**Which Polya phase is writing the functions? Which phase is trying other products?**
The Polya phase that is writing the functions is the phase in which you carry out the plan. The phase that is trying other products is when you evaluate the solution you created. 
---

## Problem 4 (7 pts)

**1. Prediction (written BEFORE running):** the list after outer passes 1–4.

```text
pass 1: ['Dev, Marisol, Quinn, Abel, Tamsin, Jonah, Beatriz, Ollie, Keiko, Hugo, Ingrid, Erza']
pass 2: ['Abel, Dev, Marisol, Quinn, Tamsin, Jonah, Beatriz, Ollie, Keiko, Hugo, Ingrid, Erza']
pass 3: ['Abel, Dev, Marisol, Quinn, Tamsin, Jonah, Beatriz, Ollie, Keiko, Hugo, Ingrid, Erza'] 
pass 4: ['Abel, Dev, Jonah, Marisol, Quinn, Tasmin, Beatriz, Ollie, Keiko, Hugo, Ingrid, Erza']
```

**Actual output (copied from the run):**

```text 
['Marisol', 'Dev', 'Quinn', 'Abel', 'Tamsin', 'Jonah', 'Beatriz', 'Ollie', 'Keiko', 'Hugo', 'Ingrid', 'Ezra']
['Dev', 'Marisol', 'Quinn', 'Abel', 'Tamsin', 'Jonah', 'Beatriz', 'Ollie', 'Keiko', 'Hugo', 'Ingrid', 'Ezra']
['Dev', 'Marisol', 'Quinn', 'Abel', 'Tamsin', 'Jonah', 'Beatriz', 'Ollie', 'Keiko', 'Hugo', 'Ingrid', 'Ezra']
['Abel', 'Dev', 'Marisol', 'Quinn', 'Tamsin', 'Jonah', 'Beatriz', 'Ollie', 'Keiko', 'Hugo', 'Ingrid', 'Ezra']
['Abel', 'Dev', 'Marisol', 'Quinn', 'Tamsin', 'Jonah', 'Beatriz', 'Ollie', 'Keiko', 'Hugo', 'Ingrid', 'Ezra']
['Abel', 'Dev', 'Jonah', 'Marisol', 'Quinn', 'Tamsin', 'Beatriz', 'Ollie', 'Keiko', 'Hugo', 'Ingrid', 'Ezra']
['Abel', 'Beatriz', 'Dev', 'Jonah', 'Marisol', 'Quinn', 'Tamsin', 'Ollie', 'Keiko', 'Hugo', 'Ingrid', 'Ezra']
['Abel', 'Beatriz', 'Dev', 'Jonah', 'Marisol', 'Ollie', 'Quinn', 'Tamsin', 'Keiko', 'Hugo', 'Ingrid', 'Ezra']
['Abel', 'Beatriz', 'Dev', 'Jonah', 'Keiko', 'Marisol', 'Ollie', 'Quinn', 'Tamsin', 'Hugo', 'Ingrid', 'Ezra']
['Abel', 'Beatriz', 'Dev', 'Hugo', 'Jonah', 'Keiko', 'Marisol', 'Ollie', 'Quinn', 'Tamsin', 'Ingrid', 'Ezra']
['Abel', 'Beatriz', 'Dev', 'Hugo', 'Ingrid', 'Jonah', 'Keiko', 'Marisol', 'Ollie', 'Quinn', 'Tamsin', 'Ezra']
['Abel', 'Beatriz', 'Dev', 'Ezra', 'Hugo', 'Ingrid', 'Jonah', 'Keiko', 'Marisol', 'Ollie', 'Quinn', 'Tamsin']

**2. Loop control in your code**

| Loop | Initialize | Test | Modify |
|---|---|---|---|
| Outer | i starts at 1  | check whether i is less than the length of the list (12) | i increases by 1 each iteration of the for loop |
| Inner | j starts at one position before i  |  check if j is greater than or equal to 0| j decreases by -1 for each iteration of the while loop  |

**3. Why "greater than" and not "greater than or equal to"?** What changed with `["Fay", "Al", "Fay", "Bo"]`?
Why "greater than" and not "greater than or equal to" is a "greater than or equal to" would lead to the list not being sorted and the final output being the same as the orignal list, since Fay is greater than Al and Bo, so the output of ["Fay", "Al", "Fay", "Bo"] is ["Fay", "Al", "Fay", "Bo"], not ["Al, Bo, Fay, Fay'].

## Problem 5 (6 pts)

**1. Predictions vs. results**

| Target | On roster? | Predicted `visited` | Actual `visited` |
|Benedict|Yes|4|4|
|Isador|Yes|5|5|
|Eamon |Yes|5|5|
|Harper|Yes|2|2|

**2. Base cases:**
The  base cases (termination conditions) of my function is that if the len[mid_item] == 1 the function is to return false. 

**3. Number of activations when "Gideon" is found:**
The number of activations when "Giden was found was that 5 binary_search existed. 

**4. An unsorted list and target where binary search fails:**
Why a binary search will give wrong answers on an unsorted list is in a  binary search a item is bigger than another depending on where it is in the list, and not if the string or integer is bigger than the previous one. So if you have the list [2, 4, 8, 6, 1, 5], the search would fail. Since 5 is smaller than 6, but, since 5 is after 6, it reads 5 as bigger than six and the search would not work. 
---

## Problem 6 (10 pts)

**Insertion sort table (paste):**
    n |   sorted      n-1 |  reversed  (n^2-n)/2 |  shuffled  (n^2-n)/4
---------------------------------------------------------------------------
   10 |        9        9 |        45         45 |        33       22.5
   20 |       19       19 |       190        190 |       122       95.0
   40 |       39       39 |       780        780 |       439      390.0
   80 |       79       79 |      3160       3160 |      1583     1580.0
  160 |      159      159 |     12720      12720 |      6833     6360.0
  320 |      319      319 |     51040      51040 |     25958    25520.0
**Binary search table (paste):**
   n | max visited |  log2(n)
----------------------------------
     15 |           4 |     3.91
    100 |           7 |     6.64
    200 |           8 |     7.64
   1000 |          10 |     9.97
  30000 |          15 |    14.87
 100000 |          17 |    16.61

1. Do best and worst cases match the formulas exactly?
The best and worst case counts match the formulas almost exactly exepcted for shuffled. Why shuffled was off compared to the others is that there are mutiple ways to shuffled a list to make it sorted, but with the others they follow an exact way to either sort or search a table. 
2. How close is the shuffled count to the average-case estimate?
The shuffled counts are not that close to ther average-case estimate. 
3. What happens to the work when n doubles (insertion sort vs. binary search)?
With binary search the worst-case numbers do not grow as larger compared to n. While with insertion sort, when n is doubled the worst-case numbers grow a lot compared to n. 
4. Why does binary search make the registrar's 30,000-record search feel instant?
With binary search it cuts the records into half and keeps cutting the records in half until the search is completed. However, with insertion sort, it goes through each record which makes the search take a lot longer. 
5. A real situation where data arrives almost sorted: A list of finanical transactions