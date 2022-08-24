class WordDistance:

    def __init__(self, words: List[str]):
        self.dic, self.l = {}, len(words)
        # try to record every str and their ind
        for i, w in enumerate(words):
            self.dic[w] = self.dic.get(w, []) + [i]

    # dic={}
    # words=["practice", "makes", "perfect", "coding", "makes"]
    # for i, w in enumerate(words):
    #     dic[w] = dic.get(w, []) + [i]
    # print(dic)
    # OUTPUT:{'practice': [0], 'makes': [1, 4], 'perfect': [2], 'coding': [3]}

    def shortest(self, word1: str, word2: str) -> int:
        # [3] [0]
        l1, l2 = self.dic[word1], self.dic[word2]
        i = j = 0
        # 5
        res = self.l
        # O(m+n) time complexity
        while i < len(l1) and j < len(l2):
            res = min(res, abs(l1[i] - l2[j]))
            # try to approach each other
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return res

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)