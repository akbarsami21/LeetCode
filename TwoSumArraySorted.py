class Solution(object):
    def twoSum(self, numbers, target):
        left=0
        right=len(numbers)-1

        while left<right:
            if numbers[right]+numbers[left]==target:
                return [left+1,right+1]
            elif numbers[left]+numbers[right]>target:
                right-=1
            elif numbers[left]+numbers[right]<target:
                 left+=1
        return []
            
obj=Solution()
print(obj.twoSum([2,7,11,15],9))
        