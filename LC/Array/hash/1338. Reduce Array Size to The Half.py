class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = collections.Counter(arr)
        cc = sorted(c.items(), key=lambda x: x[1], reverse=True)  # 按照值从大到小排序

        # 转化为tuple
        # >>> x = Counter({'a':5, 'b':3, 'c':7})
        # >>> x.most_common()=[('c', 7), ('a', 5), ('b', 3)]
        freqsum = 0
        count = 0
        for n, freq in cc:
            freqsum += freq
            count += 1
            if freqsum >= len(arr) // 2:
                return count

