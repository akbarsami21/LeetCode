class Solution(object):
    def compareVersion(self, version1, version2):
        version1_list=version1.split('.')
        version2_list=version2.split('.')
        len1=len(version1_list)
        len2=len(version2_list)

        for i in range(max(len1,len2)):
            i1=int(version1_list[i]) if i<len1 else 0
            i2=int(version2_list[i]) if i<len2 else 0

            if i1!=i2:
                return 1 if i1>i2 else -1
        return 0
obj=Solution()
print(obj.compareVersion("1.01","1.001"))
        