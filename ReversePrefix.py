class Solution(object):
    def reversePrefix(self, word, ch):
        try:
            index=word.index(ch)
            res=word[:index+1][::-1]
            return res+word[index+1:]
        except Exception:
            return word
        
        
obj=Solution()
print(obj.reversePrefix('abcdefd','d'))
        