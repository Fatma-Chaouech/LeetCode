class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        first = cost[0]
        second = cost[1]
        n = len(cost)
        if n <= 2 : 
            return min(first, second)
        
        for i in range(2, n) :
            cur_el = cost[i] + min(first, second)
            first = second 
            second = cur_el
        
        
        return min(first, second)
