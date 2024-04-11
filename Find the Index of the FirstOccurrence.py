class Solution(object):
    def strStr(self, haystack, needle):
        
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i]==needle[0]:
                if haystack[i:len(needle)+i]==needle:
                    return i
                
        return -1

obj=Solution()
print(obj.strStr("sami", "mi"))
 