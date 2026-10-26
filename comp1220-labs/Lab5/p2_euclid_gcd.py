"""Problem 2 - The Euclidean algorithm (10 points)     Sections 5.2 and 5.5

Section 5.2, Question 3 describes the Euclidean algorithm for the greatest
common divisor (GCD) of two positive integers X and Y:

    As long as neither X nor Y is zero, replace the LARGER of the two with
    the remainder of dividing the larger by the smaller. When one of them
    becomes zero, the GCD is the other (non-zero) value.

Python's remainder operator is %.   Example: 48 % 18 == 12
Do NOT use math.gcd.

Run this file to check your work:   python p2_euclid_gcd.py
"""

from lab5_checks import check, run, summary


# 2a. Iterative version: use a while loop.
def gcd(x, y):
    """Return the greatest common divisor of positive integers x and y."""
    temp1 = x
    temp2 = y
    while True: 
            modualus = temp1 % temp2 

            if modualus == 0: 
                 break

            temp1 = temp2
            temp2 = modualus 
    return temp2 



# 2b. Recursive version (Chapter 5 Review Problem 30). No loops allowed:
#     the function must call itself. What is the base case?
def gcd_recursive(x, y):
    """Return the GCD of x and y using recursion instead of a loop.""" 
    temp1 = x 
    temp2 = y 
    if temp2 == 0: 
         return temp1 
    else: 
         return gcd_recursive(temp2, temp1 % temp2) 




if __name__ == "__main__":
    print("Problem 2 - Euclidean algorithm")
    cases = [((48, 18), 6), ((18, 48), 6), ((17, 5), 1), ((100, 75), 25), ((7, 7), 7), ((1071, 462), 21)]
    for (x, y), expected in cases:
        check(f"gcd({x}, {y})", run("gcd", gcd, x, y), expected)
    for (x, y), expected in cases:
        check(f"gcd_recursive({x}, {y})", run("gcd_recursive", gcd_recursive, x, y), expected)
    summary()
