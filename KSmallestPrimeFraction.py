from heapq import heappop, heappush


class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        heap = []
        n = len(arr)
        for i in range(n-1):
            heappush(heap,(arr[i]/arr[-1],i,n-1))
        
        for i in range(k-1):
            res,l,r = heappop(heap)
            heappush(heap,(arr[l]/arr[r-1],l,r-1))

        res,l,r = heappop(heap)

        return [arr[l],arr[r]]


sol = Solution()
print(sol.kthSmallestPrimeFraction([1, 2, 3, 5], 3))  
print(sol.kthSmallestPrimeFraction([1, 7], 1))  
