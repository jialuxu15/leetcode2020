import copy

class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        
        def backtrack(num:list,target:int,choice:list,begin:int):

            if sum(num)==target:
                result.append(copy.deepcopy(num))
                print(num,result) 
                return 
            elif sum(num)>target:
                return    
            for i in range(begin,len(choice)):
                num.append(choice[i])
                backtrack(num,target,choice,i)
                num.pop(-1)
                   
        result=[]
        backtrack([],target,candidates,0)
        return result
        
a=Solution()
print(a.combinationSum([2,3,7],7))

