class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
      
        stones = list(map(lambda x: -1 * x, stones))
        heapq.heapify(stones)
        i = len(stones)
        while i > 1:
            
            y = -1 * heapq.heappop(stones)
            x = -1 * heapq.heappop(stones)
            i -= 2
            if x != y:
                i += 1
                heapq.heappush(stones, x - y)
            
        if len(stones) :
            return -1 * heapq.heappop(stones)
        
        else:
            return 0
            
            