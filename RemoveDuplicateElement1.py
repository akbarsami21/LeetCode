
class Solution(object):
    def removeDuplicates(self, nums):
        j=1
        for i in range(1,len(nums)):
            if nums[j-1]!=nums[i]:
                nums[j]=nums[i]
                j+=1
        return j
obj=Solution()
print(obj.removeDuplicates([1,1,2]))
        