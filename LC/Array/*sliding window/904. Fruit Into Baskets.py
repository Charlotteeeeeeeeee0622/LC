# https://leetcode.cn/problems/fruit-into-baskets/solution/shen-du-jie-xi-zhe-dao-ti-he-by-linzeyin-6crr/
# 没改好版本
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_len = -1
        res = [fruits[left]]

        for right in range(1, len(fruits)):
            max_len = max(max_len, right - left)

            if fruits[right] not in res and fruits[right] != fruits[right - 1]:
                res.append(fruits[right])

                while len(res) > 2:
                    max_len = max(max_len, right - left)
                    left = right - 1
                    while fruits[left] == fruits[left - 1]:
                        left -= 1
                    res = [fruits[left], fruits[right]]

        return max_len

# 作者amy原版本
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        right = 1
        max_len = -1
        res = [fruits[left]]

        while right < len(fruits):

            if fruits[right] not in res and fruits[right] != fruits[right - 1]:
                res.append(fruits[right])

                while len(res) > 2:
                    max_len = max(max_len, right - left)
                    left = right - 1
                    while fruits[left] == fruits[left - 1]:
                        left -= 1
                    res = [fruits[left], fruits[right]]
            right += 1

        return max(max_len, right - left)


# 失败尝试，res不能实现这个函数功能
# res.remove(fruits[left]),left不能只+=1
# res实现的是一个类似于set的功能，而res.remove(fruits[left])以后，可能窗口中间仍然有remove的那个值，会有三个值存在然后计算nsum的情况
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = []
        left = 0
        nsum = 0
        for right in range(len(fruits)):

            if fruits[right] not in res:
                res.append(fruits[right])

            while len(res) > 2:
                res.remove(fruits[left])
                left += 1

            nsum = max(nsum, right - left + 1)

        return nsum

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = []
        left = 0
        nsum = 0
        for right in range(len(fruits)):

            if fruits[right] not in res:
                res.append(fruits[right])

            while len(res) > 2:
                res.remove(fruits[left])
                left += 1
                while fruits[left - 1] == fruits[left]:
                    left += 1

            nsum = max(nsum, right - left + 1)

        return nsum

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = []
        left = 0
        nsum = 0
        for right in range(len(fruits)):

            if fruits[right] not in res:
                res.append(fruits[right])

            if len(res) > 2:
                res.remove(fruits[left])
                left += 1
                while fruits[left - 1] == fruits[left]:
                    left += 1
                while len(set(fruits[left:right + 1])) > 2:
                    left += 1
                    res = fruits[left:right + 1]

            nsum = max(nsum, right - left + 1)

        return nsum




