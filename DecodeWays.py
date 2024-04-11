class Solution(object):
    def find(self, i, msg, memo):
        if i == len(msg):
            return 1
          
        if msg[i] == '0':
            return 0
            
        if i in memo:
            return memo[i]

       
        one = self.find(i + 1, msg, memo)

        two = 0
       
        if i < len(msg) - 1 and (msg[i] == '1' or (msg[i] == '2' and msg[i + 1] <= '6')):
            two = self.find(i + 2, msg, memo)

       
        memo[i] = one + two
        return memo[i]

    def numDecodings(self, msg):
        if not msg:
            return 0
        memo = {}  
        return self.find(0, msg, memo)

sol = Solution()
print(sol.numDecodings("111111111111111111111111111111111111111111111")) 


# Creating an instance of Solution and calling numDecodings
sol = Solution()
print(sol.numDecodings('226'))  # Expected output: 3
