"""Problem 3 - Let the computer solve the ages puzzle (15 points)   Section 5.3

In class we solved the "ages of three children" puzzle by hand:
  Clue 1: the product of the ages is 36.
  Clue 2: the sum of the ages is told to A, but it is NOT enough to decide.
  Clue 3: "the oldest child plays the piano" - so there IS one oldest child.

Now turn that reasoning into an algorithm. Each function is one clue.
Write each function so it works for ANY product, not just 36.

Represent a set of ages as a tuple (a, b, c) with a <= b <= c.

Run this file to check your work:   python p3_ages_puzzle.py
"""

from itertools import product, repeat

from lab5_checks import check, run, summary


# 3a. Clue 1. Use nested loops to try candidate ages.
def triples_with_product(product):
    """Return every (a, b, c) with a <= b <= c and a * b * c == product,
    in increasing order of a, then b."""
    vaild_age_combinations = [] 

    for first_child_age in range(product + 1): 
        for second_child_age in range(first_child_age, product + 1): 
            for third_child_age in range(second_child_age, product + 1): 
                if first_child_age * second_child_age * third_child_age == product:
                    vaild_age_combinations.append((first_child_age,second_child_age,third_child_age))
    print(vaild_age_combinations) 

    return(vaild_age_combinations)
            


# 3b. Clue 2. Which sums appear MORE than once among the triples?
def repeated_sums(triples):
    """Return a sorted list of the sums that occur for two or more triples.""" 
    seen = set() 
    duplicates = set()

    for triple in triples: 
        total = sum(triple) 

        if total in seen: 
            duplicates.add(total) 
        else: 
            seen.add(total)

    return sorted(duplicates)

   
    




# 3c. Clue 3. Is there a single oldest child (no tie for oldest)?
def has_unique_oldest(triple):
    """Return True if the largest age in the triple appears only once."""
    oldest = max(triple) 
    if triple.count(oldest) == 1:
        return True 
    elif triple.count(oldest) !=1:
        return False
    


# 3d. Put the three clues together.
def solve_ages(product):
    """Return the list of triples that survive all three clues."""
    def triples_with_product(product):
        vaild_age_combinations = [] 

        for first_child_age in range(product + 1): 
            for second_child_age in range(first_child_age, product + 1): 
             for third_child_age in range(second_child_age, product + 1): 
                if first_child_age * second_child_age * third_child_age == product:
                    vaild_age_combinations.append((first_child_age,second_child_age,third_child_age))
        print(vaild_age_combinations) 

        return(vaild_age_combinations) 
    
    def repeated_sums(triples):
        seen = set() 
        duplicates = set()

        for triple in triples: 
            total = sum(triple) 

            if total in seen: 
                duplicates.add(total) 
            else: 
                seen.add(total)

        return sorted(duplicates)  

    def has_unique_oldest(triple):
        oldest = max(triple) 
        if triple.count(oldest) == 1:
                return True 
        elif triple.count(oldest) !=1:
                return False
    triples = triples_with_product(product) 
    sums_that_repeat = repeated_sums(triples) 
    survivors = [ 
        triple for triple in triples 
        if sum(triple) in sums_that_repeat and has_unique_oldest(triple)
    ]
    print (survivors) 
    return survivors
    


if __name__ == "__main__":
    print("Problem 3 - Ages puzzle")
    triples = run("triples_with_product", triples_with_product, 36)
    check("number of triples with product 36", len(triples) if triples is not None else None, 8)
    check("first and last triple", (triples[0], triples[-1]) if triples else None, ((1, 1, 36), (3, 3, 4)))
    check("triples_with_product(12)", run("triples_with_product", triples_with_product, 12),
          [(1, 1, 12), (1, 2, 6), (1, 3, 4), (2, 2, 3)])
    check("repeated_sums for product 36", run("repeated_sums", repeated_sums, triples or []), [13])
    check("has_unique_oldest((2, 2, 9))", run("has_unique_oldest", has_unique_oldest, (2, 2, 9)), True)
    check("has_unique_oldest((1, 6, 6))", run("has_unique_oldest", has_unique_oldest, (1, 6, 6)), False)
    check("solve_ages(36)", run("solve_ages", solve_ages, 36), [(2, 2, 9)])
    check("solve_ages(72)", run("solve_ages", solve_ages, 72), [(3, 3, 8)])
    check("solve_ages(90)", run("solve_ages", solve_ages, 90), [(1, 9, 10), (2, 3, 15), (2, 5, 9), (3, 3, 10)]) 
    check("solve_ages(120)", run("solve_ages", solve_ages, 120),[])
    summary()