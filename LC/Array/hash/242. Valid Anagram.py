#https://leetcode.com/problems/valid-anagram/discuss/66499/Python-solutions-(sort-and-dictionary).
# ——————————————Solution1————————————————
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in range(len(s)):
            record[ord(s[i]) - ord('a')] += 1
        for i in range(len(t)):
            record[ord(t[i]) - ord('a')] -= 1
        for i in range(len(record)):
            if record[i] != 0:
                return False
                break
        return True

# ——————————————Solution2————————————————
# by my self


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = [0] * 26
        for i in s:
            hashmap[ord(i) - ord('a')] += 1

        for i in t:
            hashmap[ord(i) - ord('a')] -= 1

        for i in range(len(hashmap)):
            if hashmap[i] != 0:
                return False
                break
        return True


# ——————————————Solution3————————————————
def isAnagram1(self, s, t):
    dic1, dic2 = {}, {}
    for item in s:
        dic1[item] = dic1.get(item, 0) + 1
    for item in t:
        dic2[item] = dic2.get(item, 0) + 1
    return dic1 == dic2


def isAnagram2(self, s, t):
    dic1, dic2 = [0] * 26, [0] * 26
    for item in s:
        dic1[ord(item) - ord('a')] += 1
    for item in t:
        dic2[ord(item) - ord('a')] += 1
    return dic1 == dic2


def isAnagram3(self, s, t):
    return sorted(s) == sorted(t)

def isAnagram4(self, s, t):
    return collections.Counter(s) == collections.Counter(t)