class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1 = p2 = 0
        res = []

        while p1 < len(firstList) and p2 < len(secondList):
            start1, end1 = firstList[p1][0], firstList[p1][1]

            start2, end2 = secondList[p2][0], secondList[p2][1]

            start, end = max(start1, start2), min(end1, end2)

            # firstList = [[0,2],[5,10],[13,23],[24,25]]
            # secondList = [[1,5],[8,12],[15,24],[25,26]]

            if start <= end:
                res.append([start, end])

            if end1 < end2:
                p1 += 1

            else:
                p2 += 1

        return res

        # why not directly plus one together
        # p1+=1
        # p2+=1