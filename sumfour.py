class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        

        def slipwindow(nums:[int],sum:int):
    
            res=[]
            length=len(nums)
            left=0
            right=length-1

            while left<right:

                if nums[left]+nums[right]<sum:
                    left+=1
                elif nums[left]+nums[right]== sum:
                    res.append([nums[left],nums[right]])
                    right-=1
                    left+=1
                    
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                    while nums[right]==nums[right+1] and left<right:
                        right-=1
                    
                else:
                    right-=1
            return res
        
        result=[]
  
        nums.sort()
        
        if len(nums)==4:
            if nums[0]+nums[1]+nums[2]+nums[3]==target:
                return [nums]
            else:
                return []
    
        else:
            for i in range(len(nums)-3):
                if i>0 and nums[i]==nums[i-1]:
                    continue

                for j in range(i+1,len(nums)-2):
                    if j >i+1 and nums[j]==nums[j-1]:
                        continue
                    
                    twoset=slipwindow(nums[j+1:],target-nums[i]-nums[j])
                    if len(twoset)>0:   
                        for item in twoset:
                            result.append([nums[i],nums[j],item[0],item[1]])
                    else:
                        continue


            return result


a=Solution()
print(a.fourSum([1, 0, -1, 0, -2, 2],0))
