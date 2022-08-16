class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        records = 26 * [0]
        for i in p:
            records[ord(i) - ord('a')] += 1

        res = []
        window = 26 * [0]
        left = 0

        for right in range(len(s)):

            while right - left + 1 > len(p):
                window[ord(s[left]) - ord('a')] -= 1
                left += 1

            window[ord(s[right]) - ord('a')] += 1
            if window == records:
                res.append(left)

        return res