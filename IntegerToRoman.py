class Solution(object):
    def intToRoman(self, num):
        l=[['I',1],['IV',4],['V',5],['IX',9],['X',10],
           ['XL',40],['L',50],['XC',90],['C',100],['CD',400],['D',500],
           ['D',500],['CM',900],['M',1000]]

        result=""
        for key,val in reversed(l):
            if num//val:
                count=num//val
                result+=(key*count)
                num=num%val
        return result

obj=Solution()
print(obj.intToRoman(9))
        