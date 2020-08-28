class Solution:

    def letterCombinations(self, digits: str) -> [str]:
        if not digits:
            return 

        phone = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

       
        def backtrack(lettercombin:str,nextdigits:list):
            if len(nextdigits)==0:
                res.append(lettercombin)
                return print(lettercombin)
            else:
                for i in phone[nextdigits[0]]:
                    backtrack(lettercombin+i,nextdigits[1:])

        res=[]
        backtrack("",digits)
        return res

a=Solution()
a.letterCombinations("23")

        