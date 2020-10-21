"""
Given two strings `a` and `b`, write a function to determine if `a` is an
**anagram** of `b`.

*Note: an anagram is a word, phrase, or name formed by rearranging the letters
of another, such as cinema, formed from iceman.*

**Example:**

Input: `a` = "anagram", `b` = "nagaram"
Output `True`

**Example:**

Input: `a` = "bat", `b` = "tar"
Output `False`
"""


# understand we want
# to test whether string 1 and string2 are anagrams or words having the same letters arranged differently
def is_anagram(a, b):
    if a == b:
        return False
    elif len(a) == len(b) and set(list(a)) == set(list(b)):
        return True
    else:
        return False


