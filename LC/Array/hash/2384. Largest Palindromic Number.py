# strip(): returns a new string after removing any leading and trailing whitespaces including tabs (\t).
# rstrip(): returns a new string with trailing whitespace removed. It’s easier to remember as removing white spaces from “right” side of the string.
# lstrip(): returns a new string with leading whitespace removed, or removing whitespaces from the “left” side of the string.
from collections import Counter


def largestPalindromic(self, num: str) -> str:
    count = Counter(num)
    res = ''.join(count[i] // 2 * i for i in '9876543210').lstrip('0')
    mid = max(count[i] % 2 * i for i in count)
    return (res + mid + res[::-1]) or '0'