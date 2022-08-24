if __name__ == '__main__':
    class Solution:
        def validWordAbbreviation(self, word: str, abbr: str) -> bool:
            # 同时遍历
            # while isnumeric
            i = 0
            j = 0
            k = ''
            while i < len(word) and j < len(abbr):
                k = ''
                if word[i] == abbr[j] or (abbr[j] == '1' and j == len(abbr) - 1):
                    i += 1;
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
                # elif abbr[j].isnumeric():
                #     while abbr[j].isnumeric() and j<len(abbr)-1:
                #         # 不管怎么改都会有bug，最主要问题是k为空字符串的问题，i的位置有问题
                #         k+=abbr[j]
                #         j+=1
                #     i+=int(k)
                # else:
                #     return False

            return i == len(word) and j == len(abbr)