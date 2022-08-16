# https://leetcode.com/problems/ugly-number-iii/discuss/769707/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def enough(num) -> bool:
            # x只要是a,b,c任何一个的倍数都可以
            totalnum = mid // a + mid // b + mid // c - mid // ab - mid // ac - mid // bc + mid // abc
            return totalnum >= n

        ab = a * b // math.gcd(a, b)
        bc = b * c // math.gcd(b, c)
        ac = a * c // math.gcd(a, c)
        # 注意下abc的最小公倍数是a和bc操作
        abc = a * bc // math.gcd(a, bc)

        left = 1
        right = 10 ** 10

        # 相等无线循环，若right正好取到target，left正好取到target-1
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return right
