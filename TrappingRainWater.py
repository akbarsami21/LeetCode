class Solution(object):
    def trap(self, height):

        left=[0]*len(height)
        right=[0]*len(height)
        ans=0
        
        left[0]=height[0]
        for i in range(1,len(height)):
            left[i]=max(left[i-1],height[i])

        right[-1]=height[-1]
        for i in range(len(height)-2,-1,-1):
            right[i]=max(right[i+1],height[i])
        
        for i in range(len(height)):
            ans+=min(left[i],right[i])-height[i]
        
        return ans
obj=Solution()
print(obj.trap([4,2,0,3,2,5]))