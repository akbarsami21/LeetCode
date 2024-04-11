class Solution(object):
    def singleNumber(self, nums):
        xor=0
        for i in nums:
            xor=(xor^i)
        return xor
    
obj=Solution()
print(obj.singleNumber([4,1,2,1,2]))
  