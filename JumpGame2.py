class Solution(object):
    def jump(self, nums):
        farthest=0
        jumps=0
        current=0

        for i in range(len(nums)-1):
            farthest=max(farthest,nums[i]+i)

            if current==i:
                current=farthest
                jumps+=1
        return jumps
    
obj=Solution()
print(obj.jump([2,3,1,1,4]))
        