class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # 同时遍历
        # while isnumeric
        i = 0
        j = 0
        k = ''
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == "0":
                return False
            elif abbr[j].isnumeric():
                k = j
                while k < len(abbr) and abbr[k].isnumeric():
                    k += 1
                i += int(abbr[j:k])
                j = k
            else:
                return False
            # else:
            #     while abbr[j].isnumeric():
            #         j+=1
            #         k+=s[j]
            # i+=int(k)

        return i == len(word) and j == len(abbr)