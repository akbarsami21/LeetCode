import heapq

class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        workers = sorted((float(w) / q, q) for w, q in zip(wage, quality))
        res = float("inf")
        quality_sum = 0
        heap = []

        for cur_ratio, q in workers:
            heapq.heappush(heap, -q)
            quality_sum += q
            
            if len(heap) > k:
                quality_sum += heapq.heappop(heap)
            
            if len(heap) == k:
                res = min(res, quality_sum * cur_ratio)
        
        return res
obj=Solution()
print(obj.mincostToHireWorkers([10,20,5],[70,50,30],2))