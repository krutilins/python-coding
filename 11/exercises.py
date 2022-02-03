from typing import Iterable


def test(nums):
  #Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five.
  return nums.count(19) == 2 and nums.count(5) >= 3

def test_1(nums: Iterable(int)):
  # Accept a list of integers and check the length and the fifth element. 
  # Return true if the length of the list is 8 and fifth element occurs thrice in the said list
  return len(nums) >= 5 and len(nums) == 8 and nums.count(nums[4]) == 3


def test_2(n):
  # Write a Python program that accept an integer test whether an integer greater than 4^4 and which is 4 mod 34.
  return n % 34 == 4 and n > 4 ** 4