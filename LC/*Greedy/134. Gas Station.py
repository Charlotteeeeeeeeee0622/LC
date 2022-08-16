#https://leetcode.cn/problems/gas-station/solution/shi-yong-tu-de-si-xiang-fen-xi-gai-wen-ti-by-cyayc/
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        rest = 0
        minrest = float('inf')
        road = []
        for i in range(len(gas)):
            rest += gas[i] - cost[i]
            if rest < minrest:
                minrest = rest
                minindex = i
        # 亏空最严重的一个点必须放在最后一步走，等着前面剩余的救助

        return -1 if rest < 0 else (minindex + 1) % len(gas)

#     public int canCompleteCircuit(int[] gas, int[] cost) {
#     int len = gas.length;
#     int spare = 0;
#     int minSpare = Integer.MAX_VALUE;
#     int minIndex = 0;

#     for (int i = 0; i < len; i++) {
#         spare += gas[i] - cost[i];
#         if (spare < minSpare) {
#             minSpare = spare;
#             minIndex = i;
#         }
#     }

#     return spare < 0 ? -1 : (minIndex + 1) % len;
# }
