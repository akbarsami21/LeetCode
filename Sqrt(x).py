class Solution(object):
    def mySqrt(self, x):           
        
        left,right=0,x

        while left<=right:
            mid=left+((right-left)//2) 
            if mid**2>x:
                right=mid-1
            elif mid**2<x:
                left=mid+1
                result=False
            else:
                return True
        return result
                  
obj=Solution()
print(obj.mySqrt(3))