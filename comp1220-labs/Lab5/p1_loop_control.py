"""Problem 1 - Loop control (10 points)                     Section 5.4

Every loop needs three things: INITIALIZE, TEST, and MODIFY (Figure 5.7).
Write each function below. Do NOT use Python's built-in sum().

Run this file to check your work:   python p1_loop_control.py
"""

from lab5_checks import check, run, summary


# ---------------------------------------------------------------------------
# 1a. The book shows this loop, which never stops:
#
#       Number = 1
#       while (Number != 6):
#           Number = Number + 2
#
# DO NOT RUN IT. Instead, write a version that collects the odd numbers
# 1, 3, 5, ... that are less than `limit`, and is guaranteed to stop for
# ANY limit. Use a while loop (not range()).
# ---------------------------------------------------------------------------
def odd_numbers_below(limit):
    """Return a list of the odd numbers 1, 3, 5, ... that are < limit."""
    first_num = 1
    number_to_print = first_num 
    list_to_return = [] 

    while (number_to_print < limit):
        list_to_return.append(number_to_print) 
        print(number_to_print) 
        number_to_print = number_to_print + 2  
    return list_to_return
        
 


# ---------------------------------------------------------------------------
# 1b. Total a list with a for-each loop:   for Number in List: ...
# ---------------------------------------------------------------------------
def total(numbers):
    """Return the sum of the numbers in the list, using a for loop."""
    my_sum = 0 
    for number in numbers: 
        my_sum= my_sum + number
        print(number) 
    return my_sum



# ---------------------------------------------------------------------------
# 1c. Section 5.4, Question 2 gives this PRETEST loop:
#
#       Z = 0
#       X = 1
#       while (X < 6):
#           Z = Z + X
#           X = X + 1
#
# Python has no repeat...until (POSTTEST) loop. Rewrite the routine as a
# posttest loop by using   while True:   with an   if ...: break   as the
# LAST statement of the body. Return the final value of Z.
# ---------------------------------------------------------------------------
def repeat_until_version():
    """Return Z computed with a posttest (repeat ... until) loop."""
    Z = 0 
    X = 1 

    while True:
        Z = Z + X
        X = X + 1
        if (X >= 6): 
            break 

    return Z
        




    


if __name__ == "__main__":
    print("Problem 1 - Loop control")
    check("odd_numbers_below(6)", run("odd_numbers_below", odd_numbers_below, 6), [1, 3, 5])
    check("odd_numbers_below(7)", run("odd_numbers_below", odd_numbers_below, 7), [1, 3, 5])
    check("odd_numbers_below(1)", run("odd_numbers_below", odd_numbers_below, 1), [])
    check("total([4, 8, 15, 16, 23, 42])", run("total", total, [4, 8, 15, 16, 23, 42]), 108)
    check("total([])", run("total", total, []), 0)
    check("repeat_until_version()", run("repeat_until_version", repeat_until_version), 15)
    summary()
