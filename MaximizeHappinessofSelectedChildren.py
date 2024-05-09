class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        happiness.sort()
        stack=happiness[:]
        i,maxhappies=0,0
        
        while k>0 and stack:
            curr=stack.pop()
            if(curr-i)>0:
                maxhappies+=(curr-i)
            i+=1
            k-=1
        return maxhappies
obj=Solution()
print(obj.maximumHappinessSum([1,2,3],2))
        