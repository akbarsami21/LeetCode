class Solution(object):
    def lengthOfLastWord(self, s):
        count=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=' ':
                count+=1
            else:
                if count>0:
                    return count
        return count
    

obj=Solution()
print(obj.lengthOfLastWord('a'))
        
            
        