class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        record = [0] * 11
        for b in bills:
            if b == 5:
                record[5] += 1
            elif b == 10:
                record[5] -= 1
                record[10] += 1
            elif b == 20:
                if record[5] and record[10]:
                    record[5] -= 1
                    record[10] -= 1
                else:
                    record[5] -= 3

            if record[5] < 0:
                return False
        return True


class Solution:
    def lemonadeChange(self, bills):
        five = ten = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                five, ten = five - 1, ten + 1
            elif ten > 0:
                five, ten = five - 1, ten - 1
            else:
                five -= 3
            if five < 0: return False
        return True