import unittest
import string
import random

"""
merge sort
  N log N

  In a best case, all of left and right lists will be sorted and it will
  march through the first and then append the second at each step. Using
  a recursive solution incurs some overhead but it is nicely readable. 

  For merge, worst case is that each compare swaps the march.

  In production, I would choose based on profiling, but especially initially
  the best code is what's already provided in an StdLib.

  In Python I was able to skip cases like mixes of numbers and characters.
  Languages like JS need to handle the mix of those as well as undefined,
  null, true, false, etc.

"""

def merge_sort(items):
  return merge(split(items), None)

def split(items):
  if len(items) == 1:
    return items

  if len(items) == 2:
    if items[1] > items[0]:
      return items
    else:
      return [items[1], items[0]]

  return merge(
    split(items[0 : int(len(items) / 2)]),
    split(items[int(len(items) / 2) : len(items)]),
  )

def merge(left, right):
  if right == None:
    return left

  result = []
  idx_left = 0
  idx_right = 0

  while True:
    if idx_left == len(left):
      return result + right[idx_right:]
    elif idx_right == len(right):
      return result + left[idx_left:]
    elif left[idx_left] < right[idx_right]:
      result.append(left[idx_left])
      idx_left += 1
    else:
      result.append(right[idx_right])
      idx_right += 1

### Tests --------------------------------------------------------------------
#-- Numeric Sort -------------------------------------------------------------
def test_numeric_with_one_value():
  input = [1]
  expected = [1]

  assert merge_sort(input) == expected

def test_numeric_with_two_values():
  input = [1, 2]
  expected = [1, 2]

  assert merge_sort(input) == expected

def test_numeric_with_two_values_in_reverse_order():
  input = [2, 1]
  expected = [1, 2]

  assert merge_sort(input) == expected

def test_numeric_with_even_number_of_values():
  input = [2, 3, 1, 4]
  expected = [1, 2, 3, 4]

  assert merge_sort(input) == expected

def test_numeric_with_odd_number_of_values():
  input = [2, 1, 4]
  expected = [1, 2, 4]

  assert merge_sort(input) == expected

def test_numeric_generated():
  input = [random.randrange(1000) for _ in range(0, 10000)]
  expected = input.copy()
  expected.sort()

  assert merge_sort(input) == expected
  
#-- Lexical Sort -------------------------------------------------------------
def test_lexical_with_one_value():
  input = ['a']
  expected = ['a']

  assert merge_sort(input) == expected

def test_lexical_with_two_values():
  input = ['a', 'b']
  expected = ['a', 'b']

  assert merge_sort(input) == expected

def test_lexical_with_two_values_in_reverse_order():
  input = ['b', 'a']
  expected = ['a', 'b']

  assert merge_sort(input) == expected

def test_lexical_with_even_number_of_values():
  input = ['b', 'c', 'a', 'd']
  expected = ['a', 'b', 'c', 'd']

  assert merge_sort(input) == expected

def test_lexical_with_odd_number_of_values():
  input = ['b', 'a', 'd']
  expected = ['a', 'b', 'd']

  assert merge_sort(input) == expected

def test_larger():
  input = list('The quick brown fox jumps over the lazy dog')
  expected = [
    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', 
    'a', 'b', 'c', 'd', 'e', 'e', 'e', 'f', 'g', 
    'h', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
    'o', 'o', 'o', 'p', 'q', 'r', 'r', 's', 't', 
    'u', 'u', 'v', 'w', 'x', 'y', 'z'
  ]

  assert merge_sort(input) == expected

def test_lexical_generated():
  input = [random.choice(string.ascii_letters) for _ in range(0, 10000)]
  expected = input.copy()
  expected.sort()

  assert merge_sort(input) == expected