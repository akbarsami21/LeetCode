class Solution(object):
    def isUgly(self, n):
        while n>1:
            if n%2==0:
                n//=2

            elif n%3==0:
                n//=3

            elif n%5==0:
                n//=5
            else:
                break
               
        return n==1
obj=Solution()
print(obj.isUgly(10))
            
        