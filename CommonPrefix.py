class Solution(object):
    def longestCommonPrefix(self, strs):
        result=[]
        strs.sort()
        first=strs[0]
        last=strs[len(strs)-1]

        for i in range(len(first)):
            if first[i]!=last[i]:
                break
            else:
                result.append(first[i])
        return ''.join(result)
    
obj=Solution()
print(obj.longestCommonPrefix(["dog","racecar","car"]))
        