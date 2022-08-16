# https://leetcode.com/problems/binary-subarrays-with-sum/discuss/186683/C%2B%2BJavaPython-Sliding-Window-O(1)-Space

import collections

# ——————————————Solution1———————————————


def numSubarraysWithSum(self, nums, goal):
    # python做前缀表
    c = collections.Counter({0: 1})
    nsum = res = 0
    for i in nums:
        nsum += i
        # This is keeping track of when we get past goal,
        # as when we get past goal, we start with the new substring,
        # and we already have the count and use it when we reach the SUM again and again
        res += c[nsum - goal]
        c[nsum] += 1
    return res


if __name__ == '__main__':
    nums =[1,0,1,0,1]
    goal = 2
    numSubarraysWithSum(nums,goal)

# ——————————————Solution2————————————————
# count最多子数组问题都可以用这种姓氏的题解
# atMost(A, S) counts the number of the subarrays of A the sum of which is at most(less than or equal to) S.
# Therefore, we can use atMost(A, S) - atMost(A, S - 1)
# to get the number of the subarrays the sum of which is exactly S.


def numSubarraysWithSum(self, A, S):
    def atMost(S):
        if S < 0: return 0
        res = i = 0
        for j in range(len(A)):
            S -= A[j]
            while S < 0:
                S += A[i]
                i += 1
            res += j - i + 1
        return res
    return atMost(S) - atMost(S - 1)

def numSubarraysWithSum(self, A: List[int], S: int) -> int:
    def atmost(k):
        res = i = 0
        for j in range(len(A)):
            k -= A[j]
            while i <= j and k < 0:
                k += A[i]
                i += 1
            res += j-i+1
        return res
    return atmost(S) - atmost(S-1)

# class Solution:
#    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
#         nsum=0
#         left=0
#         res=[]
#         for right in range(len(nums)):
#             nsum+=nums[right]
#             while nsum>goal:
#                 nsum-=nums[left]
#                 left+=1
#             if nsum==goal:
#                 res.append(nums[left:right+1])
#             if right==len(nums)-1:
#                 nsum-=nums[left]
#                 left+=1
#                 if nsum==goal:
#                     res.append(nums[left:right+1])
#         return len(res)
