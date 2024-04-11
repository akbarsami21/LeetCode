class Solution(object):
    def rotate(self, nums, k):
        k=k%len(nums)
        nums.reverse()
        nums[:k]=nums[:k][::-1]
        nums[k:]=nums[k:][::-1]
        return nums

obj=Solution()
print(obj.rotate([1,2,3,4,5,6,7],3))
        