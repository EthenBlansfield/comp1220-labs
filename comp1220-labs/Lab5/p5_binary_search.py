"""Problem 5 - Recursive binary search (20 points)          Section 5.5

Translate the binary search pseudocode (Figure 5.14) into Python.

Rules:
  * The function must be RECURSIVE: it calls itself on a smaller sublist.
    No while or for loops inside binary_search.
  * Use the book's "middle": the FIRST entry of the SECOND half.
    For a list of length n that is index n // 2.
  * Python slices give you the sublists:
        items[:m]      the entries BEFORE index m
        items[m + 1:]  the entries AFTER index m
  * Return True if the target is found, False otherwise.
  * Every time you look at a test entry, append it to the `visited` list,
    so we can see which entries were "interrogated".

Run this file to check your work:   python p5_binary_search.py
"""

from lab5_checks import check, run, summary
from lab5_data import CLASS_ROSTER


def binary_search(items, target, visited= []) -> bool:
    """Return True if target is in the sorted list `items`, else False.

    Append each test entry you examine to the list `visited`.
    """
    mid_item = int(len(items) // 2)
    length_of_list = len(items) 

    if length_of_list == 0: 
      return False
    visited.append(items[mid_item])  

    if items[mid_item] == target: 
        return True 
    elif len(items) == 1:
        return False 

    elif target > items[mid_item]: 
        top_half = items[mid_item+1:]
        found = binary_search(items = top_half, target= target, visited=visited)
        return found 
    elif target < items[mid_item]:  
        bottom_half = items[:mid_item] 
        found = binary_search(items = bottom_half, target= target, visited=visited) 
        return found  



        

        
        





def search_and_report(items, target):
    """Helper: run binary_search and return (found, visited)."""
    visited = []
    found = binary_search(items, target, visited)
    return found, visited


if __name__ == "__main__":
    print("Problem 5 - Binary search")
    check("find 'Priya'", run("binary_search", search_and_report, CLASS_ROSTER, "Priya"),
          (True, ["Priya"]))
    check("find 'Gideon'", run("binary_search", search_and_report, CLASS_ROSTER, "Gideon"),
          (True, ["Priya", "Harper", "Dahlia", "Farah", "Gideon"]))
    check("find 'Zuri' (last entry)", run("binary_search", search_and_report, CLASS_ROSTER, "Zuri"),
          (True, ["Priya", "Xiomara", "Zelda", "Zoe", "Zuri"]))
    check("'Brian' is not on the roster", run("binary_search", search_and_report, CLASS_ROSTER, "Brian"),
          (False, ["Priya", "Harper", "Dahlia", "Benedict", "Calvin"]))
    check("empty list", run("binary_search", search_and_report, [], "Anyone"), (False, [])) 
    check("find 'Benedict'", run("binary_search", search_and_report, CLASS_ROSTER, "Benedict"),
              (True, ['Priya', 'Harper', 'Dahlia', 'Benedict']))
    check("find 'Isador'", run("binary_search", search_and_report, CLASS_ROSTER, "Isador"),
          (False, ['Priya', 'Harper', 'Lucia', 'Jasper', 'Isadora']))
    check("find 'Eamon'", run("binary_search", search_and_report, CLASS_ROSTER, "Eamon"),
          (True, ['Priya', 'Harper', 'Dahlia', 'Farah', 'Eamon'])) 
    check("find 'Harper'", run("binary_search", search_and_report, CLASS_ROSTER, "Harper"),
            (True, ['Priya', 'Harper']))
    # Your own test: pick a name and predict the visited list BEFORE running.
    # Record your prediction and the actual result in written_answers.md.
    summary()
