# Write a function that removes the even numbers from the given array and returns the resulting array.
#
# [execution time limit] 4 seconds (py3)
#
# [input] array.integer numbers
#
# Array of numbers
#
# [output] array.integer
#
# Array without even numbers
"""PROBLEM#5"""


# def removeEvens(numbers):
#     for index, x in enumerate(numbers):
#         if x % 2 == 0:
#             numbers.pop(index)
#     return numbers --->Changes ordedr of things


def removeEvens(numbers):
    odds = []
    for x in numbers:
        if x % 2 == 0:
            continue
        else:
            odds.append(x)
    return odds


"""PROBLEM6"""

# Given a sequence of integers, find its median.
#
# Example
#
# For sequence = [-1, 3, -2, 2], the output should be
# arrayMedian(sequence) = 0.5;
# For sequence = [1, 3, 2], the output should be
# arrayMedian(sequence) = 2.
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] array.integer sequence
#
# An unsorted array of integers.
#
# Guaranteed constraints:
# 2 ≤ sequence.length ≤ 105,
# -106 ≤ sequence[i] ≤ 106.
#
# [output] float
#
# The median of sequence.

def arrayMedian(sequence):
    sequence = sorted(sequence)
    length = len(sequence)
    if length%2 ==0:
        i1 = int(length/2)-1
        i2 = int(length/2)
        return (sequence[i2]+sequence[i1])/2
    else:
        return sequence[int((length-1)/2)]

"""PROBLEM#7""" """REDO"""


# Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing
# sequence by removing no more than one element from the array.
#
# Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence
# containing only one element is also considered to be strictly increasing.
#
# Example
#
# For sequence = [1, 3, 2, 1], the output should be
# almostIncreasingSequence(sequence) = false.
#
# There is no one element in this array that can be removed in order to get a strictly increasing sequence.
#
# For sequence = [1, 3, 2], the output should be
# almostIncreasingSequence(sequence) = true.
#
# You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can
# remove 2 to get the strictly increasing sequence [1, 3].
# input:
# sequence: [1, 3, 2]
# Expected Output:
# true

def almostIncreasingSequence(sequence):
    size = len(sequence)
    count = 0
    if size == 2:
        return True
    for i in range(size - 1):
        if sequence[i + 1] <= sequence[i]:
            count += 1
            skip_neighbor = i + 2 < size and sequence[i + 2] <= sequence[i]
            skip_back = i - 1 >= 0 and sequence[i + 1] <= sequence[i - 1]
            if skip_neighbor and skip_back or count >= 2:
                return False
    return True


"""PROBLEM#8"""
# You have a string s. Split s into the minimum possible number of increasing substrings.
# A substring is considered to be increasing when the next symbol in the substring is also nex
# t in the English alphabet. This is case sensitive, i.e. 'b' is next for 'a' but 'C' is not next for 'b'.
# Return an array of these substrings.
#
# Example
#
# For s = "ABCDEFFDEfghCBA", the output should be
# increasingSubstrings(s) = ["ABCDEF", "F", "DE", "fgh", "C", "B", "A"].
#
# Input/Output
#
# [execution time limit] 0.5 seconds (py3)
#
# [input] string s
#
# A string composed only of English letters.

def increasingsubstrings(s): """REDO"""
    inc = []
    start = ""
    for i in range(len(s)):
        if i == len(s) - 1:
            start += s[i]
            inc.append(start)
            break
        if ord(s[i]) == (ord(s[i + 1] - 1)):
            start += s[i]
        else:
            start += s[i]
            inc.append(start)
            start = ""

###Tests

# Input:
# s: "ABCDEFFDEfghCBA"
# Expected Output:
# ["ABCDEF",
#  "F",
#  "DE",
#  "fgh",
#  "C",
#  "B",
#  "A"]

# Test 5
# Input:
# s: "abababaabbaabab"
# Expected Output:
# ["ab",
#  "ab",
#  "ab",
#  "a",
#  "ab",
#  "b",
#  "a",
#  "ab",
#  "ab"]

# s: "JJYzKaHM"
# Expected Output:
# ["J",
#  "J",
#  "Y",
#  "z",
#  "K",
#  "a",
#  "H",
#  "M"]