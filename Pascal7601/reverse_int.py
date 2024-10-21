"""
program that takes an integer as input and
and returns the integer with reversed digit
ordering
"""

def reverse(num: int) -> int:
  """
  function that returns a reversed integer
  """
  if num < 0: # store the sign of the number
    op = -1
  else:
    op = 1

  num_str = str(abs(num)) # store the absolute value of the number as sting
  reversed_num = int(num_str[::-1])

  return reversed_num * op

