class Solution(object):
    def isHappy(self, n):
        visit=set()

        while n not in visit:
            visit.add(n)
            n=self.sumOfSquare(n)

            if n==1:
                return True
        return False
    
    def sumOfSquare(self,n):
        output=0
        while n:
            digit=n%10
            digit=digit**2
            output+=digit
            n//=10
        return output

obj=Solution()
print(obj.isHappy(2))

        