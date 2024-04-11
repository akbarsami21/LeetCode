class Solution(object):
    def isPalindrome(self, s):
        arr=''
        for c in s:
            if c.isalnum():
                arr+=c.lower()
        return arr==arr[::-1]
        
obj=Solution()
print(obj.isPalindrome('A man, a plan, a canal: Panama'))
        