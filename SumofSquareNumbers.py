class Solution(object):
    def judgeSquareSum(self, c):
        l,r=1,c
        while l<r:
            if l**2+r**2==c:
                return True
            elif l**2+r**2>c:
                r-=1
            else:
                l+=1
        return False
obj=Solution()
print(obj.judgeSquareSum(4))