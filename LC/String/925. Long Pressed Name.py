class Solution:
    #     def isLongPressedName(self, name: str, typed: str) -> bool:
    #         record=26*[0]
    #         for c in name:
    #             record[ord(c)-ord('a')]+=1

    #         for c in typed:
    #             record[ord(c)-ord('a')]-=1

    #         for i in range(len(record)):
    #             if record[i]>0:
    #                 return False

    #         return True

    def isLongPressedName(self, name, typed):
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)