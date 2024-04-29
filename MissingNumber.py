class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        actual_sum=n*(n+1)//2
        nums_sum=sum(nums)
        return actual_sum-nums_sum
obj=Solution()
print(obj.missingNumber([9,6,4,2,3,5,7,0,1]))
        