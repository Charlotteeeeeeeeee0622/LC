#https://pythondict.com/python-qa/%E5%A6%82%E4%BD%95%E6%8C%89%E5%80%BC%E5%AF%B9counter%E6%8E%92%E5%BA%8F%EF%BC%9F-python/
import collections
from typing import List


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freq = {}
    for i in range(len(nums)):
        freq[nums[i]] = freq.get(nums[i], 0) + 1

    minpq = []
    for num, freq in freq.items():
        heapq.heappush(minpq, (freq, num))
        if len(minpq) > k:
            heapq.heappop(minpq)

    res = [0] * k
    for i in range(k - 1, -1, -1):
        res[i] = heapq.heappop(minpq)[1]
    return res


def top(nums: List[int], k: int) -> List[int]:
    c = collections.Counter(nums)
    sc = sorted([(freq, n) for n, freq in c.items()], reverse=True)
    res = []
    for n, freq in sc:
        res.append(freq)
    ans = []
    for i in range(k):
        ans.append(res.pop(0))
    return ans
    # c = collections.Counter(nums)
    # ans = []
    # for n, freq in c.items():

    #     ans.append(n)
    #
    # print(ans)
    # res = []
    # for i in range(k):
    #     res.append(ans.pop(0))
    # return res


if __name__ == '__main__':
    nums1 = [1, 2, 3, 3, 4, 4]
    k = 2
    print(top(nums1, k))

    nums2 = [4, 3, 2, 2, 1, 1]
    print(top(nums2, k))
