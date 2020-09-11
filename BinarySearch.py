class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:

        def BinarySearch(nums:[int],target:int):

            
            res=[]
            left=0
            right=len(nums)-1
            if right==-1:
                return [-1,-1]
            while left<=right:
                mid=int((left+right)/2)

                if target>=nums[mid]:
                    left=mid+1
                else:
                    right=mid-1

            if target>nums[-1]:
                return[-1,-1]
            elif target==nums[-1]:
                res.append(len(nums)-1)
            else:
                if nums[right]==target:
                    res.append(right)
                else:
                    return[-1,-1]
                

                            
            left=0
            right=len(nums)-1
            while left<=right:
                mid=int((left+right)/2)

                if target>nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
            
            if target<nums[0]:
                return[-1,-1]
            elif target==nums[0]:
                res.append(0)
            else:
                if nums[left]==target:
                    res.append(left)
                else:
                    return[-1,-1]
        
            return [res[1],res[0]]

        return BinarySearch(nums,target)
            
                    

a=Solution()
print(a.searchRange([2,2,4,5,6,10,11],3))

            

