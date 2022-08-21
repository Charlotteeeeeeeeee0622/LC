class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # 就暴力判断是否存在某个位置的值是目标的值，且其他位的值都不大于目标数组的值，最多判断三回
        flag1, flag2, flag3 = False, False, False

        for arr in triplets:
            if arr[0] <= target[0] and arr[1] <= target[1] and arr[2] <= target[2]:
                if arr[0] == target[0]:
                    flags1 = True
                if arr[1] == target[1]:
                    flag2 = True
                if arr[2] == target[2]:
                    flag3 = True

        return flag1 and flag2 and flag3