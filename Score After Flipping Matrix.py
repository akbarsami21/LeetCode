class Solution(object):
    def matrixScore(self, grid):
        row,col=len(grid),len(grid[0])
        res=row*2**(col-1)
        for i in range(1,col):
            count=0
            for j in range(row):
                if grid[j][i]!=grid[j][0]:
                    count+=1
            count=max(count,row-count)
            res+=count*(2**(col-i-1))
        return res
obj=Solution()
print(obj.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))        