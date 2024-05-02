class Solution(object):
    def findMaxK(self, nums):
        num_set=set(nums)
        max_k=-1

        for num in nums:
            if num>0 and -num in num_set:
                max_k=max(num,max_k)
        return max_k
obj=Solution()
print(obj.findMaxK([-1,2,-3,3])) 