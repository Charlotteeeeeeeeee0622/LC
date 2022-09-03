class Solution:
    def isPossible(self, A):
        left = collections.Counter(A)
        end = collections.Counter()
        for i in A:
            if not left[i]: continue
            left[i] -= 1
            if end[i - 1] > 0:
                end[i - 1] -= 1
                end[i] += 1
            elif left[i + 1] and left[i + 2]:
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
            else:
                return False
        return True

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        tail = collections.Counter()
        for i in nums:
            if counter[i] and tail[i-1]: # 可以衔接
                counter[i]-=1
                tail[i-1]-=1
                tail[i]+=1
                continue
            if counter[i] and counter[i+1] and counter[i+2]: # 可以生成新序列
                tail[i+2] += 1
                counter[i] -= 1
                counter[i+1] -= 1
                counter[i+2] -= 1
                continue
            if counter[i]:
                return False
        return True