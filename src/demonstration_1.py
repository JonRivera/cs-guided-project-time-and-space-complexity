"""
Given a sorted array `nums`, remove the duplicates from the array.

Example 1:

Given nums = [0, 1, 2, 3, 3, 3, 4]

Your function should return [0, 1, 2, 3, 4]

Example 2:

Given nums = [0, 1, 1, 2, 2, 2, 3, 4, 4, 5]

Your function should return [0, 1, 2, 3, 4, 5].

*Note: For your first-pass, an out-of-place solution is okay. However, after
solving out-of-place, try an in-place solution with a space complexity of O(1).
For that solution, you will need to return the length of the modified `nums`.
The length will tell the user where the end of the array is after removing all
of the duplicates.*
"""

# Track Time for Code to Execute:
t0 = time.time()
# CODE BLOCK
t1 = time.time()
time1 = t1 - t0
import time


# Understand
# Remove Duplicates for given list
# Plan
# Need a way of tracking repeated elements
# If we have a repeated element then remove it from list.pop based on index
# Option#2:Can simply convert given list to set and then reconvert it back to a list

def remove_duplicates(nums):
    nums = list(set(nums))
    return nums
