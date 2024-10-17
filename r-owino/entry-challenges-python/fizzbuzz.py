#!/usr/bin/env python3
"""The FizzBuzz problem"""

from typing import List, Union
def fizzbuzz() -> List[Union[str, int]]:
    """
    Prints the numbers from 1 to 100. For multiples of 3, prints "Fizz".
    For multiples of 5, prints "Buzz". For numbers that are multiples of 
    both 3 and 5, prints "FizzBuzz".

    Parameters
    ----------
    None

    Returns
    -------
    List[Union[str, int]]
        A list of length 100 where each element is either:
        - The integer itself (for non-multiples of 3 and 5),
        - The string "Fizz" (for multiples of 3),
        - The string "Buzz" (for multiples of 5),
        - The string "FizzBuzz" (for multiples of both 3 and 5)
    """
    res = []

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(i)
        
    return res

print(fizzbuzz())
