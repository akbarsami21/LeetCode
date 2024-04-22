class Solution(object):
    def permute(self, nums):
        resultList=[]
        self.back_tracking(resultList,[],nums)
        return resultList
    def back_tracking(self,resultList,tempList,nums):
        if len(tempList)==len(nums):
            resultList.append(list(tempList)) 
        
        for number in nums:
            if number in tempList:
                continue
            tempList.append(number)
            self.back_tracking(resultList,tempList,nums)
            tempList.pop()

obj=Solution()
print(obj.permute(['A','B','C']))