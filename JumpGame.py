class Solution(object):
    def canJump(self, nums):
        n=len(nums)-1
        last_position=n
        for i in range(n-1,-1,-1):
            if i+nums[i]>=last_position:
                last_position=i
            
        if last_position==0:
            return True 
        else: 
            return False

obj=Solution()
print(obj.canJump([3,2,1,0,4]))