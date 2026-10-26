"""Problem 7 - Armstrong numbers (5 points)        Chapter 5 Review Problem 38

A positive integer is an ARMSTRONG NUMBER if the sum of the CUBES of its
digits equals the number itself. Example:

    153  ->  1*1*1 + 5*5*5 + 3*3*3  =  1 + 125 + 27  =  153

Get the digits with arithmetic, not strings:
    n % 10   is the last digit        153 % 10  == 3
    n // 10  drops the last digit     153 // 10 == 15

Run this file to check your work:   python p7_armstrong_numbers.py
"""

from lab5_checks import check, run, summary
from lab5_data import ARMSTRONG_LIMIT


def sum_of_digit_cubes(n):
    """Return the sum of the cubes of the digits of n. Use a while loop."""
    total = 0 
    while n > 0: 
        digit = n % 10 
        total += digit ** 3 
        n //= 10 

    return total
    


def is_armstrong(n):
    """Return True if n is an Armstrong number."""
    number = n 
    t = number 
    p = len(str(n)) 
    s = 0 
    while t > 0: 
        d = t % 10 
        s += d ** p 
        t //= 10 

    if s == n: 
        return(True) 
    else: 
        return(False)


def armstrong_numbers(limit):
    """Return a list of every Armstrong number from 1 up to (not including) limit."""
    start = 1
    end = limit 
    armstrong_numbers = [
    n for n in range(start, end) 
    if sum(int(digit) ** len(str(n)) for digit in str(n)) == n
] 
    return(armstrong_numbers)



 




if __name__ == "__main__":
    print("Problem 7 - Armstrong numbers")
    check("sum_of_digit_cubes(153)", run("sum_of_digit_cubes", sum_of_digit_cubes, 153), 153)
    check("sum_of_digit_cubes(12)", run("sum_of_digit_cubes", sum_of_digit_cubes, 12), 9)
    check("is_armstrong(370)", run("is_armstrong", is_armstrong, 370), True)
    check("is_armstrong(100)", run("is_armstrong", is_armstrong, 100), False)
    result = run("armstrong_numbers", armstrong_numbers, ARMSTRONG_LIMIT)
    check(f"how many Armstrong numbers below {ARMSTRONG_LIMIT}", len(result) if result is not None else None, 13)
    print("  Armstrong numbers found:", result)
    summary()
