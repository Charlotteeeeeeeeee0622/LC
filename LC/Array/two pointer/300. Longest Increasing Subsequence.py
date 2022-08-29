# Dynamic programming + Dichotomy.
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        tails, res = [0] * len(nums), 0
        for num in nums:
            i = 0
            j = res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else:
                    j = m
            tails[i] = num
            if j == res: res += 1
        return res

# 直接看文字确实不太好懂，加个例子就比较容易明白
# 比如序列是78912345，前三个遍历完以后tail是789
# 这时候遍历到1，就得把1放到合适的位置，于是在tail二分查找1的位置，变成了189
# （如果序列在此时结束，因为res不变，所以依旧输出3）
# 再遍历到2成为129，然后是123直到12345
