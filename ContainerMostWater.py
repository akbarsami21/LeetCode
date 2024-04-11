class Solution(object):
    def maxArea(self,height):
        l=0
        r=len(height)-1
        max_area=float('-inf')
        while l<r:
            area=min(height[l],height[r])*(r-l)
            max_area=max(area,max_area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area

obj=Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))