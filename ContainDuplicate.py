class Solution(object):
    def containsDuplicate(self, nums):
        res=set()
        for num in nums:
            if num in res:
                return True
            res.add(num)
        return False
obj=Solution()
print(obj.containsDuplicate([1,0,2,3,4]))
