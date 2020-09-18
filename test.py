class Solution:
    def lengthOfLastWord(self, s: str) -> int:


        a=''
        for i in range(len(s)-1,-1,-1):
            if s[i] ==' ' and a=='':
                continue
            elif s[i]==' ' and len(a)>0:
                break
            else:
                a+=s[i]
                
        return a,len(a)

a=Solution()
print(a.lengthOfLastWord("hello world  "))
