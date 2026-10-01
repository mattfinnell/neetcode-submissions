class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        return min(
            self._min_cost(cost, 0, memo), 
            self._min_cost(cost, 1, memo)
        )

    def _min_cost(self, cost, i, memo):
        if i >= len(cost):
            return 0

        if i in memo:
            return memo[i]

        memo[i] = cost[i] + min(
            self._min_cost(cost, i + 1, memo), 
            self._min_cost(cost, i + 2, memo)
        )

        return memo[i]