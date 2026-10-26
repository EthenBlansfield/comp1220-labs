"""Shared data for Lab 5. Import from here; do not edit these lists.

    from lab5_data import BAND_ROSTER, CLASS_ROSTER, student_ids
"""

# Problem 4: an unsorted list of names (insertion sort).
BAND_ROSTER = [
    "Marisol", "Dev", "Quinn", "Abel", "Tamsin", "Jonah",
    "Beatriz", "Ollie", "Keiko", "Hugo", "Ingrid", "Ezra",
]

# Problem 4: a few small lists for testing edge cases.
SMALL_LISTS = [
    [],
    ["Zed"],
    ["Bo", "Al"],
    ["Al", "Bo", "Cy"],
    ["Cy", "Bo", "Al"],
    ["Fay", "Al", "Fay", "Bo"],   # duplicates
]

# Problem 5: a SORTED list of 31 names (binary search).
CLASS_ROSTER = [
    "Aaliyah", "Benedict", "Calvin", "Dahlia", "Eamon", "Farah", "Gideon",
    "Harper", "Isadora", "Jasper", "Kenji", "Lucia", "Malik", "Nadia",
    "Oscar", "Priya", "Quentin", "Rosalind", "Silas", "Talia", "Umar",
    "Vera", "Wesley", "Xiomara", "Yusuf", "Zara", "Zeke", "Zelda",
    "Zion", "Zoe", "Zuri",
]


def student_ids(count=30000, first=100001):
    """Return a sorted list of `count` student ID numbers starting at `first`.

    The default is 30,000 records, the size of the registrar's "current
    student" file in Section 5.6.
    """
    return list(range(first, first + count))


# Problem 7: the range of numbers to scan for Armstrong numbers.
ARMSTRONG_LIMIT = 1000
