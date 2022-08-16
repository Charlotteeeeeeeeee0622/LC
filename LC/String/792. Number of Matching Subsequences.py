
# #https://leetcode.cn/problems/number-of-matching-subsequences/solution/zhen-zheng-yun-xing-cheng-gong-de-python3jie-fa-zh/
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        for w in words:
            waiting[w[0]].append(iter(w[1:]))  # 存储以w[0]开头的前缀，此时waiting = {'a': [[], ['c', 'd'], ['c', 'e']], 'b': [['b']]}
        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)  # 在本题的例子中 it 分别为[]、['c', 'd']、['c', 'e']
        return len(waiting[None])

# https://leetcode.cn/problems/number-of-matching-subsequences/solution/792-pi-pei-zi-xu-lie-de-dan-ci-shu-liang-ge-bi-jia/
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        count = 0
        for i in words:
            num = 0
            pos = -1
            for j in i:
                pos = S.find(j, pos + 1)  # 从pos+1位置往后找，找不到返回-1
                if pos == -1:
                    break
                else:
                    num = num + 1
            if num == len(i):
                count = count + 1
        return count
