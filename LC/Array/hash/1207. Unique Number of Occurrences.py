import collections


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = collections.Counter(arr)
        dic = sorted(dic.items(), key=lambda x: x[1])

        res = []
        for n, freq in dic:
            res.append(freq)

        for r in range(1, len(res)):
            if res[r] == res[r - 1]:
                return False

        return True


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)
        return len(c) == len(set(c.values()))


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = set()
        for freq in collections.Counter(arr).values():
            if freq in seen:
                return False
            seen.add(freq)
        return True