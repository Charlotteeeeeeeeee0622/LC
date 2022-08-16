# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         s = collections.Counter(s)
#         t = collections.Counter(t)
#
#         sres = []
#         tres = []
#
#         s = sorted(s.items(), key=lambda x: x[1], reverse=True)
#         t = sorted(t.items(), key=lambda x: x[1], reverse=True)
#
#         for key, freq in s:
#             sres.append(freq)
#
#         for key, freq in t:
#             tres.append(freq)
#
#         if sres == tres:
#             return True
#         else:
#             return False

# 无法满足 aabbaaba 和 bbaabbba
# https://leetcode.cn/problems/isomorphic-strings/solution/by-jyd-i4wt/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}
        for a, b in zip(s, t):
            # 对于已有映射 a -> s2t[a]，若和当前字符映射 a -> b 不匹配，
            # 说明有一对多的映射关系，则返回 false ；
            # 对于映射 b -> a 也同理
            if a in s2t and s2t[a] != b or \
               b in t2s and t2s[b] != a:
                return False
            s2t[a], t2s[b] = b, a
        return True

