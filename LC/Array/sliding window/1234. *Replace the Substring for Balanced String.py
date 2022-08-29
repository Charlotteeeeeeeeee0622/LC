# https://leetcode.com/problems/replace-the-substring-for-balanced-string/discuss/408978/JavaC%2B%2BPython-Sliding-Window
class Solution:
    def balancedString(self, s):
        count = collections.Counter(s)
        res = n = len(s)
        if all(n / 4 == count[char] for char in 'QWER'):
            return 0
        left = 0
        for right, char in enumerate(s):
            # 换掉一个right索引表示的char查看是否可以平衡
            count[char] -= 1
            while left <= right and all(n / 4 >= count[char] for char in 'QWER'):
                res = min(res, right - left + 1)
                count[s[left]] = count[s[left]] + 1
                left += 1
        return res

