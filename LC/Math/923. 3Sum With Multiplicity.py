class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        cnt = collections.Counter(arr);
        ans = 0
        for i in cnt:
            for j in cnt:
                remain = target - i - j
                if remain == i == j:
                    ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
                elif i == j:
                    ans += cnt[i] * (cnt[i] - 1) // 2 * cnt[remain]
                elif i < j < remain:
                    ans += cnt[i] * cnt[j] * cnt[remain]
        return ans % (10 ** 9 + 7)