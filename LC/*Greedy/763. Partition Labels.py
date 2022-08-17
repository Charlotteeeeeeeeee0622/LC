class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        rightmost = {c: i for i, c in enumerate(s)}

        left = 0
        right = 0

        for i, c in enumerate(s):
            right = max(rightmost[c], right)
            if right == i:
                res.append(right - left + 1)
                left = right + 1

        return res


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex = {}
        res = []
        for i, c in enumerate(s):
            lastindex[c] = i
        groupsize=0
        groupend=0
        for i,c in enumerate(s):
            groupsize+=1
            groupend=max(groupend,lastindex[c])
            if i==groupend:
                res.append(groupsize)
                groupsize=0
                groupend+=1
        return res


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i

        group_end = 0
        group_size = 0
        res = []
        for i, c in enumerate(s):
            group_size += 1
            group_end = max(group_end, last_index[c])

            if i == last_index[c]:
                res.append(group_size)
                group_end += 1
                group_size = 0

        return res