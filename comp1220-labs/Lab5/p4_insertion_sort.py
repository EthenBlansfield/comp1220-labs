"""Problem 4 - Insertion sort (25 points)                   Section 5.4

Translate the insertion sort pseudocode (Figure 5.11) into Python.

Rules:
  * Sort the list IN PLACE: shuffle entries within the list you were given.
    Do not build a second list.
  * Do NOT use sort(), sorted(), min(), max(), insert(), pop(), copy(),
    list(), or any import that sorts.
  * Use the book's plan: the pivot starts at the SECOND entry; save the
    pivot in a temporary variable (this leaves a "hole"); slide larger
    names down into the hole; drop the pivot into the hole.
  * Count COMPARISONS: each time you compare an entry in the list with the
    pivot ("is the name above the hole greater than the pivot?"), add 1.
    Return that count.

Hint: Python lists start at index 0, so the book's "2nd entry" is index 1.

Run this file to check your work:   python p4_insertion_sort.py
"""

from lab5_checks import check, run, summary
from lab5_data import BAND_ROSTER, SMALL_LISTS


def insertion_sort(items, show=False):
    """Sort `items` in place into increasing order.

    Return the number of comparisons made between list entries.
    If show is True, print the list after each pass of the OUTER loop.
    """
    comparisons = 0

    for i in range(1, len(items)):
        current = items[i]
        j = i - 1

        while j >= 0:
            comparisons += 1
            if items[j] <= current:
                break
            items[j + 1] = items[j]
            j -= 1

        items[j + 1] = current

        if show:
            print(items)

    return comparisons


        
        



if __name__ == "__main__":
    print("Problem 4 - Insertion sort")

    roster = list(BAND_ROSTER)
    print("\nBefore:", roster)
    count = run("insertion_sort", insertion_sort, roster, True)
    print("After: ", roster)
    check("BAND_ROSTER is sorted", roster, sorted(BAND_ROSTER))

    for original in SMALL_LISTS:
        items = list(original)
        run("insertion_sort", insertion_sort, items)
        check(f"sorts {original}", items, sorted(original))

    check("comparisons for ['Al', 'Bo', 'Cy'] (already sorted)",
          run("insertion_sort", insertion_sort, ["Al", "Bo", "Cy"]), 2)
    check("comparisons for ['Cy', 'Bo', 'Al'] (reversed)",
          run("insertion_sort", insertion_sort, ["Cy", "Bo", "Al"]), 3)
    check("works on numbers too", run("insertion_sort", insertion_sort, [5, 4, 3, 2, 1]), 10)
    summary()
