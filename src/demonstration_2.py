"""
Given a list of integers, your function should return `True` if any value
appears at least two times in the array. Your function should return `False` if
every element is unique.

Example:

Input: [1,3,3,2,1]
Output: True

Example:

Input: [0,1,2,3]
Output: False

*Note: In your first solution, it is okay to use a simple linear search. What
is the time complexity of this approach? Other possible solutions will have
time complexities of `O(n log n)` or `O(n)`. Possible space complexities are
`O(1)` or `O(n)`. Try to come up with solutions with different time and space
complexities and think about the tradeoffs between the solutions.*
"""


# Understand
# If there are two or more values in the array, return True
# Otherwise return False b/c values are unique
# Plan
# Track instances of every elements
# If there are two or more instances return False

# loop through  list
# Create a counter based on a dictionary, if counter==2  return True
# Keep track of repeating values using counts
#FIX CODE
# def contains_duplicate(nums):
#     counts = {}
#     for number in nums:
#         counts[number] = 1
#         if counts[number] == 2:
#             return True
#         else:
#             counts[number] += 1
#     return False
# Time: BigO(N), # Space Complex : BigO(N)

#Instructor's Solution
def contains_duplicate(nums):
   nums_count = {}

    # O(n)
    for n in nums:
        if n in nums_counts: # O(1)
            nums_count[n] += 1
        else:
            nums_count[n] = 1

    # O(n)
    for n in nums_count:
        if nums_counts[n] > 1: # O(1)
            return True

    return False
