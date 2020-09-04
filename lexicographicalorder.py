class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        length=len(nums)
        
        if length<2:
            return nums
        elif length==2:
            nums.reverse()
            return nums


        for i in range(length-1,0,-1):
            if nums[i]>nums[i-1]:
                break

        if i==1 and nums[1]<=nums[0]:
            nums.reverse()
            return nums

        P=nums[i-1]
        p=i-1

        for j in range(length-1,i-1,-1):
            if nums[j]>P:    
                break 
        K=nums[j]
        k=j   

 
        nums[p]=K
        nums[k]=P

        num=nums[p+1:]
        num.reverse()

        for i in range(len(num)):
            nums[p+1]=num[i]


        return nums


a=Solution()
print(a.nextPermutation([1,3,2]))
        

        

                
