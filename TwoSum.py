class Solution(object):
    def twoSum(self, arr, target):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if target-arr[i]==arr[j]:
                    return [i,j]
        return None
   
ob=Solution()
print(ob.twoSum([1,3,1],2))