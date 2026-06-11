class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCostToIdx = [0, 0] # idx = 2
        for i in range(2, len(cost) + 1):
            minCost = min(minCostToIdx[1] + cost[i - 1],
            minCostToIdx[0] + cost[i - 2])
            minCostToIdx[0] = minCostToIdx[1]
            minCostToIdx[1] = minCost

        return minCostToIdx[-1]

