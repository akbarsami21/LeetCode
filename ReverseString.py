class Solution(object):
    def reverseWords(self, s):
    
       return ' '.join(s.split()[::-1])


obj=Solution()
print(obj.reverseWords('Hello World   '))
  