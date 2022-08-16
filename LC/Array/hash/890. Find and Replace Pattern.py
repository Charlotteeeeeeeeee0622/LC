# https://leetcode.com/problems/find-and-replace-pattern/discuss/167943/Easy-Python-Solution-using-dictionary
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """

        def match(char, pattern):
            if len(char) != len(pattern):
                return False
            dic = {}
            for c, p in zip(char, pattern):
                if c not in dic:
                    if p in dic.values():
                        return False
                    dic[c] = p
                else:
                    if dic[c] != p:
                        return False
            return True

        res = []
        for char in words:
            if match(char, pattern):
                res.append(char)
        return res