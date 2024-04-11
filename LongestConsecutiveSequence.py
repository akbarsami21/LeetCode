class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        nums_set=set(nums)
        logest_cs=0

        for num in nums_set:
            if num-1 not in nums_set:
                current_element=num
                current_lenght=1
                
                while current_element+1 in nums_set:
                    current_element+=1
                    current_lenght+=1

                logest_cs=max(logest_cs,current_lenght)

        return logest_cs
    
obj=Solution()
print(obj.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))



