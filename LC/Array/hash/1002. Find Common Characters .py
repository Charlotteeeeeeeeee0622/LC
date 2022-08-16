class Solution:
    def commonChars(self, words):
        res = collections.Counter(words[0])
        for word in words:
            res &= collections.Counter(word)
        return list(res.elements())