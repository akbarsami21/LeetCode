class Solution(object):
    def isValid(self, s):
        stack=[]
        hasmap={')':'(','}':'{',']':'[',}
        open_brackets=('(','{','[')

        for c in s:
            if c in open_brackets:
                stack.append(c)

            elif stack and stack[-1]==hasmap[c]:
                stack.pop()

            else:
                return False
        return False if stack else True

obj=Solution()
print(obj.isValid("{}())")) 
        