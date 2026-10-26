"""Problem 6 - Measure efficiency (15 points)                Section 5.6

Section 5.6 predicts how much work our algorithms do:

    Insertion sort on n entries
        best case  (already sorted):  n - 1             comparisons
        worst case (reverse order):   (n*n - n) / 2     comparisons
        average case:                 (n*n - n) / 4     comparisons (about)
    Binary search on n entries
        at most about  log2(n)  entries interrogated  (rounded up)

In this problem you TEST those predictions using YOUR code from
Problems 4 and 5. Finish Problems 4 and 5 first.

Part A (code): complete the two functions marked TODO.
Part B (writing): run this file, copy the tables into written_answers.md,
and answer the questions there.

Run:   python p6_efficiency_experiment.py
"""

import math
import random

from lab5_checks import check, run, summary
from lab5_data import student_ids
from p4_insertion_sort import insertion_sort
from p5_binary_search import binary_search

SIZES = [10, 20, 40, 80, 160, 320]


def make_list(n, order):
    """Return a list of the numbers 1..n arranged in the given order.

    order is "sorted", "reversed", or "shuffled". A shuffled list uses
    random.Random(n) so everyone gets the same "random" list.
    """
    # TODO: build and return the list. Hint: list(range(1, n + 1)),
    #       reversed(...), and random.Random(n).shuffle(the_list)
    if order not in ("sorted, reversed, shuffled"): 
        raise 
    if order == "sorted":
        ordered_list =[] 
        index = 1
        while index <= n: 
            ordered_list.append(index) 
            index += 1 
        return ordered_list 
    elif order == "reversed": 
        ordered_list = [] 
        index = 1 
        while index <= n: 
            ordered_list.append((n-index)+1) 
            index +=1   
        return ordered_list 

    elif order == "shuffled":  
        ordered_list =[] 
        index = 1
        while index <= n: 
            ordered_list.append(index) 
            index += 1 
        random.shuffle(ordered_list)  
        return ordered_list
    







def max_interrogations(sorted_list, targets):
    """Binary-search sorted_list for each target. Return the LARGEST number
    of entries visited by any single search."""
    # TODO: use binary_search(sorted_list, target, visited) from Problem 5.
    current_number_of_items_visited = -100000 

    for my_target in targets: 
        visited = [] 
        binary_search(sorted_list, target= my_target, visited = visited) 
        number_of_items_visited = len(visited) 
        #print (number_of_items_visited) 
        if current_number_of_items_visited < number_of_items_visited: 
            current_number_of_items_visited = number_of_items_visited 
             
    return current_number_of_items_visited



def sort_table():
    print(f"\n{'n':>5} | {'sorted':>8} {'n-1':>8} | {'reversed':>9} {'(n^2-n)/2':>10} | {'shuffled':>9} {'(n^2-n)/4':>10}")
    print("-" * 75)
    for n in SIZES:
        counts = {}
        for order in ("sorted", "reversed", "shuffled"):
            items = make_list(n, order)
            counts[order] = insertion_sort(items)
        print(f"{n:>5} | {counts['sorted']:>8} {n - 1:>8} | {counts['reversed']:>9} {(n * n - n) // 2:>10} |"
              f" {counts['shuffled']:>9} {(n * n - n) / 4:>10.1f}")


def search_table():
    print(f"\n{'n':>7} | {'max visited':>11} | {'log2(n)':>8}")
    print("-" * 34)
    for n in (15, 100, 200, 1000, 30000, 100000):
        ids = student_ids(n)
        # search for every 97th ID, plus the first, the last, and IDs that are NOT present
        targets = ids[::97] + [ids[0], ids[-1], ids[0] - 1, ids[-1] + 1]
        print(f"{n:>7} | {max_interrogations(ids, targets):>11} | {math.log2(n):>8.2f}")


if __name__ == "__main__":
    print("Problem 6 - Efficiency experiment")
    check("make_list(5, 'sorted')", run("make_list", make_list, 5, "sorted"), [1, 2, 3, 4, 5])
    check("make_list(5, 'reversed')", run("make_list", make_list, 5, "reversed"), [5, 4, 3, 2, 1])
    shuffled = run("make_list", make_list, 10, "shuffled")
    check("make_list(10, 'shuffled') has the same numbers", sorted(shuffled) if shuffled else None,
          list(range(1, 11)))
    check("max_interrogations on 15 IDs", run("max_interrogations", max_interrogations,
                                              student_ids(15), student_ids(15)), 4)
    summary()

    try:
        sort_table()
        search_table()
    except NotImplementedError:
        print("\nFinish the TODOs (and Problems 4 and 5) to see the tables.")
