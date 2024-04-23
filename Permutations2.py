class Solution(object):
    def permuteUnique(self, nums):
        resultList=[]
        nums.sort()
        self.backtrack(resultList,[],nums,[False]*len(nums))
        return resultList
    def backtrack(self,resultList,tempList,nums,used):
        if len(tempList)==len(nums):
            resultList.append(list(tempList))
            return 
        for i in range(len(nums)):
            if used[i]:
                continue
            if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                continue
            used[i]=True
            tempList.append(nums[i])
            self.backtrack(resultList,tempList,nums,used)
            used[i]=False
            tempList.pop()

obj=Solution()
print(obj.permuteUnique([1,1,2]))
        