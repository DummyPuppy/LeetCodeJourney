#Greedy algo
#jump game
#max jump step in the array is the value at that index
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) ==1:
            return True
        
        goal = len(nums)-1
        for i in range(len(nums)-2, -1,-1):
            if i+nums[i] >=goal:
                goal = i
        return True if goal == 0 else False
