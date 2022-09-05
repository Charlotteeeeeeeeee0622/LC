class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: -abs(x[0] - x[1]))  # 前面的是绝对值最大的，也就是最不接近的
        n = len(costs) // 2;
        cost = 0;
        a = 0;
        b = 0
        for c in costs:
            if a == n:
                cost += c[1]
                b += 1
            elif b == n:
                cost += c[0]
                a += 1
            else:
                if c[0] < c[1]:
                    cost += c[0]
                    a += 1
                else:
                    cost += c[1]
                    b += 1
        return cost
