class Solution(object):
    def majorityElement(self, nums):
        result=nums[0]
        count=1

        for i in range(1,len(nums)):
            if nums[i]==result:
                count+=1
            else:
                count-=1
            
            if count==0:
                result=nums[i]
                count=1
        return result

obj=Solution()
print(obj.majorityElement([3,2,3,2]))
        