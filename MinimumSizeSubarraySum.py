class Solution(object):
    def minSubArrayLen(self, target, nums):
        l,total=0,0
        result=float('inf')

        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                result=min(r-l+1,result)
                total-=nums[l]
                l+=1
        return 0 if result==float('inf') else result
   

obj=Solution()
print(obj.minSubArrayLen(7,[2,3,1,2,4,3]))


        