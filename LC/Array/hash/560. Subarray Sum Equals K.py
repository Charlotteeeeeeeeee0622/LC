# this problem could not use sliding window cuz
# sliding windows only fit for the condition : all positive, all negetive, or sorted
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prevsum = 0
        pmap = {0: 1}

        for n in nums:
            prevsum += n

            # exist num in, -num ->res
            if prevsum - k in pmap:
                res += pmap[prevsum - k]

            pmap[prevsum] = pmap.get(prevsum, 0) + 1

        return res