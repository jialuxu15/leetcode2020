import copy
class Solution:
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        
        candidates.sort()
        def backtrack(num:list,target:int,choice:list,begin:int):

            if sum(num)==target:
                if len(result)>0:
                    if num == result[-1]:
                        return
                result.append(copy.deepcopy(num))
                 
            elif sum(num)>target:
                return    
            for i in range(begin,len(choice)):
                if i>0:
                    if choice[i]==choice[i-1] and len(num)==0:
                        continue
                num.append(choice[i])
                backtrack(num,target,choice,i+1)
                num.pop(-1)
                   
        result=[]
        backtrack([],target,candidates,0)
        return result
        
a=Solution()
print(a.combinationSum2([4,2,5,2,5,3,1,5,2,2],9))