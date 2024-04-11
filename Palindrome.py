class Solution(object):
    def isPalindrome(self, x):
        xstr=str(x)
        rev=xstr[::-1]
        if xstr==rev:
            return True
        else:
            return False

obj=Solution()
print(obj.isPalindrome(11))
        