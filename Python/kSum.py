# kSum questiosn
#1 if it is two sums, use two pointers
#2 if it is 3 sums, usually use two pointers and one cursor
#3 if it is more than 3 sums, iterate through the kSum function, util it is the two sum function.
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def TwoSum(nums:List[int], target:int) -> List[List[int]]:
            sub = []
            low, high = 0, len(nums)-1
            while low < high:
                temp = nums[low]+nums[high]
                if temp > target or (high < len(nums)-1 and nums[high] == nums[high+1]):
                    high-=1
                elif temp < target or (low >0 and nums[low] == nums[low-1]):
                    low +=1
                else:
                    sub.append([nums[low],nums[high]])
                    low +=1
                    high -=1
            return sub


        def kSum(nums:List[int], k:int,target:int) -> List[List[int]]:
            result = []
            if not nums:
                return result
            nums.sort()
            
            average = target // k
            if average < nums[0] or average > nums[len(nums)-1]:
                return result
            if k == 2:
                return TwoSum(nums,target)
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in kSum(nums[i+1:],k-1,target- nums[i]):
                        result.append([nums[i]]+ subset)
            return result
        
        nums.sort()
        return kSum(nums,4,target)


        
