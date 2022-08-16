# ——————————————Solution1————————————————

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # in range
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        #         else:
        #             pass
        # return False
        # brute force 超时啦！！！

        # 绝妙的hashset解法
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

# ——————————————Solution2————————————————
# by my self


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set(nums)
        return True if len(hashset) < len(nums) else False
