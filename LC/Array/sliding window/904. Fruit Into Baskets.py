class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        l=0
        res=0
        nums=collections.Counter()
        for r in range(len(tree)):
            nums[tree[r]]+=1
            while len(nums)>2:
                nums[tree[l]]-=1
                if not nums[tree[l]]:
                    nums.pop(tree[l])
                l+=1
            res=max(res,r-l+1)
        return res

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




