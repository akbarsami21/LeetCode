class Solution(object):
    def singleNumber(self, nums):
        one=0
        two=0
        for num in nums:
            one=(one^num)&(~two)
            two=(two^num)&(~one)
        return one
obj=Solution()
print(obj.singleNumber([2,2,1,2,1,1,3]))
 