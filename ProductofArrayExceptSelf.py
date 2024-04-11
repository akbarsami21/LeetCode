class Solution(object):
    def productExceptSelf(self, nums):
        result=[1]*(len(nums))
        pre=1
        for i in range(len(nums)):
            result[i]=pre
            pre*=nums[i]
        
        post=1
        for i in range(len(nums)-1,-1,-1):
            result[i]*=post
            post*=nums[i]

        return result
    
obj=Solution()
print(obj.productExceptSelf([1,2,3,4]))