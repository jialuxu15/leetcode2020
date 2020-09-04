class Solution:
    def search(self, nums: [int], target: int) -> int:

        def BinarySearch(nums:[int],target:int):
            low=0
            high=len(nums)-1


            while low<high:
                mid=int((low+high)/2)

                if target>nums[mid]:
                    low=mid+1
                elif target<nums[mid]:
                    high=mid-1
                else:
                    return mid

            if low== high:
                if nums[low]==target:
                    return low
                else:
                    return -1
           
        

        def Listinoder(nums:[int]):
            if len(nums)<2:
                return True
            elif len(nums)==2:
                if nums[0]<nums[1]:
                    return True
                else:
                    return False
            else:
                mid=int(len(nums)/2)
                if nums[mid]>nums[0] and nums[-1]>nums[mid]:
                    return True
                else:
                    return False
        
        

        def halfsearch(nums:[int],target:int):
            length=len(nums)
            half=int(length/2)
            if Listinoder(nums[:half]):
                res1=BinarySearch(nums[0:half],target)
            else:
                halfsearch(nums[:half],target)

            if Listinoder(nums[half:]):
                res2=BinarySearch(nums[half:],target)+half
            else:
                halfsearch(nums[half:],target)
            
            if res1>0:
                return res1
            elif  res2>0:
                return res2
            return-1

        halfsearch([4,5,6,7,0,1,2],0)
        

a=Solution()
print(a.search([4,5,6,7,0,1,2],0))

                