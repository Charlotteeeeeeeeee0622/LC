# https://leetcode.com/problems/minimum-number-of-keypresses/discuss/2027810/Python-3-or-Greedy-or-Explanation
# class Solution:
import collections


def minimumKeypresses(s: str) -> int:
    pressnum = 0
    count = 0
    c = collections.Counter(s)
    #print(c)
    for i, freq in sorted(c.values(), reverse=True):
        if i % 9 == 0:
            count += 1
        pressnum += count * freq


if __name__ == '__main__':
    s = "apple"
    print(minimumKeypresses(s))
