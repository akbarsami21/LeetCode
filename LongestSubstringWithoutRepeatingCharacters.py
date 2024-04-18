class Solution(object):
    def lengthOfLongestSubstring(self, s):
        chrset=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in chrset:
                chrset.remove(s[l])
                l+=1
            chrset.add(s[r])
            res=max(res,r-l+1)
        return res
            
obj=Solution()
print(obj.lengthOfLongestSubstring('abcabcss'))
        