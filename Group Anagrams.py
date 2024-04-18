from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        
        result=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            result[tuple(count)].append(s)
        return result.values()
    
obj=Solution()
print(obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
        